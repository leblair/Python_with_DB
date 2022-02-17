import psycopg2

try:
    conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()
    cur.execute("SELECT * from res_users where id>%s", (1,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()



