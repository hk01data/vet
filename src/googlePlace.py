import requests
import json
import pandas as pd


df = pd.read_csv('vet.csv', encoding = 'utf8')
df = df[111:]
URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
API_KEY = 'AIzaSyAo1IdMwXkSVsDc3-ZVrzdj9iDRFXO4wFs'

place_id = []
for idx, name in enumerate(df['獸醫診所名稱']):
    print('{} {}'.format(idx+1, name))

    param = {
        'input': name,
        'inputtype': 'textquery',
        'fields':'',
        'key': API_KEY
    }
    r = requests.get(URL, params = param)

    json_data = json.loads(r.text)
    print(json_data)
    if json_data['status'] == 'OK':
        print(json_data['candidates'][0])
        place_id.append(json_data['candidates'][0]['place_id'])
    else:
        print(json_data['status'])
        place_id.append(json_data['status'])

print(place_id)

df['place_id'] = place_id
df.to_csv('vet_id.csv', encoding = 'utf8')


