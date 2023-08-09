import requests
from moebiustech.settings import REVERSE_GEOCODING_KEY

def get_location_from_coordinates(lat, lng, api_key):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={REVERSE_GEOCODING_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        results = data['results']
        if results:
            location_info = results[0]['formatted_address']
            return location_info
    return None