import sqlite3


def createTable():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantit INTEGER, price REAL)")
    
    con.commit()
    con.close()

def insert(item, quant, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quant,price))
    con.commit()
    con.close()


def veiw():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()


def update(quantity, price, item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantit=?, price=? WHERE item=?",(quantity, price, item))
    con.commit()
    con.close()

update(40,7.5,"Beer")
print(veiw())