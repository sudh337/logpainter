import json
import sqlite3
from counter import *
import googlemaps
import time
import sys


def getcoordinates(conn, cursor, loc_id):
    cur.execute('SELECT geo_id from Geodata where location_id = ?', (loc_id,))
    try:
        geo_id = cur.fetchone()[0]
        print "Data already exists for Location"
    except TypeError:
        cur.execute('SELECT latitude, longitude FROM Location where location_id = ?', (loc_id,))
        coordinates = cur.fetchone()
        return (coordinates,loc_id)  # we will return the result as a tuple and then use the same to input to geodata()


def getgeodata(gmaps, coordinates):
    #print "Waiting for 34.50 seconds so that google does't block us!"
    for t in xrange(10, 0, -1):
        time.sleep(1)
        sys.stdout.write(str(t) + '..')
        sys.stdout.flush()
    time.sleep(0.50)
    # time.sleep(34.50)
    try:
        rev_data = gmaps.reverse_geocode(coordinates)
        return rev_data
    except:
        return None


def getformattedaddress(rev_data):
    try:
        formatted_addr = rev_data[0]['formatted_address']
        return formatted_addr
    except:
        formatted_addr = ''
        print 'Could not retrieve formatted address'
        return formatted_addr


def getpincode(rev_data):
    try:
        pincode = rev_data[0]['address_components'][-1]['long_name']
        return pincode
    except:
        pincode = ''
        print 'Could not retrieve pincode'
        return pincode
