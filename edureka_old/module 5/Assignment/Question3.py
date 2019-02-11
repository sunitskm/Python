import os
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.isfile(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print 'Need to create schema'
    print 'Creating database'
else:
    print 'Database exists, assume schema does, too.'
conn.close()
