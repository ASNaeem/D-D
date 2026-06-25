#!/usr/bin/env python3
import os
import re
import time
import argparse
import urllib.parse
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

BASE_URL = "http://dnd2024.wikidot.com"

# Class names to match class prefixes
CLASSES = [
    "artificer", "barbarian", "bard", "cleric", "druid", "fighter",
    "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"
]

def clean_name(name):
    """Clean URL name to a neat title case string (e.g. shield-of-faith -> Shield of Faith)"""
    # Replace dashes with spaces
    spaced = name.replace("-", " ")
    # Capitalize except for minor words
    minor_words = {"of", "the", "and", "a", "an", "in", "to", "for", "with", "by", "at", "from"}
    words = spaced.split()
    capitalized = []
    for i, word in enumerate(words):
        if i > 0 and word.lower() in minor_words:
            capitalized.append(word.lower())
        else:
            capitalized.append(word.capitalize())
    return " ".join(capitalized)

def get_local_path(url_path):
    """
    Map a Wikidot relative URL path to a local workspace file path.
    Returns (local_absolute_path, category)
    """
    url_path = url_path.strip("/")
    if not url_path:
        return None, None

    # Handle formats like "species:aasimar", "feat:alert", "paladin:oath-of-devotion"
    parts = url_path.split(":")
    if len(parts) == 1:
        # Check if it is a main class page e.g. "paladin"
        name = parts[0]
        if name in CLASSES:
            class_name = clean_name(name)
            return os.path.join("Classes", class_name, f"{class_name} - D&D 5e (2024).md"), "classes"
        return None, None

    prefix, name = parts[0], parts[1]
    name_clean = clean_name(name)

    if prefix == "species":
        if name == "all":
            return None, None
        return os.path.join("Race", f"Race_{name_clean}.md"), "species"
    elif prefix == "background":
        if name == "all":
            return None, None
        return os.path.join("Backgrounds", f"Background_{name_clean}.md"), "backgrounds"
    elif prefix == "feat":
        if name == "all":
            return None, None
        return os.path.join("Feats", f"Feat_{name_clean}.md"), "feats"
    elif prefix == "spell":
        if name == "all":
            return None, None
        return os.path.join("Spells", f"Spell_{name_clean}.md"), "spells"
    elif prefix == "equipment":
        if name == "all":
            return None, None
        return os.path.join("Equipment", f"Equipment_{name_clean}.md"), "equipment"
    elif prefix == "magic-item":
        if name == "all":
            return None, None
        return os.path.join("MagicItems", f"MagicItem_{name_clean}.md"), "magic-items"
    elif prefix in CLASSES:
        class_name = clean_name(prefix)
        # Check if main page or subclass
        if name == "main" or name == "spell-list" or name == "spell":
            return os.path.join("Classes", class_name, f"{class_name} - D&D 5e (2024).md"), "classes"
        else:
            return os.path.join("Classes", class_name, "Subclasses", f"Sublcass_{class_name} - {name_clean}.md"), "classes"

    return None, None

