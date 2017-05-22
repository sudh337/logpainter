import googlemaps
import json
import sqlite3
from credentials import *
from updateEntry import updateGeodata
from fetchGeoData import *


conn = sqlite3.connect('logPainter_v5.sqlite')
cur = conn.cursor()
gmaps = googlemaps.Client(geo_coding_api_key)

cur.executescript('''

       CREATE TABLE IF NOT EXISTS Geodata (
        geo_id integer PRIMARY KEY AUTOINCREMENT,
        formatted_address text,
        pincode text,
        fulldata blob,
        location_id integer
);

''')

cur.execute('SELECT COUNT(*) FROM Location')
count = cur.fetchone()[0]
#count = countEntries('Location')

for id in range (1, count+1):
    location_info = getcoordinates(conn, cur, id)
    coordinates = location_info[0]
    rev_data = getgeodata(gmaps, coordinates)
    formatted_address = getformattedaddress(rev_data)
    pincode = getpincode(rev_data)
    fulldata = str(rev_data)
    geo_id = updateGeodata(conn, cur, formatted_address, pincode, fulldata, id)
    print "Entry updated in database at geo_id #" + str(geo_id)

print "Total Entries Updated is #" + str(count)