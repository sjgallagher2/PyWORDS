import sqlite3

db_fname = "data/database/words.db"

# Create a connector to the database
db_conn = sqlite3.connect(db_fname)

# Create a cursor for executing sql
db_cursor = db_conn.cursor()

# Now we can query
db_cursor.execute("""SELECT dictline.dl_stem1_uvij,inflections.infl_ending_uvij 
FROM dictline
JOIN inflections ON dictline.dl_type = inflections.infl_type 
    AND dictline.dl_variant = inflections.infl_variant
    AND dictline.dl_pos = inflections.infl_pos
WHERE dictline.dl_pos IS 'N' AND dictline.dl_stem1_uvij GLOB 'acro*'
    AND inflections.infl_stem_id IS 1 AND inflections.infl_frequency IS 'A'
;
""")

rows = db_cursor.fetchall()
for row in rows:
    print(row)