def convert_html_to_md(soup, current_file_path):
    """Convert HTML soup to Markdown, rewriting links and tables nicely."""
    
    def walk(node, indent=0):
        if isinstance(node, NavigableString):
            # Clean string data
            text = str(node)
            # Remove redundant formatting within text
            return text
        
        if not isinstance(node, Tag):
            return ""

        tag_name = node.name

        # Ignore ads, comments, scripts, styles
        if tag_name in ["script", "style", "noscript", "iframe"]:
            return ""
        if "error-block" in node.get("class", []):
            return ""
        if node.get("id") in ["wad-tier3-above-content", "wad-tier3-below-content"]:
            return ""

        # Handle headings
        if tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(tag_name[1])
            # Process content inside heading
            content = "".join(walk(c) for c in node.contents).strip()
            return f"\n\n{'#' * level} {content}\n\n"

        # Handle paragraphs
        if tag_name == "p":
            content = "".join(walk(c) for c in node.contents).strip()
            return f"\n\n{content}\n\n" if content else ""

        # Handle line breaks
        if tag_name == "br":
            return "\n"

        # Handle inline bold/italic
        if tag_name in ["strong", "b"]:
            content = "".join(walk(c) for c in node.contents)
            return f"**{content}**" if content.strip() else content
        if tag_name in ["em", "i"]:
            content = "".join(walk(c) for c in node.contents)
            return f"*{content}*" if content.strip() else content

        # Handle links
        if tag_name == "a":
            href = node.get("href", "")
            content = "".join(walk(c) for c in node.contents)
            if not href:
                return content
            
            # Rewrite internal relative links
            parsed_href = urllib.parse.urlparse(href)
            is_internal = False
            path_to_check = href
            
            if not parsed_href.scheme and href.startswith("/"):
                is_internal = True
                path_to_check = parsed_href.path
            elif parsed_href.netloc == "dnd2024.wikidot.com":
                is_internal = True
                path_to_check = parsed_href.path

            if is_internal:
                local_target_rel, _ = get_local_path(path_to_check)
                if local_target_rel:
                    # Calculate relative link between local files
                    # e.g. current = "Classes/Paladin/Paladin - D&D 5e (2024).md"
                    # target = "Spells/Spell_Shield of Faith.md"
                    # relpath = "../../Spells/Spell_Shield of Faith.md"
                    current_dir = os.path.dirname(current_file_path)
                    rel_link = os.path.relpath(local_target_rel, current_dir).replace("\\", "/")
                    return f"[{content}]({rel_link})"
                else:
                    # If we don't map it, make it relative to the home page or absolute
                    return f"[{content}]({BASE_URL}{path_to_check})"

            return f"[{content}]({href})"

        # Handle lists
        if tag_name in ["ul", "ol"]:
            list_items = []
            for i, child in enumerate(node.contents):
                if isinstance(child, Tag) and child.name == "li":
                    item_content = "".join(walk(c) for c in child.contents).strip()
                    # Strip excessive leading/trailing newlines
                    item_content = re.sub(r'^\n+', '', item_content)
                    item_content = re.sub(r'\n+$', '', item_content)
                    # Replace interior double-newlines with single ones
                    item_content = item_content.replace("\n\n", "\n")
                    
                    prefix = "1. " if tag_name == "ol" else "- "
                    indent_str = "    " * indent
                    list_items.append(f"{indent_str}{prefix}{item_content}")
            return "\n" + "\n".join(list_items) + "\n"

        # Handle collapsible blocks (Wikidot style)
        if "collapsible-block" in node.get("class", []):
            summary = "Show Details"
            folded_link = node.find(class_="collapsible-block-folded")
            if folded_link:
                summary = folded_link.get_text().strip("+ \xa0\n\t")
            
            unfolded_content = node.find(class_="collapsible-block-content")
            if unfolded_content:
                content = "".join(walk(c) for c in unfolded_content.contents).strip()
                return f"\n\n<details>\n<summary>{summary}</summary>\n\n{content}\n\n</details>\n\n"
            return ""

        # Handle tables
        if tag_name == "table":
            rows = node.find_all("tr")
            if not rows:
                return ""
            
            md_rows = []
            max_cols = 0
            
            # First pass: parse cell contents and determine column count
            parsed_rows = []
            for row in rows:
                cells = row.find_all(["td", "th"])
                parsed_cells = []
                for cell in cells:
                    cell_text = "".join(walk(c) for c in cell.contents).strip()
                    # Clean up cells to not break Markdown table layout (replace newlines with <br>)
                    cell_text = cell_text.replace("\n\n", "<br>").replace("\n", "<br>")
                    cell_text = cell_text.replace("|", "\\|") # Escape pipes
                    parsed_cells.append(cell_text)
                if parsed_cells:
                    parsed_rows.append(parsed_cells)
                    max_cols = max(max_cols, len(parsed_cells))

            if not parsed_rows:
                return ""

            # Standardize column count for all rows
            for r in parsed_rows:
                while len(r) < max_cols:
                    r.append("")

            # Generate markdown table
            header_row = parsed_rows[0]
            md_rows.append("| " + " | ".join(header_row) + " |")
            
            # Alignment row
            alignments = []
            for col_idx in range(max_cols):
                # Simple alignment logic: align center if content looks numeric
                alignments.append(":---:")
            md_rows.append("| " + " | ".join(alignments) + " |")

            # Data rows
            for data_row in parsed_rows[1:]:
                md_rows.append("| " + " | ".join(data_row) + " |")

            return "\n\n" + "\n".join(md_rows) + "\n\n"

        # Walk all other containers (div, span, etc.)
        return "".join(walk(c) for c in node.contents)

    # Convert the entire content
    md = walk(soup)
    
    # Post-process cleanup of newlines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

def scrape_page(url_path, output_dir):
    """Scrape a single Wikidot page, convert to Markdown, and save."""
    full_url = f"{BASE_URL}/{url_path.lstrip('/')}"
    print(f"Scraping: {full_url}")
    
    try:
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error downloading {full_url}: {e}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    content_div = soup.find(id="page-content")
    if not content_div:
        print(f"Error: No #page-content div found on {full_url}")
        return False

    # Get local path
    local_path, category = get_local_path(url_path)
    if not local_path:
        print(f"Skipping {url_path}: URL prefix does not map to a configured category directory.")
        return False

    # Adjust output directory
    abs_output_path = os.path.join(output_dir, local_path)
    os.makedirs(os.path.dirname(abs_output_path), exist_ok=True)

    # Process and convert content
    page_title = soup.find(class_="page-title")
    title_str = page_title.get_text().strip() if page_title else clean_name(url_path.split(":")[-1])
    
    markdown_content = convert_html_to_md(content_div, local_path)
    
    final_markdown = f"# {title_str}\n\n"
    # Add source credit metadata
    final_markdown += f"Source: D&D 5e (2024) Wikidot <{full_url}>\n\n"
    final_markdown += markdown_content

    with open(abs_output_path, "w", encoding="utf-8") as f:
        f.write(final_markdown)

    print(f"Saved: {abs_output_path}")
    return True

