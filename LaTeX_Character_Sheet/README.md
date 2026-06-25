# 📖 D&D 5.5e (2024) LaTeX Character Sheet Template

This folder contains a custom, high-aesthetic LaTeX template for a D&D 5e (2024) character sheet, heavily inspired by modern 3rd party Pinterest layouts and visual grids.

---

## 📂 File Structure

- **[character_sheet.tex](file:///d:/D&D/LaTeX_Character_Sheet/character_sheet.tex)**: The main layout and document structure. Compile this file to generate your PDF.
- **[character_data.tex](file:///d:/D&D/LaTeX_Character_Sheet/character_data.tex)**: The character database containing all scores, levels, names, and proficiencies. **This is the only file you need to modify when leveling up or changing character stats.**
- **[dnd5e_sheet.sty](file:///d:/D&D/LaTeX_Character_Sheet/dnd5e_sheet.sty)**: The LaTeX package containing custom layout variables, color themes, and TikZ macros for stats.

---

## ⚡ How to Update Character Stats

To update your character sheet (e.g. when leveling up or changing items):
1. Open [character_data.tex](file:///d:/D&D/LaTeX_Character_Sheet/character_data.tex).
2. Change the macro values (e.g., change `\CharLevel{6}` to `\CharLevel{7}`).
3. Re-compile the document! The LaTeX engine will automatically re-run the calculations for modifiers, saving throws, skills, and HP maximums.

---

## 🚀 How to Compile

You can compile this project in two ways:

### 1. Locally (Offline)
Make sure you have a LaTeX distribution installed (such as TeX Live, MiKTeX, or MacTeX).

Using a terminal, run:
```bash
pdflatex character_sheet.tex
```
or (if using system fonts):
```bash
xelatex character_sheet.tex
```

### 2. Online (Overleaf)
1. Zip the folder contents: `character_sheet.tex`, `character_data.tex`, and `dnd5e_sheet.sty`.
2. Go to [Overleaf](https://www.overleaf.com), create a blank project, and click **Upload**.
3. Upload the zipped file and click **Recompile**!
