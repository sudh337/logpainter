import json
import sqlite3
import re
import time
from parsingFunctions import *
from updateEntry import *
from dataFetch import *
from lookup import *

logFile = open('dlinkrouter.log', 'r')
#
conn = sqlite3.connect('logPainter_v5.sqlite')
cur = conn.cursor()

cur.executescript('''

        CREATE TABLE IF NOT EXISTS IPinfo (
        ip_id integer,
        loc_id integer,
        isp_id integer,
        as_id integer,
        org_id integer,
        port_id integer
    );

    CREATE TABLE IF NOT EXISTS ASnumber (
        as_id integer PRIMARY KEY AUTOINCREMENT,
        as_no varchar,
        isp_id integer
    );

    CREATE TABLE IF NOT EXISTS Location (
        location_id integer PRIMARY KEY AUTOINCREMENT,
        latitude float,
        longitude float,
        zip_code text,
        address varchar,
        country_id integer,
        region_id integer,
        city_id integer
    );

    CREATE TABLE IF NOT EXISTS Organization (
        org_id integer PRIMARY KEY AUTOINCREMENT,
        name text
    );

    CREATE TABLE IF NOT EXISTS Country (
        country_id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        country_code text
    );

    CREATE TABLE IF NOT EXISTS City (
        city_id integer PRIMARY KEY AUTOINCREMENT,
        name text
    );

    CREATE TABLE IF NOT EXISTS Region (
        region_id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        region_code text
    );

    CREATE TABLE IF NOT EXISTS Protocol (
        protocol_id integer PRIMARY KEY AUTOINCREMENT,
        name text
    );

    CREATE TABLE IF NOT EXISTS Ports (
        port_id integer PRIMARY KEY AUTOINCREMENT,
        number integer,
        service text,
        service_id integer,
        protocol_id integer
    );

    CREATE TABLE IF NOT EXISTS Isp (
        isp_id integer PRIMARY KEY AUTOINCREMENT,
        name text
    );

    CREATE TABLE IF NOT EXISTS IPadd (
        ip_id integer PRIMARY KEY AUTOINCREMENT,
        ip text,
        ts datetime
    );

''')

conn.commit()
print "Database Created!"

fh = logFile.readlines()
print "Total lines to parse : %s" % len(fh)
total_lines = 1
start = time.time()

for line in fh:
    # print str(logParserIP(line))+":"+str(logParserProtocol(line))+":"+str(logParserPort(line))+ "\t" + str(logParserDT(line))
    total_lines += 1
    ip = logParserIP(line)
    if ip is None:
        continue
    else:
        searchIP = ipLookup(conn, cur, ip)

        if searchIP[0] == 0:
            data_ip = getInfo(ip)

            protocol = logParserProtocol(line)
            try:
                protocol = protocol.lower()
            except AttributeError:
                pass
            protocol_id = updateProtocol(conn, cur, protocol)

            port_no = logParserPort(line)
            port_id = updatePorts(conn, cur, port_no, protocol_id)

            ts = logParserDT(line)
            ip_id = updateIPadd(conn, cur, ip, ts)

            city = infoCity(data_ip)
            try:
                city = city.lower()
            except AttributeError:
                pass
            city_id = updateCity(conn, cur, city)

            regionCode = infoRegionCode(data_ip)
            try:
                regionCode = regionCode.lower()
            except AttributeError:
                pass
            regionName = infoRegionName(data_ip)
            try:
                regionName = regionName.lower()
            except AttributeError:
                pass
            region_id = updateRegion(conn, cur, regionName, regionCode)

            country = infoCountry(data_ip)
            try:
                country = country.lower()
            except AttributeError:
                pass
            countryCode = infoCountryCode(data_ip)
            try:
                countryCode = countryCode.lower()
            except AttributeError:
                pass
            country_id = updateCountry(conn, cur, country, countryCode)

            lat = infoLat(data_ip)
            lon = infoLon(data_ip)
            zip = infoZip(data_ip)
            loc_id = updateLocation(conn, cur, lat, lon, zip, country_id, region_id, city_id)

            isp = infoIsp(data_ip)
            try:
                isp = isp.lower()
            except AttributeError:
                pass
            isp_id = updateIsp(conn, cur, isp)

            as_no = infoAsNo(data_ip)
            as_id = updateASnumber(conn, cur, as_no, isp_id)

            org = infoOrg(data_ip)
            try:
                org = org.lower()
            except AttributeError:
                pass
            org_id = updateOrganization(conn, cur, org)

            updateIPinfo(conn, cur, ip_id, loc_id, isp_id, as_id, org_id, port_id)
            total_lines += 1
            time.sleep(1)
        else:
            ip_id = searchIP[1]
            ipData = ipInfoLookup(conn, cur, ip_id)
            loc_id = ipData[0]
            isp_id = ipData[1]
            as_id = ipData[2]
            org_id = ipData[3]

            protocol = logParserProtocol(line)
            try:
                protocol = protocol.lower()
            except AttributeError:
                pass
            searchProtocol = protocolLookup(conn, cur, protocol)
            if searchProtocol[0] == 0:
                protocol_id = updateProtocol(conn, cur, protocol)
            else:
                protocol_id = searchProtocol[1]

            port_no = logParserPort(line)
            searchPort = portLookup(conn, cur, port_no)
            if searchPort[0] == 0:
                port_id = updatePorts(conn, cur, port_no, protocol_id)
            else:
                port_id = searchPort[1]

            updateIPinfo(conn, cur, ip_id, loc_id, isp_id, as_id, org_id, port_id)
            total_lines += 1
            #time.sleep(1)

print "\nTotal number of lines parsed :" + str(total_lines)
# print "Total attackers : " + str(len(att_ips))
# print "Total ports targeted : " + str(len(ports_t) + len(ports_u))
end = time.time()
elapsed = end - start
print "Time elapsed : " + str(elapsed)
