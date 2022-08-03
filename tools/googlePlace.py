import requests
import json
import pandas as pd


# df = pd.read_csv('vet.csv', encoding = 'utf8')
# df = df[111:]

API_KEY = 'AIzaSyAo1IdMwXkSVsDc3-ZVrzdj9iDRFXO4wFs'

# Retrieve place_id
# URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
# place_id = []
# for idx, name in enumerate(df['獸醫診所名稱']):
#     print('{} {}'.format(idx+1, name))

#     param = {
#         'input': name,
#         'inputtype': 'textquery',
#         'fields':'',
#         'key': API_KEY
#     }
#     r = requests.get(URL, params = param)

#     json_data = json.loads(r.text)
#     print(json_data)
#     if json_data['status'] == 'OK':
#         print(json_data['candidates'][0])
#         place_id.append(json_data['candidates'][0]['place_id'])
#     else:
#         print(json_data['status'])
#         place_id.append(json_data['status'])

# print(place_id)

# df['place_id'] = place_id
# df.to_csv('vet_id.csv', encoding = 'utf8')


# Retrieve place openinghours
URL = 'https://maps.googleapis.com/maps/api/place/details/json?'
df = pd.read_csv('input_files/vet_id.csv', encoding = 'utf8')
# df = df[:2]
place_details = []

for idx, pid in enumerate(df['place_id']):
    print('{} {}'.format(idx+1, pid))

    param = {
        'key': API_KEY,
        'placeid': pid,
        'language': 'zh-TW',
        'fields':'geometry/location,website,opening_hours,permanently_closed'
    }
    if pid:
        r = requests.get(URL, params = param)
        json_data = json.loads(r.text)
        if json_data['status'] == 'OK':
            print(json_data)
            place_details.append(json_data)
        else:
            print(json_data)
            place_details.append(json_data['status'])
        #place_details.append(pid)
    else:
        place_details.append('')

print(place_details)

df['place_details'] = place_details
df.to_csv('output/vet_detail.csv', encoding = 'utf8')

