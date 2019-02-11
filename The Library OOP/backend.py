import sqlite3

class Database:
    def __init__(self,):
        #Create a connection object
        self.conn = sqlite3.connect("books.db")
        #Curson object to point to the database
        self.cur=self.conn.cursor()
        #Execute the query
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        #Commit the changes
        self.conn.commit()

    #create_table()
    def add_entry(self,title,author,year=2000,isbn=0):
        self.cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view_all(self,):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return (rows)

    def search_entry(self,title = "",author = "",year = "",isbn = ""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return (rows)

    def delete_entry(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.conn.commit()

    def update_entry(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title = ?,author = ?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



    #add_entry("Shiva Trilogy","Amit Shukla")
    #add_entry("Alice in wonderland","Lewis Carol",1941,42321132)
    #delete_entry(4)
    #update_entry(5,"Shiva Trilogy","Amit Trivedi", 2013,5543678)
    #print(view_all())
    #print(search_entry(author = "Amit Trivedi"))
