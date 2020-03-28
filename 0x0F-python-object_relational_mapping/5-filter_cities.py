#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute(
        """SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY id;""", (sys.argv[4],))
    rows = curs.fetchall()
    print(", ".join([row[0] for row in rows]))
    curs.close()
    db.close()
