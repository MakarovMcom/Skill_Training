token = '...'

# Python 3
import http.client, urllib.parse
import pandas as pd
import time
import json

def geocoding(string):
    conn = http.client.HTTPConnection('api.positionstack.com')
    params = urllib.parse.urlencode({
        'access_key': 'a178b45604719b5757c6c1cdaf0791a9',
        'query': string,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))
    res = conn.getresponse()
    data = json.load(res)
    return data


df = pd.read_csv('C:/Users/.../Desktop/espoo_rental_withoutbuildings.csv', encoding='utf8')
print(df['address'].head())

latitude = []
longitude = []
for i in df['address']:
    try:
        la = geocoding(i)['data'][0]['latitude']
        lo = geocoding(i)['data'][0]['longitude']
        latitude.append(la)
        longitude.append(lo)
        print(i, la, lo)
    except Exception as e:
        la = ''
        lo = ''
        latitude.append(la)
        longitude.append(lo)
        print(i, la, lo)
    time.sleep(1)

geo_data = pd.DataFrame()
geo_data['address'] = df['address']
geo_data['latitude'] = latitude
geo_data['longitude'] = longitude
print(geo_data.head())

geo_data.to_csv('geo_data.csv',encoding = 'utf-8',header=['address','latitude', 'longitude'])