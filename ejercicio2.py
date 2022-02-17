import sys

import psycopg2

try:
    conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()
    #cur.execute("SELECT * from res_users where id>%s", (1,))
    cur.execute("DROP TABLE IF EXISTS taulatest")
    cur.execute("CREATE TABLE taulatest(Id int PRIMARY KEY, data VARCHAR(10))")

    cur.execute("INSERT INTO taulatest VALUES (1,'padata1')")
    cur.execute("INSERT INTO taulatest VALUES (2,'padata2')")
    cur.execute("INSERT INTO taulatest VALUES (3,'padata3')")
    cur.execute("INSERT INTO taulatest VALUES (4,'padata4')")
    cur.execute("INSERT INTO taulatest VALUES (5,'padata5')")
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    if conn is not None:
        conn.rollback()
        print(error)
        sys.exit(1)
finally:
    if conn is not None:
        conn.close()