from lxml import etree
import pandas as pd
from collections import defaultdict

# Parse the XML file
file_path = 'std_crafting_pieces_xml-zho-CN.xml'  # Adjust to your actual file path
tree = etree.parse(file_path)
root = tree.getroot()

# Dictionary to store occurrences of each translation text
name_count = defaultdict(int)

# List to store the extracted data
data = []

# Helper function to convert number to letter (A, B, C, etc.)
def int_to_letter(n):
    return chr(64 + n)  # chr(65) is 'A', so chr(64 + 1) gives 'A', chr(64 + 2) gives 'B', and so on.

# Iterate over each 'string' element to extract 'id' and 'text' attributes
for string_element in root.findall(".//string"):
    # Extract the 'id' and 'text' attributes, checking if they exist
    string_id = string_element.get('id')
    string_text = string_element.get('text')

    # Proceed only if both 'id' and 'text' exist
    if string_id and string_text:
        # Increment the count for this translation text
        name_count[string_text] += 1
        
        # If the name repeats, rename the first occurrence with "A" and increment for subsequent occurrences
        if name_count[string_text] == 2:
            # Rename the first occurrence by finding and renaming it with "A"
            for item in data:
                if item['text'] == string_text:
                    item['text'] = f"{string_text}A"
                    break
            # Now rename this second occurrence as "B"
            string_text = f"{string_text}B"
        elif name_count[string_text] > 2:
            # For further duplicates, append the appropriate letter (C, D, etc.)
            string_text = f"{string_text}{int_to_letter(name_count[string_text])}"
        
        # Append the data to the list
        data.append({'id': string_id, 'text': string_text})

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file = 'extracted_strings_with_unique_letters.csv'  # Adjust to your desired output path
df.to_csv(output_file, index=False)

print(f"Data extracted and saved to {output_file}")
