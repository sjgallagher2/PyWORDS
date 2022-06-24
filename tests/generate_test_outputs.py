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


def get_stemN_endings(cursor,stem,stemN):
    """
    Get endings available for dl_stemN (N=1,2,3,4) for word stem `stem`
    """
    if stemN not in [1,2,3,4]:
        raise ValueError("Stem must be one of: 1,2,3,4")
    query = """SELECT dictline.dl_id,dictline.dl_stem{0},inflects.infl_id,inflects.infl_ending
    FROM dictline
    JOIN inflects ON dictline.dl_type = inflects.infl_type 
        AND dictline.dl_variant = inflects.infl_variant
        AND dictline.dl_pos = inflects.infl_pos
    WHERE dictline.dl_stem{0}= '{1}' 
        AND inflects.infl_stem_id IS {0} AND inflects.infl_frequency IS 'A'
    ;
    """.format(stemN,stem)
    cursor.execute(query)
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

#verify_database()  # Build or verify database
db_conn = sqlite3.connect('words.db')
db_curs = db_conn.cursor()
#db_curs.execute("""SELECT DISTINCT infl_ending FROM inflects""")
endings = get_possible_endings(db_curs,'aqu')

# Auto-generate list of possible endings from database
#endings = [e[0] for e in endings if e[0]]  # None should be included by default
#endings.append('')  # This is None by default, we replace with ''
#endings_vi = [e.replace('u', 'v').replace('j', 'i') for e in endings]
#
#
## Not great practice to reproduce program logic but this is simple enough that the method has been manually
## verified to produce the correct output.
## Go through each split and check if the ending is in list of possible endings obtained from database
#def find_endings(w,endings_list_vi):
#    splits = []
#    w = w.replace('u', 'v').replace('j', 'i')  # Verify the word is VI and not UVIJ
#    for i in range(len(w), 0, -1):
#        wsub = w[i:]
#        if wsub in endings_list_vi:
#            splits.append(i)
#    return splits
#
#
#for w in noun_list:
#    print("Word: {0}\tSlices: {1}".format(w,find_endings(w,endings_vi)))
#
db_conn.close()
