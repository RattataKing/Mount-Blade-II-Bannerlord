from lxml import etree
import pandas as pd

# Parse the XML file
file_path = 'crafting_pieces.xml'  # Adjust to your actual file path
tree = etree.parse(file_path)
root = tree.getroot()

# List to store the extracted data
data = []

# Iterate over each 'CraftingPiece' element to extract all attributes and materials
for crafting_piece in root.findall(".//CraftingPiece"):
    # Extract attributes of the crafting piece
    piece_id = crafting_piece.get('id')
    raw_name = crafting_piece.get('name')
    tier = crafting_piece.get('tier')
    piece_type = crafting_piece.get('piece_type')
    mesh = crafting_piece.get('mesh')
    culture = crafting_piece.get('culture')
    length = crafting_piece.get('length')
    weight = crafting_piece.get('weight')
    is_hidden = crafting_piece.get('is_hidden')
    crafting_cost = crafting_piece.get('CraftingCost')

    # Split the name into string_id and clean name
    if raw_name:
        name_split = raw_name.split('}')
        string_id = name_split[0][2:] if len(name_split) == 2 else None
        clean_name = name_split[1] if len(name_split) == 2 else raw_name
    else:
        string_id, clean_name = None, None

    # Extract BladeData-related attributes (stack_amount, physics_material, etc.)
    blade_data = crafting_piece.find('BladeData')
    if blade_data is not None:
        stack_amount = blade_data.get('stack_amount')
        physics_material = blade_data.get('physics_material')
        body_name = blade_data.get('body_name')

        # Extract thrust and swing data
        thrust = blade_data.find('Thrust')
        swing = blade_data.find('Swing')
        if thrust is not None:
            thrust_damage_type = thrust.get('damage_type')
            thrust_damage_factor = thrust.get('damage_factor')
        else:
            thrust_damage_type, thrust_damage_factor = None, None

        if swing is not None:
            swing_damage_type = swing.get('damage_type')
            swing_damage_factor = swing.get('damage_factor')
        else:
            swing_damage_type, swing_damage_factor = None, None
    else:
        stack_amount, physics_material, body_name = None, None, None
        thrust_damage_type, thrust_damage_factor = None, None
        swing_damage_type, swing_damage_factor = None, None

    # Extract materials (id and count) and concatenate them
    materials_list = []
    materials_section = crafting_piece.find('Materials')
    if materials_section is not None:
        for material in materials_section.findall('Material'):
            material_id = material.get('id')
            material_count = material.get('count')
            materials_list.append(f"{material_id}: {material_count}")

    # Join all materials into a single string
    materials_combined = ', '.join(materials_list) if materials_list else None

    # Append the data to the list
    data.append({
        'id': piece_id,
        'string_id': string_id,
        'name': clean_name,
        'tier': tier,
        'piece_type': piece_type,
        'mesh': mesh,
        'culture': culture,
        'length': length,
        'weight': weight,
        'is_hidden': is_hidden,
        'CraftingCost': crafting_cost,
        'stack_amount': stack_amount,
        'physics_material': physics_material,
        'body_name': body_name,
        'thrust_damage_type': thrust_damage_type,
        'thrust_damage_factor': thrust_damage_factor,
        'swing_damage_type': swing_damage_type,
        'swing_damage_factor': swing_damage_factor,
        'materials': materials_combined
    })

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file = 'extracted_crafting_pieces_new.csv'  # Adjust to your desired output path
df.to_csv(output_file, index=False)

print(f"Data extracted and saved to {output_file}")
