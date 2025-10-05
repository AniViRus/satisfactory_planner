import os
import sys
import json

# redirect stdout and stderr because Windows is dumb
if sys.stdout is None or sys.stderr is None:
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w') 

data_file = 'Data\\data.json'

# Load your JSON data
with open(data_file, 'r') as file:
    data = json.load(file)

# Check for missing 'products' key in recipes
for recipe_name, recipe_data in data['recipes'].items():
    if 'products' not in recipe_data:
        print(f"Recipe '{recipe_name}' is missing the 'products' key.")
