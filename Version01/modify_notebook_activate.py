
import json

notebook_path = "1.- Introducción a Python. Python Avanzado/1. Sesión-1.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# Modify the source activate command
if len(notebook_content['cells']) > 11 and \
   notebook_content['cells'][11]['cell_type'] == 'code' and \
   notebook_content['cells'][11]['source'] == ['source activate programads']:
    
    notebook_content['cells'][11]['source'] = ['conda activate programads']
    print(f"Successfully updated 'source activate' command in {notebook_path}")

    # Now, remove the redundant cells (Windows title and activate command)
    if len(notebook_content['cells']) > 13 and \
       notebook_content['cells'][12]['cell_type'] == 'markdown' and \
       notebook_content['cells'][13]['cell_type'] == 'code' and \
       notebook_content['cells'][13]['source'] == ['activate programads']:
        
        del notebook_content['cells'][13]
        del notebook_content['cells'][12]
        print(f"Successfully removed redundant activation cells from {notebook_path}")
    else:
        print(f"Redundant activation cells not found or content mismatch. No cells removed.")

else:
    print(f"'source activate' code cell not found or content mismatch. No changes made.")


with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4)
