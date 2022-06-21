import unittest
import sqlite3
import pywords.lookup as lookup
from pywords.matchfilter import MatchFilter
from generate_database import verify_database

"""
VARIANTS
N 1     First declension nouns
    0   Usual first declension (aqua, acquae => aqu aqu)
    1   Usual first declension (aqua, acquae => aqu aqu)
    6   First declension 'Greek' (epitome, epitomes => epitom epitom; musice, musices => music  music)
    7   (cometes, cometae => comet comet)
    8   (Archias, Archiae => Archi Archi, Aeneas, Aeneae => Aene  Aene)

N 2     Second declension nouns
    0   Second declension nouns in "us"  amicus amici  =>  amic amic
    1   Second declension nouns in "us" 
    2   Second declension neuter nouns  verbum verbi  =>  verb verb
    3   Second declension nouns in "er" whether of not the "er" in base   puer pueri  =>  puer puer
        ager agri   =>  ager agr
    4   Early (BC) 2nd declension nouns in ius/ium (not filius-like) uses GENDER discrimination 
        to reduce to single VAR  radius 
        rad(i)i  => radi radi        M
        atrium atr(i)i  =>  atri atri       N
    5   Second declension special nouns in "ius", "filius" and proper names 
        filius fili  =>  fili  fili  --  but is very special case
        Lucius Lucii  =>  Luci  Luci
    6   Second declension "Greek" nouns  barbitos barbiti   =>   barbit barbit
    7   Androgeos  Androgeo  =>  Andregeos  Andrege
        Also for -ys for Greek -os  chelys  (-yn ACC)  =>  chelys  chel
        amphibachys  amphibrachyos  =>  amphibrachys  amphibrach
    8   Nouns from Greek in -on       --  only  N
        Ilion Ilii    =>  Ili  Ili   
    9 Panthus, Panthi => Panth Panth 

N 3     Third declension nouns
    0   Third declension, shared with 1, 8, 9
    1   Third declension M or F nouns whose stems end in a consonant
        miles militis  =>  miles milit
        lex legis  =>  lex leg
        frater fratris  =>  frater fratr
        soror sororis  =>  soror soror
        All third declension that have the endings -udo, -io, -tas, -x 
        pulcritudo pulcritudinis  =>  plucritudo pulcritudin
        legio legionis  =>  legio legion    
        varietas varietatis  =>  varietas varietat
        radix radicis  =>  radix  radic     
    2   Third declension  N nouns with stems ending in a consonant
        Ex: nomen nomenis  =>  nomen nomin
        Ex: iter itineris =>  iter itiner
        Ex: tempus temporis  =>  tempus  tempor
    3   Third declension nouns  I-stems (M & F)
        Ex: hostis hostis  =>  hostis host 
        Ex: finis finis  =>  finis fin
        Consonant i-stems
        Ex: urbs urbis  =>  urbs urb         
        Ex: mons montis  =>  mons mont
        Also use this for present participles (-ns) used as substantives in M & F
    4   Third declension nouns  I-stems (N)
        mare maris  =>  mare mar                       --  ending in "e"
        animal animalis  =>  animal animal             --  ending in "al"
        exemplar exemplaris  =>  exemplar exemplar     --  ending in "ar"
        Also use this for present participles (-ns) used as substantives in N     
    6   Third declension Greek nouns  aer aeris  =>  aer aer
    7   lampas lampados  =>  lampas  lampad;  Atlantis, Atlantidos  =>  Atlantis Atlantid
    8   Mixec Greek II and III  (V)
        Moses, Mosis  =>  Moses Mos
        Ulixes, Ulixis/i/ei  =>  Uxiles Uxil/Uxile     
        Achilles, Achillis  =>  Achilles Achill/Achille
    9   Both Greek 3rd declension and Latin 3rd.
        tigris tigris/tigridis  =>  tigris tigr/tigrid
        praxis praxios  =>  prax praxi
        haeresis haereseos  =>  haeres haerese (haeresis, -is is NOT --   of type 3 9, the ACC SING is haeresem)
        pater patros  =>  pater patr
        Note that the ACC SING can be derived from either the 1st or the 
        2nd stem (depends on word)

N 4     Fourth declension nouns
    0   Fourth declension nouns M & F in "us"
        passus passus  =>  pass pass
        manus manus  =>  man man
    1   Fourth declension nouns M & F in "us", same as 0
    2   Fourth declension nouns N in "u"
        genu genus  =>  gen gen
        cornu cornus  =>  corn corn
N 5     Fifth declension nouns
    1   All fifth declension nouns - N 5 1 
        dies diei  =>  di di
        res rei  =>  r r

N 9
    8 For abbreviations, indeclinable, but a special case vis. capitalization
    9 For those other few nouns that are not declined, e.g., fas

ADJECTIVES
ADJ 0 
      0  Adjectives where i must be in stem

ADJ 1
      0  
      1  First and second declension adjectives (-us in NOM SM )
         malus mala malum  => mal mal pei pessi 
         altus alta altum  =>  alt alt alti altissi
      2  Adjectives of first and second declension (-er) - ADJ 1 2 
         miser misera miserum  =>  miser miser miseri miserri
         sacer sacra sacrum  =>  sacer sacr zzz  sacerri     --  no COMP
         pulcher pulchri  =>  pulcher pulchr pulchri pulcherri
      3  nullus type adjectives           (with ius in GEN and i in DAT sing)
         nullus (gen) nullius  =>  null null zzz zzz   --  no COMP or SUPER
      4  nullus type adjectives in -er    (with ius in GEN and i in DAT sing)
         alter, altera, alterum   =>  alter   alter
         neuter, neutra, neutrum  =>  neuter  neutr
      5  alius, alia, aliud => ali ali    
         (sort of has ius in GEN {but we put i in stem} and i in DAT sing)
         Has alternative form alterius in GEN SING 

ADJ 2  An ADJ declension from the Greek - made up based on Greek nouns
         For the -os, -on adjectives, which OLD cites
         I am saying that -os is the ending for Common, not Masculine
         Like other ADJ 1 1, the stems are the same
         Plurals are the same as ADJ 1 1 
      0  Default for plurals
      1  -,  e,  -  the F part 
      2  -,  a,  -  the F part 
      3  es, es, es adjectives
      6  os, os, - 
      7  os, -,  -
      8  -,  -,  on 

ADJ 3
      0  
      1  Adjectives of third declension - one ending  - ADJ 3 1 
         audax (gen) audacis  =>  audax audac audaci audacissi
         prudens prudentis  =>  prudens prudent prudenti prudentissi
      2  Adjectives of third declension - two endings   - ADJ 3 2 
         brevis breve  =>  brev brev brevi brevissi
         facil facil   =>  facil facil facili facilli
      3  Adjectives of third declension - three endings  - ADJ 3 3 
         celer celeris  celere  =>  celer celer celeri celerri
         acer acris acre  =>  acer acr acri acerri
      6  Greek adjectives of third declension
         This is a real wild guess, but is generated from the Greek forms 
         In Greek there are two endings, but is compressed to one in Latin
         amethystizon amethystizontos => amethystizon amethystizont
         
ADJ 9
      8  For ADJ abbreviations, indeclinable, but a special case vis. capitalization
      9  For adjective that is not declined                    


VERBS
V 0 
    0   Default case, used in same place as V 1 1
V 1
    1   Verbs of the first conjugation
        voco vocare vocavi vocatus  =>  voc voc vocav vocat
        porto portave portavi portatus  =>  port port portav portat

V 2 
    1   Verbs of the second conjugation
        The characteristic 'e' is in the inflection, not carried in the stem
        moneo monere monui monitum  =>  mon mon monu monit
        habeo habere habui habitus  =>  hab hab habu habit
        deleo delere delevi deletus  =>  del del delev delet
        iubeo iubere iussi iussus  =>   iub iub iuss iuss
        video videre vidi visus  =>  vid vid vid vis

V 3 
    0
    1   Verbs of the third conjugation, variant 1
        rego regere rexi rectum  =>  reg reg rex rect
        pono ponere posui positus  =>  pon pon posu posit
        capio capere cepi captus  => capi cap cep capt   --  I-stem too w/KEY
    2   Irregular verbs similar to third conj
        fero ferre tuli latus  =>  fer fer tul lat
    3   Irregular verbs similar to 3rd/4th conj, no perfect system
        fio fieri factus sum   =>  fi f zzz fact           
    4   Verbs of the fourth conjugation are coded as a variant of third
        audio audire audivi auditus  =>  audi aud audiv audit

V 5
    1   Verbs like to be
        sum esse fui futurus  =>  s . fu fut
        adsum adesse adfui adfuturus  =>  ads ad adfu adfut

V 6
    1   Verb eo, ire, ivi/ii, itus
        eo ire ivi itus  =>  e i iv (i) it
    2   Verbs like volo
        volo velle volui -  =>  vol vel volu -
        nolo nolle nolui -  =>  nol nol nolu -
        malo malle malui -  =>  mal mal malu -

V 7 
    1   Defective third decl verbs
        aio  x   =>  ai  a  zzz   zzz
    2   Defective verb
        inquam   =>  inqui  inqu   zzz  zzz
    3   Defective third decl verbs
        edo edere/esse edi esus  =>  ed ed ed es (+ ed es zzz  zzz)

V 8 
    0   Third conjugation variant
        Consists of removing the -er- after s/x (since r was originally s)
        Ex: faxo FUTP IND of facere, faxim PERF SUB, faxem PLUP SUB - stem 3 fax
        Ex: capso FUTP of capere
        Ex: duxim FUTP of ducere
        And certain other early forms (e.g., amassis = amaveris)
        There is no KEY = 4 inflection, so the 4th stem is zzz

V 9
    8   Abbreviations, indeclinable, but a special   case vis. capitalization
    9   Undeclined verb

"""


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
        self.assertEqual(lookup.find_endings("aqua"),[4,3,2])
        self.assertEqual(lookup.find_endings("aqua") , [4, 3, 2])
        self.assertEqual(lookup.find_endings("aquae") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("epitome") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("epitomes") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("cometes") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("cometae") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("Archias") , [7, 6, 5, 4])
        self.assertEqual(lookup.find_endings("Archiae") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("amicus") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("amici") , [5, 4])
        self.assertEqual(lookup.find_endings("verbum") , [6, 4])
        self.assertEqual(lookup.find_endings("verbi") , [5, 4])
        self.assertEqual(lookup.find_endings("puer") , [4, 2])
        self.assertEqual(lookup.find_endings("pueri") , [5, 4, 3, 2])
        self.assertEqual(lookup.find_endings("ager") , [4, 2])
        self.assertEqual(lookup.find_endings("agri") , [4, 3, 2])
        self.assertEqual(lookup.find_endings("radius") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("radii") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("atrium") , [6, 4, 3])
        self.assertEqual(lookup.find_endings("atrii") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("atri") , [4, 3, 2])
        self.assertEqual(lookup.find_endings("filius") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("fili") , [4, 3])
        self.assertEqual(lookup.find_endings("Lucius") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("Lucii") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("barbitos") , [8, 7, 6] )
        self.assertEqual(lookup.find_endings("barbiti") , [7, 6])
        self.assertEqual(lookup.find_endings("Androgeos") , [9, 8, 7])
        self.assertEqual(lookup.find_endings("Androgeo") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("amphibrachys") , [12, 11])
        self.assertEqual(lookup.find_endings("amphibrachyos") , [13, 12, 11, 10])
        self.assertEqual(lookup.find_endings("chelys") , [6, 5])
        self.assertEqual(lookup.find_endings("Ilion") , [5, 3])
        self.assertEqual(lookup.find_endings("Ilii") , [4, 3, 2])
        self.assertEqual(lookup.find_endings("Panthus") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("Panthi") , [6, 5])
        self.assertEqual(lookup.find_endings("miles") , [5, 4, 3, 2])
        self.assertEqual(lookup.find_endings("militis") , [7, 6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("frater") , [6, 4])
        self.assertEqual(lookup.find_endings("fratris") , [7, 6, 5, 4])
        self.assertEqual(lookup.find_endings("soror") , [5, 3])
        self.assertEqual(lookup.find_endings("sororis") , [7, 6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("pulchritudo") , [11, 10])
        self.assertEqual(lookup.find_endings("pulchritudinis") , [14, 13, 12])
        self.assertEqual(lookup.find_endings("legio") , [5, 4])
        self.assertEqual(lookup.find_endings("legionis") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("varietas") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("varietatis") , [10, 9, 8, 7, 6])
        self.assertEqual(lookup.find_endings("radix") , [5])
        self.assertEqual(lookup.find_endings("radicis") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("nomen") , [5, 3])
        self.assertEqual(lookup.find_endings("nominis") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("iter") , [4, 2])
        self.assertEqual(lookup.find_endings("itineris") , [8, 7, 6, 5, 4])
        self.assertEqual(lookup.find_endings("tempus") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("temporis") , [8, 7, 6, 5, 4])
        self.assertEqual(lookup.find_endings("hostis") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("finis") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("urbs") , [4, 3])
        self.assertEqual(lookup.find_endings("urbis") , [5, 4, 3, 2])
        self.assertEqual(lookup.find_endings("mons") , [4, 3])
        self.assertEqual(lookup.find_endings("montis") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("mare") , [4, 3, 2, 1])
        self.assertEqual(lookup.find_endings("maris") , [5, 4, 3, 2, 1])
        self.assertEqual(lookup.find_endings("animal") , [6])
        self.assertEqual(lookup.find_endings("animalis") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("exemplar") , [8, 6])
        self.assertEqual(lookup.find_endings("exemplaris") , [10, 9, 8, 7, 6])
        self.assertEqual(lookup.find_endings("aer") , [3, 1])
        self.assertEqual(lookup.find_endings("aeris") , [5, 4, 3, 2, 1])
        self.assertEqual(lookup.find_endings("lampas") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("lampados") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("Moses") , [5, 4, 3, 2])
        self.assertEqual(lookup.find_endings("Mosis") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("Ulixes") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("Ulixis") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("Ulixi") , [5, 4])
        self.assertEqual(lookup.find_endings("Ulixei") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("Achilles") , [8, 7, 6, 5])
        self.assertEqual(lookup.find_endings("Achillis") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("tigris") , [6, 5, 4, 3])
        self.assertEqual(lookup.find_endings("tigridis") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("praxis") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("praxios") , [7, 6, 5])
        self.assertEqual(lookup.find_endings("haeresis") , [8, 7, 6])
        self.assertEqual(lookup.find_endings("haereseos") , [9, 8, 7])
        self.assertEqual(lookup.find_endings("pater") , [5, 3])
        self.assertEqual(lookup.find_endings("patros") , [6, 5, 4])
        self.assertEqual(lookup.find_endings("manus") , [5, 4, 3])
        self.assertEqual(lookup.find_endings("passus") , [6, 5, 4])
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

    def test__simple_match_nouns_number_of_matches(self):
        self.assertEqual(lookup._simple_match('aqua')
        self.assertEqual(lookup._simple_match('aquae')
        self.assertEqual(lookup._simple_match('epitome')
        self.assertEqual(lookup._simple_match('epitomes')
        self.assertEqual(lookup._simple_match('cometes')
        self.assertEqual(lookup._simple_match('cometae')
        self.assertEqual(lookup._simple_match('Archias')
        self.assertEqual(lookup._simple_match('Archiae')
        self.assertEqual(lookup._simple_match('amicus')
        self.assertEqual(lookup._simple_match('amici')
        self.assertEqual(lookup._simple_match('verbum')
        self.assertEqual(lookup._simple_match('verbi')
        self.assertEqual(lookup._simple_match('puer')
        self.assertEqual(lookup._simple_match('pueri')
        self.assertEqual(lookup._simple_match('ager')
        self.assertEqual(lookup._simple_match('agri')
        self.assertEqual(lookup._simple_match('radius')
        self.assertEqual(lookup._simple_match('radii')
        self.assertEqual(lookup._simple_match('atrium')
        self.assertEqual(lookup._simple_match('atrii')
        self.assertEqual(lookup._simple_match('atri')
        self.assertEqual(lookup._simple_match('filius')
        self.assertEqual(lookup._simple_match('fili')
        self.assertEqual(lookup._simple_match('Lucius')
        self.assertEqual(lookup._simple_match('Lucii')
        self.assertEqual(lookup._simple_match('barbitos')
        self.assertEqual(lookup._simple_match('barbiti')
        self.assertEqual(lookup._simple_match('Androgeos')
        self.assertEqual(lookup._simple_match('Androgeo')
        self.assertEqual(lookup._simple_match('amphibrachys')
        self.assertEqual(lookup._simple_match('amphibrachyos')
        self.assertEqual(lookup._simple_match('chelys')
        self.assertEqual(lookup._simple_match('Ilion')
        self.assertEqual(lookup._simple_match('Ilii')
        self.assertEqual(lookup._simple_match('Panthus')
        self.assertEqual(lookup._simple_match('Panthi')
        self.assertEqual(lookup._simple_match('miles')
        self.assertEqual(lookup._simple_match('militis')
        self.assertEqual(lookup._simple_match('frater')
        self.assertEqual(lookup._simple_match('fratris')
        self.assertEqual(lookup._simple_match('soror')
        self.assertEqual(lookup._simple_match('sororis')
        self.assertEqual(lookup._simple_match('pulchritudo')
        self.assertEqual(lookup._simple_match('pulchritudinis')
        self.assertEqual(lookup._simple_match('legio')
        self.assertEqual(lookup._simple_match('legionis')
        self.assertEqual(lookup._simple_match('varietas')
        self.assertEqual(lookup._simple_match('varietatis')
        self.assertEqual(lookup._simple_match('radix')
        self.assertEqual(lookup._simple_match('radicis')
        self.assertEqual(lookup._simple_match('nomen')
        self.assertEqual(lookup._simple_match('nominis')
        self.assertEqual(lookup._simple_match('iter')
        self.assertEqual(lookup._simple_match('itineris')
        self.assertEqual(lookup._simple_match('tempus')
        self.assertEqual(lookup._simple_match('temporis')
        self.assertEqual(lookup._simple_match('hostis')
        self.assertEqual(lookup._simple_match('finis')
        self.assertEqual(lookup._simple_match('urbs')
        self.assertEqual(lookup._simple_match('urbis')
        self.assertEqual(lookup._simple_match('mons')
        self.assertEqual(lookup._simple_match('montis')
        self.assertEqual(lookup._simple_match('mare')
        self.assertEqual(lookup._simple_match('maris')
        self.assertEqual(lookup._simple_match('animal')
        self.assertEqual(lookup._simple_match('animalis')
        self.assertEqual(lookup._simple_match('exemplar')
        self.assertEqual(lookup._simple_match('exemplaris')
        self.assertEqual(lookup._simple_match('aer')
        self.assertEqual(lookup._simple_match('aeris')
        self.assertEqual(lookup._simple_match('lampas')
        self.assertEqual(lookup._simple_match('lampados')
        self.assertEqual(lookup._simple_match('Moses')
        self.assertEqual(lookup._simple_match('Mosis')
        self.assertEqual(lookup._simple_match('Ulixes')
        self.assertEqual(lookup._simple_match('Ulixis')
        self.assertEqual(lookup._simple_match('Ulixi')
        self.assertEqual(lookup._simple_match('Ulixei')
        self.assertEqual(lookup._simple_match('Achilles')
        self.assertEqual(lookup._simple_match('Achillis')
        self.assertEqual(lookup._simple_match('tigris')
        self.assertEqual(lookup._simple_match('tigridis')
        self.assertEqual(lookup._simple_match('praxis')
        self.assertEqual(lookup._simple_match('praxios')
        self.assertEqual(lookup._simple_match('haeresis')
        self.assertEqual(lookup._simple_match('haereseos')
        self.assertEqual(lookup._simple_match('pater')
        self.assertEqual(lookup._simple_match('patros')
        self.assertEqual(lookup._simple_match('manus')
        self.assertEqual(lookup._simple_match('passus')
        self.assertEqual(lookup._simple_match('genu')
        self.assertEqual(lookup._simple_match('genus')
        self.assertEqual(lookup._simple_match('cornu')
        self.assertEqual(lookup._simple_match('cornus')
        self.assertEqual(lookup._simple_match('dies')
        self.assertEqual(lookup._simple_match('diei')
        self.assertEqual(lookup._simple_match('res')
        self.assertEqual(lookup._simple_match('rei')
        self.assertEqual(lookup._simple_match('fas')

    def test__remove_enclitics(self):
        pass
    def test_match_word(self):
        pass
    def test_get_dictionary_string(self):
        pass


if __name__ == '__main__':
    unittest.main()

    #filt = MatchFilter(substantives=True)

    ## superlative adjective
    #words.lookup_word('maximum')
    #words.lookup_word('prior')
    #words.lookup_word('unus')
    ##words.lookup_word('vnvs')
    #words.lookup_word('paret')
    #words.lookup_word('imperat')  # TODO Returns noun, which is incorrect
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
