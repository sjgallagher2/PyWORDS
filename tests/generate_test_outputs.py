import sqlite3
import pywords.lookup as lookup
from generate_database import verify_database

# This file finds (hopefully) accurate test outputs by querying the database
# and returning results. This is slower than loading everything in, but less
# prone to logic errors.

# Random selection of nouns from every declension/variant pair
noun_list = ['aqua' ,'aquae' ,'epitome' ,'epitomes' ,'cometes' ,'cometae' ,'Archias' ,'Archiae' ,'amicus' ,'amici' ,'verbum',
             'verbi' ,'puer' ,'pueri' ,'ager' ,'agri' ,'radius' ,'radii' ,'atrium' ,'atrii' ,'atri' ,'filius' ,'fili' ,'Lucius',
             'Lucii' ,'barbitos' ,'barbiti' ,'Androgeos' ,'Androgeo' ,'amphibrachys' ,'amphibrachyos' ,'chelys' ,'Ilion',
             'Ilii' ,'Panthus' ,'Panthi' ,'miles' ,'militis' ,'frater' ,'fratris' ,'soror' ,'sororis' ,'pulchritudo',
             'pulchritudinis' ,'legio' ,'legionis' ,'varietas' ,'varietatis' ,'radix' ,'radicis' ,'nomen' ,'nominis' ,'iter',
             'itineris' ,'tempus' ,'temporis' ,'hostis' ,'finis' ,'urbs' ,'urbis' ,'mons' ,'montis' ,'mare' ,'maris' ,'animal',
             'animalis' ,'exemplar' ,'exemplaris' ,'aer' ,'aeris' ,'lampas' ,'lampados' ,'Moses' ,'Mosis' ,'Ulixes' ,'Ulixis',
             'Ulixi' ,'Ulixei' ,'Achilles' ,'Achillis' ,'tigris' ,'tigridis' ,'praxis' ,'praxios' ,'haeresis' ,'haereseos' ,'pater',
             'patros' ,'manus' ,'passus' ,'genu' ,'genus' ,'cornu' ,'cornus' ,'dies' ,'diei' ,'res' ,'rei' ,'fas',
             'reibus']

verify_database()  # Build or verify database
db_conn = sqlite3.connect('words.db')
db_curs = db_conn.cursor()
db_curs.execute("""SELECT DISTINCT infl_ending FROM inflects""")
# Auto-generate list of possible endings from database
endings = db_curs.fetchall()
endings = [e[0] for e in endings if e[0]]  # None should be included by default
endings.append('')  # This is None by default, we replace with ''
endings_vi = [e.replace('u', 'v').replace('j', 'i') for e in endings]


# Not great practice to reproduce program logic but this is simple enough that the method has been manually
# verified to produce the correct output.
# Go through each split and check if the ending is in list of possible endings obtained from database
def find_endings(w,endings_list_vi):
    splits = []
    w = w.replace('u', 'v').replace('j', 'i')  # Verify the word is VI and not UVIJ
    for i in range(len(w), 0, -1):
        wsub = w[i:]
        if wsub in endings_list_vi:
            splits.append(i)
    return splits


for w in noun_list:
    print("Word: {0}\tSlices: {1}".format(w,find_endings(w,endings_vi)))

db_conn.close()
