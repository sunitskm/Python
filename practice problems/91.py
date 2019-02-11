import sqlite3
import pandas as pd

df1  = pd.read_csv('ten-more-countries.txt')
print(type(df1))
print(df1.iterrows())
rows = df1.iterrows()

conn = sqlite3.connect('database.db')
cur = conn.cursor()
for row in rows:
    print(row[1]['Country'])
    country = row[1]['Country']
    print(row[1]['Area'])
    area = row[1]['Area']
    sql = "INSERT INTO countries VALUES(NULL,?,?,NULL)",(country,area)
    cur.execute("INSERT INTO countries VALUES(NULL,?,?,NULL)",(country,area))
conn.commit()
conn.close()
conn = sqlite3.connect('database.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM COUNTRIES")
    rows = cur.fetchall()
    for element in rows:
        print(element)
