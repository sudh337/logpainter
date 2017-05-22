import sqlite3


def ipLookup(conn, cursor, ip):
    cursor.execute('SELECT ip_id from IPadd where ip=?', (ip,))
    try:
        ip_id = cursor.fetchone()[0]
        print "IP found in database " + str(ip)
        search = 1
        result = [search, ip_id]
        return result
    except TypeError:
        print "IP not found in database "
        # cursor.execute('INSERT INTO IPadd(ip, ts) VALUES(?, ?)', (ip, ts))
        # ip_id = cursor.lastrowid
        # conn.commit()
        # print 'IPadd Table updated with ' + str(ip)
        search = 0
        ip_id = 0
        result = [search, ip_id]
        return result


def ipInfoLookup(conn, cursor, ip_id):
    cursor.execute('SELECT loc_id, isp_id, as_id, org_id from IPinfo where ip_id=?', (ip_id,))
    data = cursor.fetchone()
    return data


def portLookup(conn, cursor, port_no):
    cursor.execute('SELECT port_id from Ports where number=?', (port_no,))
    try:
        port_id = cursor.fetchone()[0]
        print "Port found in database " + str(port_no)
        search = 1
        result = [search, port_id]
        return result
    except TypeError:
        print "Port not found in database "
        # cursor.execute('INSERT INTO IPadd(ip, ts) VALUES(?, ?)', (ip, ts))
        # ip_id = cursor.lastrowid
        # conn.commit()
        # print 'IPadd Table updated with ' + str(ip)
        search = 0
        port_id = 0
        result = [search, port_id]
        return result


def protocolLookup(conn, cursor, protocol):
    cursor.execute('SELECT protocol_id from Protocol where name=?', (protocol,))
    try:
        protocol_id = cursor.fetchone()[0]
        print "Protocol found in database " + str(protocol)
        search = 1
        result = [search, protocol_id]
        return result
    except TypeError:
        print "Protocol not found in database"
        # cursor.execute('INSERT INTO IPadd(ip, ts) VALUES(?, ?)', (ip, ts))
        # ip_id = cursor.lastrowid
        # conn.commit()
        # print 'IPadd Table updated with ' + str(ip)
        search = 0
        protocol_id = 0
        result = [search, protocol_id]
        return result
