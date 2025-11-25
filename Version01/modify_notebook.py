
import json

notebook_path = "1.- Introducción a Python. Python Avanzado/1. Sesión-1.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# The target cell is at index 5 (0-indexed)
# It's a code cell containing "conda update conda\nconda update anaconda"
if len(notebook_content['cells']) > 5 and \
   notebook_content['cells'][5]['cell_type'] == 'code' and \
   notebook_content['cells'][5]['source'] == ['conda update conda\n', 'conda update anaconda']:
    
    notebook_content['cells'][5]['source'] = []
    print(f"Successfully cleared code cell at index 5 in {notebook_path}")
else:
    print(f"Target code cell not found or content mismatch in {notebook_path}. No changes made.")
    # For debugging, print the actual content if it's a code cell at that index
    if len(notebook_content['cells']) > 5 and notebook_content['cells'][5]['cell_type'] == 'code':
        print(f"Actual content: {notebook_content['cells'][5]['source']}")


with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4)
