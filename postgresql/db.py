import psycopg2
import secrets
from psycopg2 import sql

try:
    conn = psycopg2.connect("dbname='postgres' user='pygres' host='localhost' password='%s'" % secrets.db_pass)
    cur = conn.cursor()
    cur.execute(
        sql.SQL("insert into {} values (%s, %s)")
            .format(sql.Identifier('fierce_followers')),
        [12345, 'hello'])
    cur.execute("select * from fierce_followers")
    rows=cur.fetchall()
    print rows
    conn.commit()
    cur.close()
except Exception as e:
    print e.message