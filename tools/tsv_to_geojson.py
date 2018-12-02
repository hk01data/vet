import pandas as pd
import json

df = pd.read_csv('vet.tsv', sep='\t', encoding='utf-8')
df = df.fillna('')



geojson_features = []
for index, row in df.iterrows():
    geo = {
        "type":"Point",
             "coordinates":[  
                row['Longitude'],
                row['Latitude']
             ]
    }
    

    data = {
        "last_updated": row['last_updated'],
        "chi_name": row['chi_name'],
        "chi_address": row['chi_address'],
        "district": row['district'],
        "tel1": row['tel1'],
        "tel2": row['tel2'],
        "tel3": row['tel3'],
        "website": row['website'],
        "fb_page": row['fb_page'],
        "remarks": row['remarks'],
        "opening_hours": row['opening_hours'],
        "weekday_text": row['weekday_text']
    }


    features = {
        "type": "Feature",
        "properties" : data,
        "geometry" : geo
    }
    geojson_features.append(features)
    #print(json.loads(str(row['opening_hours'])))


geojson = {
    "type":"FeatureCollection",
    "features": geojson_features
}

#print(json.dumps(geojson, indent=4, sort_keys=True, ensure_ascii=False))
print(geojson)
with open('file.txt', 'w', encoding='utf-8') as file:
     file.write(json.dumps(geojson, ensure_ascii=False))