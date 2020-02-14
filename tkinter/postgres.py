import psycopg2



def createTable():
    con = psycopg2.connect("dbname='db1' user='postgres' password='603Concord' host='localhost' port='5432' ")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantit INTEGER, price REAL)")
    
    con.commit()
    con.close()

def insert(item, quant, price):
    con = psycopg2.connect("dbname='db1' user='postgres' password='603Concord' host='localhost' port='5432' ")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quant, price))
    con.commit()
    con.close()


def veiw():
    con = psycopg2.connect("dbname='db1' user='postgres' password='603Concord' host='localhost' port='5432' ")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect("dbname='db1' user='postgres' password='603Concord' host='localhost' port='5432' ")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    con.commit()
    con.close()


def update(quantity, price, item):
    con = psycopg2.connect("dbname='db1' user='postgres' password='603Concord' host='localhost' port='5432' ")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantit=%s, price=%s WHERE item=%s",(quantity, price, item))
    con.commit()
    con.close()


update(20,11,"Wine glass")
print(veiw())