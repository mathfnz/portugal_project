# %% 
import json
import requests

overpass_url = "https://overpass-api.de/api/interpreter"

overpass_query = """
[out:json];
area[name="Braga"]->.searchArea;
(
  node["amenity"="school"](area.searchArea);
  node["amenity"="hospital"](area.searchArea);
  node["railway"="station"](area.searchArea);
);
out center;
"""

# %% API request
print("Requesting infrastructure data for Braga...")
response = requests.get(overpass_url, params={"data": overpass_query})

# %% Verifying if the request was succed and creating json file
if response.status_code == 200:
    print("Request successful!")
    data = response.json()
    
    with open('infrastructure_braga.json', 'w', encoding='utf-8') as open_json:
        json.dump(data, open_json, ensure_ascii=False, indent=4)
    print("Data saved successfully. File 'infrastructure_braga.json' created.")
    print(f"Total elements found: {len(data['elements'])}")
        
else:
    print(f"Request failed! Status code: {response.status_code}")
    print("API Response: ")
    print(response.text)

