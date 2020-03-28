#!/usr/bin/python3
"""script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, write one
that is safe from MySQL injections!"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT id, name FROM states \
        WHERE name = %s ORDER BY id;""", (sys.argv[4],))
    rows = curs.fetchall()
    for r in rows:
        print(r)
    curs.close()
    db.close()
