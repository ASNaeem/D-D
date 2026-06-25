# 📖 D&D 2024 Wikidot Scraper Guide

This directory contains the Python-based web scraper that downloads D&D 5e (2024) content from `http://dnd2024.wikidot.com/`, converts it into clean Markdown files, and rewrites internal wiki links to point to local workspace paths.

---

## 🛠️ Prerequisites

The scraper requires **Python 3** and a few dependencies:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Run the Scraper

You can run the scraper directly from this folder (`d:\D&D\Scraper`):

### 1. Scrape a Single Specific Page
Downloads a page and converts it. The argument is the relative Wikidot path.
```bash
python scraper.py --url species:aasimar
python scraper.py --url feat:alert
```

### 2. Scrape a Whole Category
Downloads all pages within a given index. Supported categories: `species`, `backgrounds`, `feats`, `spells`, `classes`.
```bash
python scraper.py --category species
python scraper.py --category backgrounds
```

### 3. Test Scrape with a Limit
To test the scraper without downloading a massive list (e.g. all 170+ feats), use the `--limit` flag:
```bash
python scraper.py --category feats --limit 5
```

### 4. Scrape Classes and Subclasses
```bash
python scraper.py --category classes
```

---

## 📂 Default Output Location

By default, files are saved relative to the D&D project root directory (`d:\D&D\`) regardless of where you execute the script from:
- `species` mapping -> `Race/Race_{Name}.md`
- `backgrounds` mapping -> `Backgrounds/Background_{Name}.md`
- `feats` mapping -> `Feats/Feat_{Name}.md`
- `spells` mapping -> `Spells/Spell_{Name}.md`
- `classes` & subclasses -> `Classes/`

### Customizing the Output Directory
You can override the default output location using the `--output` flag:
```bash
python scraper.py --category species --output C:\path\to\custom\folder
```

---

## 🔗 How Relative Link Rewriting Works
When the scraper encounters an internal link (e.g. `href="/spell:light"` inside a background page), it calculates the relative path from the output file to the target spell page.
For example, inside `Backgrounds/Background_Acolyte.md`, the link is converted to:
`[Magic Initiate (Cleric)](../Feats/Feat_Magic Initiate.md)`

This allows full offline navigation of the wiki content directly inside your Obsidian vault or Markdown editor.
