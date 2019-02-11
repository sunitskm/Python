import csv
import sqlite3

# Create the database
conn = sqlite3.connect('pricelist.db')
cur = conn.cursor()

# Create the table
cur.execute('DROP TABLE IF EXISTS prices')
cur.execute('CREATE TABLE  prices ( Gain REAL, Loss REAL, Phone_Number text, Address text) ')
conn.commit()

# Load the CSV file into CSV reader
csvfile = open('sample-storedata.csv', 'rb')
creader = csv.reader(csvfile, delimiter=',', quotechar='|')

# Iterate through the CSV reader, inserting values into the database
for t in creader:
    #rint(t)
    to_db = [unicode(t[0], "utf8"), unicode(t[1], "utf8"), unicode(t[2], "utf8"), unicode(t[3]+","+t[4], "utf8")]
    cur.execute('INSERT INTO  prices VALUES (?,?,?,?)', to_db )
cur.execute('SELECT * FROM prices')
rows = cur.fetchall()
print
for row in rows:
    print "%2s %-10s %s %s" % row
col_names = [cn[0] for cn in cur.description]
print "%s %s %s %s " % (col_names[0], col_names[1], col_names[2],col_names[3])
# Close the csv file, commit changes, and close the connection
csvfile.close()
conn.close()
