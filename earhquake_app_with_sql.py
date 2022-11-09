import requests
import sqlite3


def save_earthquake(earthquake_list: list[str]) -> None:
   """
   Save data about earthquakes from list(json object)
   """
   conn = sqlite3.connect('earthquakes_db.db')
   cursor = conn.cursor()
   cursor.execute('CREATE TABLE earthquakes (place TEXT, magnitude REAL);')
   cursor.executemany('INSERT INTO earthquakes (place, magnitude) VALUES (?, ?)', earthquake_list)
   conn.commit()
   conn.close()


def print_earthquakes() -> None:
   '''
   Print in terminal data from created database
   '''
   conn = sqlite3.connect('earthquakes_db.db')
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM earthquakes;')
   data = cursor.fetchall()
   [print(row) for row in data]
   conn.commit()
   conn.close()


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'                           # api


starttime = input('Enter the start time YYYY-MM-DD: ')                              # api params
endtime = input('Enter the end time YYYY-MM-DD: ')
latitude = input('Enter the latitude: ')                    
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')


response = requests.get(url, headers={'Accept': 'application/json'}, params={       # get json object from api
   'format':'geojson',
   'starttime':starttime,
   'endtime':endtime,
   'latitude':latitude,
   'longitude':longitude,
   'maxradiuskm':maxradiuskm,
   'minmagnitude':minmagnitude
})


data = response.json()                                                              # get data from json object to list
earthquake_list = []
for i in range(len(data['features'])):
   place = data['features'][i]['properties']['place']
   mag = data['features'][i]['properties']['mag']
   earthquake_list.append((place, mag))


save_earthquake(earthquake_list)
print_earthquakes()