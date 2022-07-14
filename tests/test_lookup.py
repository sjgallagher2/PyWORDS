import unittest
import random
import sqlite3
import pywords.lookup as lookup
from pywords.lookup import WordMatch
import pywords.definitions as definitions
from pywords.matchfilter import MatchFilter
import pywords.utils as pwutils
#from generate_database import verify_database


def build_dictline_from_str(s):
    ps = s[:34].split()
    senses = s[34:]
    pos = definitions.parts_of_speech[ps[0]]
    if pos == 'noun':
        return definitions.DictlineNounEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],ps[9],senses)
    if pos == 'adjective':
        return definitions.DictlineAdjectiveEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'verb':
        return definitions.DictlineVerbEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'adverb':
        return definitions.DictlineAdverbEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],senses)
    if pos == 'conjunction':
        return definitions.DictlineConjunctionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],senses)
    if pos in ['pronoun','pack (internal use only)']:
        return definitions.DictlinePronounEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'number':
        return definitions.DictlineNumberEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],ps[9],senses)
    if pos == 'preposition':
        return definitions.DictlinePrepositionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],senses)
    if pos == 'interjection':
        return definitions.DictlineInterjectionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],senses)


class TestDictlineClasses(unittest.TestCase):
    def test_dictline_noun_entry_eq(self):
        noun1 = definitions.DictlineNounEntry(pos='N',decl='1',variant='1',gender='M',noun_kind='T',age='A',area='Y',
                                              geog='C',freq='A',src='X',senses='definitions, arbitrarily filled')
        noun2 = definitions.DictlineNounEntry(pos='N',decl='1',variant='1',gender='M',noun_kind='T',age='A',area='Y',
                                              geog='C',freq='A',src='X',senses='definitions, arbitrarily filled')
        self.assertTrue(noun1 == noun2)

    def test_dictline_noun_entry_not_eq(self):
        noun1 = definitions.DictlineNounEntry(pos='N',decl='1',variant='1',gender='M',noun_kind='T',age='A',area='Y',
                                              geog='C',freq='A',src='X',senses='definitions, arbitrarily filled')
        noun3 = definitions.DictlineNounEntry(pos='N',decl='2',variant='1',gender='M',noun_kind='T',age='A',area='Y',
                                              geog='C',freq='A',src='X',senses='definitions, arbitrarily filled')
        self.assertFalse(noun1 == noun3)

    def test_dictline_pronoun_entry_eq(self):
        pron1 = definitions.DictlinePronounEntry(pos='PRON',decl='1',variant='1',pronoun_kind='PERS',age='A',area='Y',
                                                 geog='A',freq='X',src='A',senses='definitions, arbitrarily filled')
        pron2 = definitions.DictlinePronounEntry(pos='PRON',decl='1',variant='1',pronoun_kind='PERS',age='A',area='Y',
                                                 geog='A',freq='X',src='A',senses='definitions, arbitrarily filled')
        self.assertTrue(pron1 == pron2)

    def test_dictline_pronoun_entry_not_eq(self):
        pron1 = definitions.DictlinePronounEntry(pos='PRON',decl='1',variant='1',pronoun_kind='PERS',age='A',area='Y',
                                                 geog='A',freq='X',src='A',senses='definitions, arbitrarily filled')
        pron3 = definitions.DictlinePronounEntry(pos='PRON',decl='1',variant='2',pronoun_kind='PERS',age='A',area='Y',
                                                 geog='A',freq='X',src='A',senses='definitions, arbitrarily filled')
        self.assertFalse(pron1 == pron3)


