import sqlite3
con = sqlite3.connect('new.db')
with con:
    cur = con.cursor()
    #cur.execute('DROP TABLE Friends;')
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    cur.execute("SELECT max(ID) from Friends;")
    data = cur.fetchone()
    print "The last Id of the inserted row is %d" %data
