import psycopg2
from .. import secrets
from psycopg2 import sql


class PostgresDB:

    default_dbname = "postgres"
    default_user = "pygres"
    default_host = "localhost"

    def __init__(self):
        self.conn = self.open(pw=secrets.db_pass)

    def executeSql(self, command):
        cur = self.conn.cursor()
        cur.execute(command)
        result = cur.statusmessage
        conn.commit() #update data
        cur.close()
        return result

    #open a connection to PostgreSQL DB
    @staticmethod
    def open(dbname=default_dbname, user=default_user, host=default_host, pw=None):
        return psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (dbname, user, host, pw))

    def __del__(self):
        self.conn.close()


try:
    conn = PostgresDB.open(pw=secrets.db_pass)
    cur = conn.cursor()
    cur.execute(
        sql.SQL("insert into {} values (%s, %s)").format(sql.Identifier('fierce_followers')), [12345, 'hello'])
    cur.execute("select * from fierce_followers")
    rows = cur.fetchall()
    print rows
    conn.commit()
    cur.close()
except Exception as e:
    print e.message


