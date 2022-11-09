import requests


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'                        # api url


starttime = input('Enter the start time: ')                                      # params for request
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')


response = requests.get(url, headers={'Accept': 'application/json'}, params={    # request for api
   'format':'geojson',
   'starttime':starttime,
   'endtime':endtime,
   'latitude':latitude,
   'longitude':longitude,
   'maxradiuskm':maxradiuskm,
   'minmagnitude':minmagnitude
})


data = response.json()                                                           # getting from json needed info
for i in range(len(data['features'])):
    place = data['features'][i]['properties']['place']
    magnitude = data['features'][i]['properties']['mag']
    print(f'{i + 1}. Place: {place}. Magnitude: {magnitude}')