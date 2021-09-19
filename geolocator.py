import requests
import urllib.request

def get_location():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    response = requests.get("http://ip-api.com/json/" + external_ip).json()
    location = {'city': response['city'],
                'region': response['region'],
                'country': response['country'],
                'latitude': response['lat'],
                'longitude': response['lon'],
                'isp': response['isp'],
                'ip_address': response['query']}
    return location

print(get_location())

