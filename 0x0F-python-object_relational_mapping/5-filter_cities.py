#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute(
        """SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY id;""", (sys.argv[4],))
    rows = curs.fetchall()
    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0])
    curs.close()
    db.close()
