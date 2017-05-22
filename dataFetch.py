import requests
import json

singleUrl = 'http://ip-api.com/json/'
batchUrl = 'http://ip-api.com/batch'


def getInfo(ip):
    finalUrl = singleUrl + ip
    r = requests.get(finalUrl)
    try:
        data = json.loads(r.content)
        return data
    except:
        print "Failure to retrieve data!"
        return None


def infoCity(data):
    try:
        city = data['city']
        return city
    except KeyError:
        return None


def infoZip(data):
    try:
        zip = data['zip']
        return zip
    except:
        return None


def infoCountryCode(data):
    try:
        countryCode = data['countryCode']
        return countryCode
    except:
        return None


def infoCountry(data):
    try:
        country = data['country']
        return country
    except:
        return None


def infoRegionCode(data):
    try:
        regionCode = data['region']
    except:
        return None


def infoIsp(data):
    try:
        isp = data['isp']
        return isp
    except:
        return None


def infoLon(data):
    try:
        lon = data['lon']
        return lon
    except:
        return None


def infoTimeZone(data):
    try:
        timezone = data['timezone']
        return timezone
    except:
        return None


def infoAsNo(data):
    try:
        as_no = data['as']
        return as_no
    except:
        return None


def infoQuery(data):
    try:
        query = data['query']
        return query
    except:
        return None


def infoLat(data):
    try:
        lat = data['lat']
        return lat
    except:
        return None


def infoOrg(data):
    try:
        org = data['org']
        return org
    except:
        return None


def infoRegionName(data):
    try:
        regionName = data['regionName']
        return regionName
    except:
        return None
