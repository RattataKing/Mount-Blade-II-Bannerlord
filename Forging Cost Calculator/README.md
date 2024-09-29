## Game Version: v1.2.11.45697

**Tool Link (Google Sheet):** [forging_cost_calculator](https://docs.google.com/spreadsheets/d/1g8_KZIT8FpruhnJnLDpKgjLW_icW5kl0nXgo94aG2HU/edit?usp=sharing)

### Contents

- **XML Templates:** 
  - `crafting_pieces.xml` -> Contains all crafting parts and their associated information, such as materials, damage factors, and more.
  - `crafting_templates.xml` -> Determines which crafting parts can be used to create various weapon types (e.g., two-handed sword, one-handed axe, etc.).
  - `std_crafting_pieces_xml-zho-CN.xml` -> Simplified Chinese translation for each crafting part.

- **Python Scripts:** 
  - `2h_sword_useable_id.py` -> Extracts a list of usable part IDs for two-handed swords.
  - `extract_items.py` -> Extracts all crafting parts and their attributes.
  - `extract_translation_duplication_rename.py` -> Extracts string IDs and their Simplified Chinese translations. If duplication occurs, part names are renamed (e.g., samenameA, samenameB).

- **Note:** 
  - In `crafting_templates.xml`, for two-handed swords, the part `mp_aserai_handed_sword_pommel` is duplicated. You will need to manually remove this duplicate entry after extraction.

### How to Use
1. **In sheet 'Core':** Edit fundamental prices (optional).
2. **In sheet 'formula':** Select parts by typing and searching keywords for blade, guard, handle, and pommel.
3. Est. cost will auto-show up, you can also manually fill in the sword name and trade price.
4. Copy the cells to manage and record more combinations.
5. You can click `View > Hidden sheets` to see full information.
6. **This README is trash, please explore the tool yourself**

Feel free to contribute by submitting issues or pull requests for improvements.
Feel free to report any bugs or issues encountered during use.