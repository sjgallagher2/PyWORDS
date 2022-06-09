import sqlite3

db_fname = "data/database/words.db"

# Create a connector to the database
db_conn = sqlite3.connect(db_fname)

# Create a cursor for executing sql
db_cursor = db_conn.cursor()

# Now we can query

