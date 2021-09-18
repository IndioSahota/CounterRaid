import requests
import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
response = requests.get("http://ip-api.com/json/" + external_ip).json()
print(response)
location = {'City': response['city'],
            'Region': response['region'],
            'Country': response['country'],
            'Latitude': response['lat'],
            'Longitude': response['lon']
}
