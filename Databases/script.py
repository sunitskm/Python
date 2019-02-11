import sqlite3
#Function to create a table if not already created
def create_table():
    #Create a connection object
    conn = sqlite3.connect("lite.db")
    #Curson object to point to the database
    cur=conn.cursor()
    #Execute the query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #Commit the changes
    conn.commit()
    conn.close()
#Function to insert data into the table
def insert(item,quantity,price):
        conn = sqlite3.connect("lite.db")
        #Curson object to point to the database
        cur=conn.cursor()
        #Execute the query
        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
        #Commit the changes
        conn.commit()
        conn.close()
#insert("RMA JERSEY",5,350)
#Funtion to view the contents of the database
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return(rows)
#Function to delete a specific item from the database
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE from store where item = ?",(item,))
    conn.commit()
    conn.close()
#Function to update a specific item with a specific quantity and price
def update(item, quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close
update('Football',9,20.0)
delete("RMA JERSEY")
print(view())
