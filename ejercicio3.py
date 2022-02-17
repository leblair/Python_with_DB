import sys
import psycopg2




try:
    conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()

    cur.execute("SELECT Id from taulatest")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    valid = False
    while not valid:
        option = input("De quin registre vols les dades?")
        if option.isdigit():
            inp = int(option)
            if inp>len(rows):
                print("no es una opcio valida")
            else:
                cur.execute("SELECT * from taulatest where id=%s", (option[-1]))
                field_rows = cur.fetchall()
                for i in field_rows:
                    print(i)
                valid = True
        else:
            print("no es un numero, entra un numero")




except (Exception, psycopg2.DatabaseError) as error:
    if conn is not None:
        conn.rollback()
        print(error)
        sys.exit(1)
finally:
    if conn is not None:
        conn.close()
