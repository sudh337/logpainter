import sqlite3


def updateIPinfo(conn, cursor, ip_id, loc_id, isp_id, as_id, org_id, port_id):
    cursor.execute('INSERT INTO IPinfo(ip_id, loc_id, isp_id, as_id, org_id, port_id) VALUES(?, ?, ?, ?, ?, ?)',
                   (ip_id, loc_id, isp_id, as_id, org_id, port_id))
    conn.commit()
    print 'IPInfo Table updated!'


def updateASnumber(conn, cursor, as_no, isp_id):
    cursor.execute('SELECT as_id from ASnumber where as_no=?', (as_no,))
    try:
        as_id = cursor.fetchone()[0]
        print "AS Number Found in DB "# + str(as_no)
        return as_id
    except TypeError:
        cursor.execute('INSERT INTO Asnumber(as_no, isp_id) VALUES(?, ?)', (as_no, isp_id))
        conn.commit()
        print "ASnumber Table Updated "# + str(as_no)
        as_id = cursor.lastrowid
        return as_id


def updateLocation(conn, cursor, lat, lon, zip, country_id, region_id, city_id):
    cursor.execute(
        'INSERT INTO Location(latitude, longitude, zip_code, country_id, region_id, city_id) VALUES(?, ?, ?, ?, ?, ?)',
        (lat, lon, zip, country_id, region_id, city_id))
    loc_id = cursor.lastrowid
    conn.commit()
    print "Location Table Updated!"
    return loc_id


def updateOrganization(conn, cursor, name):
    cursor.execute('SELECT org_id FROM Organization where name=?', (name,))
    try:
        org_id = cursor.fetchone()[0]
        print "Organization Found in DB "# + str(name)
        return org_id
    except TypeError:
        cursor.execute('INSERT INTO Organization(name) VALUES(?)', (name,))
        org_id = cursor.lastrowid
        conn.commit()
        print "Organization Table Updated "# + str(name)
        return org_id


def updateCountry(conn, cursor, name, countryCode):
    cursor.execute('SELECT country_id FROM Country where name=?', (name,))
    try:
        country_id = cursor.fetchone()[0]
        print "Country Found in DB : "# + str(name)
        return country_id
    except TypeError:
        cursor.execute('INSERT INTO Country(name, country_code) VALUES(?, ?)', (name, countryCode))
        conn.commit()
        print "Country Table Updated "# + str(name)
        return cursor.lastrowid


def updateCity(conn, cursor, name):
    cursor.execute('SELECT city_id FROM City where name=?', (name,))
    try:
        city_id = cursor.fetchone()[0]
        print "City Found in DB "# + str(name)
        return city_id
    except TypeError:
        cursor.execute('INSERT INTO City(name) VALUES(?)', (name,))
        conn.commit()
        print "City Table Updated "# + str(name)
        return cursor.lastrowid


def updateRegion(conn, cursor, name, regionCode):
    cursor.execute('SELECT region_id FROM Region where name=?', (name,))
    try:
        region_id = cursor.fetchone()[0]
        print "Region Found in DB "# + str(name)
        return region_id
    except TypeError:
        cursor.execute('INSERT INTO Region(name, region_code) VALUES(?, ?)', (name, regionCode))
        conn.commit()
        print 'Region Table updated '# + str(name)
        return cursor.lastrowid


def updateProtocol(conn, cursor, protocol):
    cursor.execute('SELECT protocol_id from Protocol where name=?', (protocol,))
    try:
        protocol_id = cursor.fetchone()[0]
        print "Protocol found in database " + str(protocol)
        return protocol_id
    except TypeError:
        cursor.execute('INSERT INTO Protocol(name) VALUES(?)', (protocol,))
        protocol_id = cursor.lastrowid
        conn.commit()
        print 'Protocol Table updated with ' + str(protocol)
        return protocol_id


def updatePorts(conn, cursor, port_no, protocol_id):
    cursor.execute('SELECT port_id from Ports where number=?', (port_no,))
    try:
        port_id = cursor.fetchone()[0]
        print "Port found in database " + str(port_no)
        return port_id
    except TypeError:
        cursor.execute('INSERT INTO Ports (number, protocol_id) VALUES (?, ?)', (port_no, protocol_id))
        port_id = cursor.lastrowid
        conn.commit()
        print 'Ports Table updated with ' + str(port_no)
        return port_id


def updateIsp(conn, cursor, name):
    cursor.execute('SELECT isp_id from Isp where name=?', (name,))
    try:
        isp_id = cursor.fetchone()[0]
        print "ISP found in database "# + str(name)
        return isp_id
    except TypeError:
        cursor.execute('INSERT INTO Isp (name) VALUES(?)', (name,))
        isp_id = cursor.lastrowid
        conn.commit()
        print "ISP Table Updated "# + str(name)
        return isp_id


# def getServiceId (cursor, port, protocol_id):
#     return 0

def updateIPadd(conn, cursor, ip, ts):
    cursor.execute('SELECT ip_id from IPadd where ip=?', (ip,))
    try:
        ip_id = cursor.fetchone()[0]
        print "IP found in database " + str(ip)
        return ip_id
    except TypeError:
        cursor.execute('INSERT INTO IPadd(ip, ts) VALUES(?, ?)', (ip, ts))
        ip_id = cursor.lastrowid
        conn.commit()
        print 'IPadd Table updated with ' + str(ip)
        return ip_id