class TestLookup(unittest.TestCase):
    def setUp(self):
        pass
        #verify_database()  # Build or verify database
        #self.db_conn = sqlite3.connect('words.db')
        #self.db_curs = self.db_conn.cursor()

    def tearDown(self):
        pass
        #self.db_conn.close()

    def test_find_endings_splices(self):
        # Just some random nouns from the list
        self.assertEqual(lookup.find_endings("aqua"),[4,3,2])  # aqua, aqu|a, aq|ua
        self.assertEqual(lookup.find_endings("aquae") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("aqvae") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("epitome") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("epitomes") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("cometes") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("cometae") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("Lucius") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("Lucii") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("barbitos") , [8, 7, 6] )
        self.assertEqual(lookup.find_endings("barbiti") , [7, 6])
        self.assertEqual(lookup.find_endings("Androgeos") , [9, 8, 7])
        self.assertEqual(lookup.find_endings("Androgeo") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("amphibrachys") , [12, 11])
        self.assertEqual(lookup.find_endings("amphibrachyos") , [13, 12, 11, 10])
        self.assertEqual(lookup.find_endings("iter") , [4, 2])
        self.assertEqual(lookup.find_endings("itineris") , [8, 7, 6, 5, 4])
        self.assertEqual(lookup.find_endings("genu") , [4, 3])
        self.assertEqual(lookup.find_endings("genus") , [5, 4, 3, 1])
        self.assertEqual(lookup.find_endings("cornu") , [5, 4])
        self.assertEqual(lookup.find_endings("cornus") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("dies") , [4, 3, 2, 1])
        self.assertEqual(lookup.find_endings("diei") , [4, 3, 2])
        self.assertEqual(lookup.find_endings("res") , [3, 2, 1])
        self.assertEqual(lookup.find_endings("rei") , [3, 2, 1])
        self.assertEqual(lookup.find_endings("reibus") , [6, 5, 4, 2])
        self.assertEqual(lookup.find_endings("fas") , [3, 2, 1])

    def test__simple_match_nouns(self):
        # Build dictline entries we expect to see
        aqua_dictline_str   = "N      1 1 F T          X X X A O water; sea, lake; river, stream; rain, rainfall (pl.), rainwater; spa; urine;"
        Mos_dictline_str    = "N      1 1 F T          X X N E O river Maas/Meuse, in Holland/France/Belgium;"
        Moses_dictline_str  = "N      3 8 M P          E E Q E E Moses;"

        aqua_dl_entry = build_dictline_from_str(aqua_dictline_str)
        Mos_dl_entry = build_dictline_from_str(Mos_dictline_str)
        Moses_dl_entry = build_dictline_from_str(Moses_dictline_str)

        # Find endings 'aqua':'', 'aqu':'a', select only 'aqu':'a', find dictline for 'aqu', ignore deponent verb
        # 'aquor' because there is no 'a' ending in the passive voice (there is in the active however)
        self.assertEqual(lookup._simple_match('aqua'),[WordMatch('aqu','a','aqu','aqu','','',aqua_dl_entry)])
        self.assertEqual(lookup._simple_match('aquae'),[WordMatch('aqu','ae','aqu','aqu','','',aqua_dl_entry)])

        # Find endings 'Moses':'', 'Mos':'es', both return same noun
        self.assertEqual(lookup._simple_match('Moses'),[WordMatch('Moses','','Moses','Mos','','',Moses_dl_entry),
                                                        WordMatch('Mos','es','Moses','Mos','','',Moses_dl_entry)])
        # Find endings 'Mos':'is' (x2), one for Mos and one for Moses
        self.assertEqual(lookup._simple_match('Mosis'),[WordMatch('Mos','is','Mos','Mos','','',Mos_dl_entry),
                                                        WordMatch('Mos','is','Moses','Mos','','',Moses_dl_entry)])

    def test__simple_match_adjectives(self):
        malus1_dictline_str  = "N      2 1 M T          X X X D X mast; beam; tall pole, upright pole; standard, prop, staff;"
        malus2_dictline_str  = "N      2 1 F T          X X X D X apple tree;"
        malus3_dictline_str  = "ADJ    1 1 X            X X X A X bad, evil, wicked; ugly; unlucky;"

        pessimus_dictline_str = "ADJ    0 0 SUPER        X X X A O worst, most incapable; wickedest; most disloyal/unkind; lowest in quality/rank;"

        malus1_dl_entry = build_dictline_from_str(malus1_dictline_str)
        malus2_dl_entry = build_dictline_from_str(malus2_dictline_str)
        malus3_dl_entry = build_dictline_from_str(malus3_dictline_str)
        pessimus_dl_entry = build_dictline_from_str(pessimus_dictline_str)
        # Find endings 'malu':'s' and 'mal':'us', reject first noun and verb with no matching endings,
        # some adjective forms for wrong stem, accept two nouns and an adjective
        # This also agrees with wiktionary, no funky varieties
        self.assertEqual(lookup._simple_match('malus'),[WordMatch('mal','us','mal','mal','','',malus1_dl_entry),
                                                        WordMatch('mal','us','mal','mal','','',malus2_dl_entry),
                                                        WordMatch('mal','us','mal','mal','pej','-',malus3_dl_entry)])

        # Comparative ADJ 0 0, verify ignoring i/j
        self.assertEqual(lookup._simple_match('peior'),[WordMatch('pei','or','mal','mal','pej','-',malus3_dl_entry)])
        self.assertEqual(lookup._simple_match('pejor'),[WordMatch('pej','or','mal','mal','pej','-',malus3_dl_entry)])

        # Superlative adjective with separate SUPER dictline entry
        self.assertEqual(lookup._simple_match('pessimus'),[WordMatch('pessi','mus','','','','pessi',pessimus_dl_entry)])

    def test__simple_match_verbs(self):
        # SETUP
        laudare_dictline_str =  "V      1 1 X            X X X A X recommend; praise, approve, extol; call upon, name; deliver eulogy on;"
        orere_dictline_str =    "V      3 1 X            E X X E X burn;"
        orare_dictline_str =    "V      1 1 X            X X X A X beg, ask for, pray; beseech, plead, entreat; worship, adore;"
        orior1_dictline_str =   "V      3 1 DEP          X X X B O rise (sun/river); arise/emerge, crop up; get up (wake); begin; originate from; be born/created; be born of, descend/spring from; proceed/be derived (from);"
        orior2_dictline_str =   "V      3 4 DEP          X X X A O rise (sun/river); arise/emerge, crop up; get up (wake); begin; originate from; be born/created; be born of, descend/spring from; proceed/be derived (from);"
        olfacere_dictline_str = "V      3 1 TRANS        X X X C O smell/detect odor of; get wind of/hear about; smell/sniff at; cause to smell of;"
        placere1_dictline_str = "V      1 1 X            X X X B X appease; placate; reconcile;"
        placere2_dictline_str = "V      2 1 DAT          X X X A X please, satisfy, give pleasure to (with dat.);"
        placere3_dictline_str = "V      2 1 IMPERS       X X X D X it is pleasing/satisfying, gives pleasure; is believed/settled/agreed/decided;"
        placere4_dictline_str = "N      9 9 N A          F X X F Z pleasure (Wiktionary);"
        fieri_dictline_str =    "V      3 3 SEMIDEP      X X X A O happen, come about; result (from); take place, be held, occur, arise (event); be made/created/instituted/elected/appointed/given; be prepared/done; develop; be made/become; (facio PASS); [fiat => so be it, very well; it is being done];"
        adest1_dictline_str =   "V      5 1 TO_BEING     X X X A O be near, be present, be in attendance, arrive, appear; aid (w/DAT);"
        adest2_dictline_str =   "V      5 1 TO_BEING     B X X C S be near, be present, be in attendance, arrive, appear; aid (w/DAT);"
        adest3_dictline_str =   "V      5 1 TO_BEING     X X X A O be near, be present, be in attendance, arrive, appear; aid (w/DAT);"

        laudare_dl_entry = build_dictline_from_str(laudare_dictline_str)
        orere_dl_entry = build_dictline_from_str(orere_dictline_str)
        orare_dl_entry = build_dictline_from_str(orare_dictline_str)
        orior1_dl_entry = build_dictline_from_str(orior1_dictline_str)
        orior2_dl_entry = build_dictline_from_str(orior2_dictline_str)
        olfacere_dl_entry = build_dictline_from_str(olfacere_dictline_str)
        placere1_dl_entry = build_dictline_from_str(placere1_dictline_str)
        placere2_dl_entry = build_dictline_from_str(placere2_dictline_str)
        placere3_dl_entry = build_dictline_from_str(placere3_dictline_str)
        placere4_dl_entry = build_dictline_from_str(placere4_dictline_str)
        fieri_dl_entry = build_dictline_from_str(fieri_dictline_str)
        adest1_dl_entry = build_dictline_from_str(adest1_dictline_str)
        adest2_dl_entry = build_dictline_from_str(adest2_dictline_str)
        adest3_dl_entry = build_dictline_from_str(adest3_dictline_str)

        # TESTS
        self.assertEqual(lookup._simple_match('laudo'),[WordMatch('laud','o','laud','laud','laudav','laudat',laudare_dl_entry)])
        self.assertEqual(lookup._simple_match('laudatum'),[WordMatch('laudat','um','laud','laud','laudav','laudat',laudare_dl_entry)])
        self.assertEqual(lookup._simple_match('laudandus'),[WordMatch('laud','andus','laud','laud','laudav','laudat',laudare_dl_entry)])

        # Deponent verb orior has no active voice; rare verb orere (to burn) does exist though
        self.assertEqual(lookup._simple_match('orit'),[WordMatch('or','it','or','or','-','-',orere_dl_entry)])
        # Orior has two forms for perfect stem, so two entries are returned
        self.assertEqual(lookup._simple_match('orior'),[WordMatch('ori','or','ori','or','-','orit',orior1_dl_entry),
                                                        WordMatch('ori','or','ori','or','-','ort',orior2_dl_entry)])

        # 'sum' is a unique (technically in ESSE.LAT), not handled by _simple_match
        # Also tests V 3 1 -c stems with empty imperative form; it should *not* return sumo -ere
        self.assertEqual(lookup._simple_match('sum'),[])
        # Tests V 3 1 -c stem with empty imperative form
        self.assertEqual(lookup._simple_match('olfac'),[WordMatch('olfac','','olfaci','olfac','olfec','olfact',olfacere_dl_entry)])

        # Test impersonal verb
        self.assertEqual(lookup._simple_match('placere'),[WordMatch('placere','','placere','','','',placere4_dl_entry),   # placere (noun form)
                                                          WordMatch('plac','ere','plac','plac','placav','placat',placere1_dl_entry),  # placo, placare
                                                          WordMatch('plac','ere','plac','plac','placu','placit',placere2_dl_entry),   # placere (takes dat.)
                                                          WordMatch('plac','ere','plac','plac','-','placit',placere3_dl_entry)])
        self.assertEqual(lookup._simple_match('placuit'),[WordMatch('placu','it','plac','plac','placu','placit',placere2_dl_entry)])

        # Semideponent infinitive
        self.assertEqual(lookup._simple_match('fieri'),[WordMatch('f','ieri','fi','f','-','fact',fieri_dl_entry)])

        # TO_BEING verb
        self.assertEqual(lookup._simple_match('adest'),[WordMatch('ad','est','ads','ad','adfu','adfut',adest1_dl_entry),
                                                        WordMatch('ad','est','ads','ad','arfu','arfut',adest2_dl_entry),
                                                        WordMatch('ad','est','ass','ad','affu','affut',adest3_dl_entry)])


        #self.assertEqual(lookup._simple_match('<fullword>'),[WordMatch('<stem>','<end>','','','','',<word>_dl_entry)])

    def test_match_word(self):
        pass

    def test_get_dictionary_string(self):
        pass

    def test__match_tackon(self):
        pass

    def test__check_tackons(self):
        pass


