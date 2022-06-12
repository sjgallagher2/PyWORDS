import sqlite3

db_fname = "data/database/words.db"
db_conn = sqlite3.connect(db_fname)
db_cursor = db_conn.cursor()

def get_stemN_endings(cursor,stem,stemN):
    """
    Get endings available for dl_stemN (N=1,2,3,4) for word stem `stem`
    """
    if stemN not in [1,2,3,4]:
        raise ValueError("Stem must be one of: 1,2,3,4")
    #db_cursor.execute("""SELECT *
    cursor.execute("""SELECT dictline.dl_id,dictline.dl_stem{0}_uvij,inflections.infl_id,inflections.infl_ending_uvij 
    FROM dictline
    JOIN inflections ON dictline.dl_type = inflections.infl_type 
        AND dictline.dl_variant = inflections.infl_variant
        AND dictline.dl_pos = inflections.infl_pos
    WHERE dictline.dl_stem{0}_vi = '{1}' 
        AND inflections.infl_stem_id IS {0} AND inflections.infl_frequency IS 'A'
    ;
    """.format(stemN,stem.replace('u','v').replace('j','i')))
    stem_rows = cursor.fetchall()
    return stem_rows


def get_possible_endings(cursor,stem):
    stem1_endings = get_stemN_endings(cursor,stem,1)
    stem2_endings = get_stemN_endings(cursor,stem,2)
    stem3_endings = get_stemN_endings(cursor,stem,3)
    stem4_endings = get_stemN_endings(cursor,stem,4)
    stem_endings = stem1_endings + stem2_endings + stem3_endings + stem4_endings
    #for row in stem_endings:
    #    print(row)
    return stem_endings

#for i in range(1000):
#    get_possible_endings(db_cursor,"cael")