def crawl_category(category, output_dir, limit=None):
    """Crawl a category index page to collect and scrape all leaf pages."""
    category_urls = {
        "species": "species:all",
        "backgrounds": "background:all",
        "feats": "feat:all",
        "spells": "spell:all"
    }

    if category not in category_urls:
        print(f"Category '{category}' is not crawlable.")
        return

    index_url_path = category_urls[category]
    full_index_url = f"{BASE_URL}/{index_url_path}"
    print(f"Crawling index: {full_index_url}")

    try:
        response = requests.get(full_index_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error downloading index {full_index_url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    content_div = soup.find(id="page-content")
    if not content_div:
        print(f"Error: No #page-content div found on index.")
        return

    # Find all internal links matching target patterns
    prefix_map = {
        "species": "species",
        "backgrounds": "background",
        "feats": "feat",
        "spells": "spell"
    }
    prefix = prefix_map.get(category, category)
    pattern = re.compile(rf"^/{prefix}:[a-z0-9-]+$")
    links_to_scrape = []
    
    for a in content_div.find_all("a"):
        href = a.get("href", "")
        if pattern.match(href):
            links_to_scrape.append(href)

    # Deduplicate and sort
    links_to_scrape = sorted(list(set(links_to_scrape)))
    print(f"Found {len(links_to_scrape)} pages to scrape in category '{category}'")

    if limit:
        links_to_scrape = links_to_scrape[:limit]
        print(f"Limited run: Scraping first {limit} pages.")

    scraped_count = 0
    for i, path in enumerate(links_to_scrape):
        success = scrape_page(path, output_dir)
        if success:
            scraped_count += 1
        # Politeness delay
        if i < len(links_to_scrape) - 1:
            time.sleep(1.0)

    print(f"Finished. Successfully scraped {scraped_count}/{len(links_to_scrape)} pages.")

def crawl_classes(output_dir):
    """Scrape class main pages and their subclass pages."""
    print("Scraping D&D 2024 classes and subclasses...")
    
    for class_name in CLASSES:
        # 1. Scrape main class page
        main_path = f"/{class_name}:main"
        success = scrape_page(main_path, output_dir)
        if not success:
            continue
            
        time.sleep(1.0)
        
        # 2. Fetch subclass links from main class page
        full_class_url = f"{BASE_URL}/{class_name}:main"
        try:
            response = requests.get(full_class_url, timeout=10)
            response.raise_for_status()
            class_soup = BeautifulSoup(response.text, "html.parser")
            content_div = class_soup.find(id="page-content")
            
            # Find subclass links
            subclass_pattern = re.compile(rf"^/{class_name}:[a-z0-9-]+$")
            subclass_links = []
            if content_div:
                for a in content_div.find_all("a"):
                    href = a.get("href", "")
                    # Exclude index/main subpages
                    if subclass_pattern.match(href) and not href.endswith((":main", ":spell-list", ":spell")):
                        subclass_links.append(href)
            
            subclass_links = sorted(list(set(subclass_links)))
            print(f"Found {len(subclass_links)} subclasses for {class_name.capitalize()}")
            
            for sub_link in subclass_links:
                scrape_page(sub_link, output_dir)
                time.sleep(1.0)
                
        except Exception as e:
            print(f"Error fetching subclasses for {class_name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="D&D 5e (2024) Wikidot Scraper")
    parser.add_argument("--url", help="Scrape a single specific page URL path (e.g. 'species:aasimar')")
    parser.add_argument("--category", choices=["species", "backgrounds", "feats", "spells", "classes"],
                        help="Scrape an entire category (e.g., species, backgrounds, feats, spells, classes)")
    parser.add_argument("--limit", type=int, help="Limit number of pages scraped in a category (for testing)")
    default_output = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--output", default=default_output, help="Workspace output directory (defaults to parent of scraper folder)")

    args = parser.parse_args()

    if args.url:
        scrape_page(args.url, args.output)
    elif args.category == "classes":
        crawl_classes(args.output)
    elif args.category:
        crawl_category(args.category, args.output, args.limit)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
