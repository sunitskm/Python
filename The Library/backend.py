import sqlite3
def create_table():
    #Create a connection object
    conn = sqlite3.connect("books.db")
    #Curson object to point to the database
    cur=conn.cursor()
    #Execute the query
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    #Commit the changes
    conn.commit()
    conn.close()
create_table()
def add_entry(title,author,year=2000,isbn=0):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return (rows)

def search_entry(title = "",author = "",year = "",isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return (rows)

def delete_entry(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update_entry(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?,author = ?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


#add_entry("Shiva Trilogy","Amit Shukla")
#add_entry("Alice in wonderland","Lewis Carol",1941,42321132)
#delete_entry(4)
#update_entry(5,"Shiva Trilogy","Amit Trivedi", 2013,5543678)
#print(view_all())
#print(search_entry(author = "Amit Trivedi"))
