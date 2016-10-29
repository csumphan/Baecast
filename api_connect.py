'''
Created on Apr 2, 2016

@author: EltonXue
'''
import urllib.request         # urllib.request.urlopen(url)
import urllib.parse           # urllib.parse.urlencode((parameter, value))
import json
from pprint import pprint

API_KEY = 'b54bc59cbcf16ec1c57ff19ecef6493d'
BASE_WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
TEST_ZIP_CODE = '92617'

# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}

def build_url_from_zip(zip_code: str, country = 'US') -> str:
    location = zip_code + ',' + country
    parameters = urllib.parse.urlencode([('zip', location), ('appid', API_KEY)])
    return BASE_WEATHER_URL + '?' + parameters

def get_response(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode(encoding = 'utf-8'))
    finally:
        if response != None:
            response.close()

# Test:
# pprint(get_response(build_url_from_zip(TEST_ZIP_CODE)))
    
    
    