if __name__ == '__main__':
    lookup.lookup_word('praedium')
    lookup.lookup_word('articulus')
    lookup.lookup_word('Adam')
    lookup.lookup_word('aer')  # Greek
    lookup.lookup_word('aedes')  # i-stem
    pwutils.get_vocab_list('articulus',markdown_fmt=True,vocab_list='llpsi')

    #unittest.main()

    #filt = MatchFilter(substantives=True)

    ## superlative adjective
    #words.lookup_word('maximum')
    #words.lookup_word('prior')
    #words.lookup_word('unus')
    ##words.lookup_word('vnvs')
    #words.lookup_word('paret')
    #words.lookup_word('imperat')
    #words.lookup_word('sumit')
    #words.lookup_inflections('maximum')
    #words.lookup_inflections('prior')
    #words.lookup_inflections('unus')
    #print("Should be the same:")
    #words.lookup_inflections('vnvs')
    #print("Moving on..")
    #words.lookup_inflections('paret')
    #words.lookup_inflections('imperat')
    #words.lookup_inflections('sumit')

    # Need to test a word from each declension-variant and conjugation-variant pair, and combinations
    # of e.g. comparison, verb type, etc, for all parts of speech
    # Need to test i/j and u/v interchanges

    # Whitaker provides a number of examples, see `docs/notes.txt`
