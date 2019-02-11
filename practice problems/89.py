import sqlite3
import pandas
conn = sqlite3.connect('database.db')
final_list = []
with conn:
    cur = conn.cursor()
    ar = 2000000
    cur.execute("SELECT * FROM COUNTRIES WHERE AREA>%d"%(ar))
    rows = cur.fetchall()
    for element in rows:
        print(element[1])
        final_list.append(element)
df = pandas.DataFrame(final_list,columns=["Rank","Country","Area","Population"])
df.to_csv('list_country.csv',index=False)
