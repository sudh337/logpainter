import sqlite3

conn = sqlite3.connect('logPainter_v5.sqlite')
cur = conn.cursor()


def countEntries(tableName):
    q = 'SELECT COUNT(*) FROM '+str(tableName)+''
    cur.execute(q)
    try:
        print "\n******************************************"
        return cur.fetchone()[0]
    except sqlite3.OperationalError:
        print "Table not present!"
        return None

