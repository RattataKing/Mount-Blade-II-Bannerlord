from lxml import etree

# Parse the XML file
file_path = 'crafting_templates.xml'
tree = etree.parse(file_path)
root = tree.getroot()

# Find the "TwoHandedSword" CraftingTemplate
two_handed_sword_template = root.xpath("//CraftingTemplate[@id='TwoHandedSword']")

# List to hold usable piece ids
usable_pieces_ids = []

if two_handed_sword_template:
    # Find all the UsablePiece elements under TwoHandedSword template
    usable_pieces = two_handed_sword_template[0].xpath(".//UsablePiece")
    
    # Extract piece_id from each UsablePiece
    for piece in usable_pieces:
        usable_pieces_ids.append(piece.get("piece_id"))

# Print or save the list of usable piece IDs
print("Usable pieces for TwoHandedSword:")
for piece_id in usable_pieces_ids:
    print(piece_id)

# Save the list of usable piece IDs to a file
with open('usable_pieces_ids.txt', 'w') as f:
    f.write("Usable pieces for TwoHandedSword:\n")
    for piece_id in usable_pieces_ids:
        f.write(f"{piece_id}\n")

print("Usable pieces saved to 'usable_pieces_ids.txt'.")