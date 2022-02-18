import psycopg2


def data_input(text):
    while True:
        option = input(text)
        if option.isdigit():
            inp = int(option)
            if inp > len(rows):
                print("no es una opcio valida")
            else:
                return option
        else:
            print("no es un numero, entra un numero")
try:
    #Exercici 1
    conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()
    print("Exercici 1:")
    cur.execute("SELECT * from res_users where id>%s", (1,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    #Exercici 2
    print("Exercici 2:")
    cur.execute("DROP TABLE IF EXISTS taulatest")
    cur.execute("CREATE TABLE taulatest(Id int PRIMARY KEY, data VARCHAR(10))")

    cur.execute("INSERT INTO taulatest VALUES (1,'padata1')")
    cur.execute("INSERT INTO taulatest VALUES (2,'padata2')")
    cur.execute("INSERT INTO taulatest VALUES (3,'padata3')")
    cur.execute("INSERT INTO taulatest VALUES (4,'padata4')")
    cur.execute("INSERT INTO taulatest VALUES (5,'padata5')")
    conn.commit()
    #Exercici 3
    print("Exercici 3:")
    cur.execute("SELECT Id from taulatest")
    rows2 = cur.fetchall()
    for i in rows2:
        print(i)
    var = data_input("De quin registre vols les dades?")
    cur.execute("SELECT * from taulatest where id=%s", (var[-1]))
    field_rows = cur.fetchall()
    for i in field_rows:
        print(i)
    #Exercici 4
    print("Exercici 4:")
    cur.execute("SELECT Id from taulatest")
    rows2 = cur.fetchall()
    for i in rows2:
        print(i)
    # opcion escogida
    var2 = data_input("De quin registre vols actualitzar les dades?")

    text = input("Escriu la nova dada: ")
    cur.execute("UPDATE taulatest set data=%s where Id=%s", (text, var2))
    conn.commit()
    print("Files modificades: {0}".format(cur.rowcount))
    cur.execute("SELECT * from taulatest where id=%s", (var2[-1]))
    field_rows2 = cur.fetchall()
    for i in field_rows2:
        print(i)


except (Exception, psycopg2.DatabaseError) as error:
    if conn is not None:
        conn.rollback()
        print(error)
        sys.exit(1)
finally:
    if conn is not None:
        conn.close()
