import psycopg2
#Function to create a table if not already created
def create_table():
    #Create a connection object
    conn = psycopg2.connect("dbname= 'database1' user='postgres' password = 'postgres1234' host = 'localhost' port = '5432'")
    #Curson object to point to the database
    cur=conn.cursor()
    #Execute the query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #Commit the changes
    conn.commit()
    conn.close()
#Function to insert data into the table
def insert(item,quantity,price):
        conn = psycopg2.connect("dbname= 'database1' user='postgres' password = 'postgres1234' host = 'localhost' port = '5432'")
        #Curson object to point to the database
        cur=conn.cursor()
        #Execute the query
        #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price))
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
        #Commit the changes
        conn.commit()
        conn.close()
#insert("RMA JERSEY",5,350)
#insert("Soccer shoes",7,700)
#Funtion to view the contents of the database
def view():
    conn = psycopg2.connect("dbname= 'database1' user='postgres' password = 'postgres1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return(rows)
#Function to delete a specific item from the database
def delete(item):
    conn = psycopg2.connect("dbname= 'database1' user='postgres' password = 'postgres1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE from store where item = %s",(item,))
    conn.commit()
    conn.close()
#Function to update a specific item with a specific quantity and price
def update(item, quantity,price):
    conn = psycopg2.connect("dbname= 'database1' user='postgres' password = 'postgres1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity,price,item))
    conn.commit()
    conn.close
create_table()
update('RMA JERSEY',9,500)
#delete("Soccer shoes")
print(view())
