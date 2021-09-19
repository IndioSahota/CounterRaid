import requests
import urllib.request


def get_location():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    response = requests.get("http://ip-api.com/json/" + external_ip).json()
    location = {'city': response['city'],
                'region': response['region'],
                'country': response['country'],
                'lat': response['lat'],
                'lon': response['lon'],
                'isp': response['isp'],
                'query': response['query']}
    return location



