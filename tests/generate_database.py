import os
import os.path
import pandas as pd
import sqlite3


def verify_database():
    dl_fname = '../pywords/data/DICTLINE.tsv'
    infl_fname = '../pywords/data/INFLECTS.tsv'

    db_fname = 'words.db'
    if not os.path.exists(db_fname):
        # Generate database tables
        db_conn = sqlite3.connect(db_fname)
        dictline_data = pd.read_csv(dl_fname,delimiter='\t')
        inflects_data = pd.read_csv(infl_fname,delimiter='\t')

        dictline_data.to_sql('dictline',db_conn, if_exists='replace', index=False)
        inflects_data.to_sql('inflects',db_conn, if_exists='replace', index=False)
        db_conn.close()
        print("Database written to {0}".format(os.getcwd()+'/'+db_fname))
    else:
        print("Database {0} already exists.".format(os.getcwd()+'/'+db_fname))



