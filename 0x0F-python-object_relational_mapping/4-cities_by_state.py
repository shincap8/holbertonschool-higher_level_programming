#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute(
        "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY id;")
    rows = curs.fetchall()
    for r in rows:
        print(r)
    curs.close()
    db.close()
