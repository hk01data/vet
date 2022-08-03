import pandas as pd
import json

df = pd.read_csv("vet.tsv", sep="\t", encoding="utf-8")
df = df.fillna("")

geojson_features = []
for index, row in df.iterrows():
    geo = {
        "type":"Point",
             "coordinates":[  
                row["Longitude"],
                row["Latitude"]
             ]
    }
    

    data = {
        "last_updated": row["last_updated"],
        "id": row["id"],
        "chi_name": row["chi_name"],
        "chi_address": row["chi_address"],
        "district": row["district"],
        "tel1": row["tel1"],
        "tel2": row["tel2"],
        "tel3": row["tel3"],
        "website": row["website"],
        "fb_page": row["fb_page"],
        "remarks": row["remarks"],
        "head_ad1_image": row["head_ad1_image"],
        "head_ad1_href": row["head_ad1_href"],
        "head_ad1_start": row["head_ad1_start"],
        "head_ad1_end": row["head_ad1_end"],
        "head_ad2_image": row["head_ad2_image"],
        "head_ad2_href": row["head_ad2_href"],
        "head_ad2_start": row["head_ad2_start"],
        "head_ad2_end": row["head_ad2_end"],
        "footer_ad1_image": row["footer_ad1_image"],
        "footer_ad1_href": row["footer_ad1_href"],
        "footer_ad1_start": row["footer_ad1_start"],
        "footer_ad1_end": row["footer_ad1_end"]
    }

    if row["opening_hours"] == "":
        data["opening_hours"] = ""
    else:
        data["opening_hours"] = json.loads(row["opening_hours"])

    if row["weekday_text"] == "":
        data["weekday_text"] = ""
    else:
        data["weekday_text"] = json.loads(row["weekday_text"])


    features = {
        "type": "Feature",
        "properties" : data,
        "geometry" : geo
    }
    geojson_features.append(features)


geojson = {
    "type":"FeatureCollection",
    "features": geojson_features
}

with open("parsed.geojson", "w", encoding="utf-8") as file:
     file.write(json.dumps(geojson, indent=4, ensure_ascii=False))
# print(json.dumps(geojson, indent=4, ensure_ascii=False))