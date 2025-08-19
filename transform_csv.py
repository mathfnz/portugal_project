# %%
import pandas as pd
import json

csv_filename = 'infrastructure_braga.csv'
json_filename = 'infrastructure_braga.json'

# %%
try:
    print(f"Reading input file: {json_filename}..")
    with open(json_filename, 'r', encoding="utf-8") as open_json:
        data = json.load(open_json)
    elements = data["elements"]
    print("Converting...")
    df = pd.json_normalize(elements)
    print(f"Saving data to output file: {csv_filename}...")
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print("\nConversion completed successfully!")
    print(f"File '{csv_filename}' was created with {len(df)} rows and {len(df.columns)} columns.")

except FileNotFoundError:
    print(f"ERROR: The input file '{json_filename}' was not found.")
    print("Please run the 'extracao_osm.py' script first to generate it.")
except KeyError:
    print(f"ERROR: The key 'elements' was not found in '{json_filename}'.")
    print("The JSON file might be empty or have an unexpected format.")

# %%
df
