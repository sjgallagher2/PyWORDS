'''
Clean missing word lists and analyze stems
'''

import pywords.lookup as lookup
import pywords.definitions as definitions
from pywords.matchfilter import MatchFilter
import os
import re

# PROCESSING
# Remove duplicates
# Remove invalid words
#   Usually or always invalid:
#     * Words < 4 letters long   (any mistakes should be covered by the appearance of other endings)
#     * Words with only consonants
#     * Words with only IVXLCDM (Roman numerals)
#     * Words with non-ascii characters
# Look for Latin word endings and put these words at the top of the list
#

            
def has_vowel(w):
    vowels = ['a','e','i','j','o','u','v'] # Forgiving list
    for ltr in w:
        if ltr in vowels:
            return True
    return False

def has_only_numeral(w):
    numerals = ['i','v','x','l','c','d','m']
    for ltr in w:
        if ltr not in numerals:
            return False
    return True

def get_stems(word_list):
    stems = {} # Dictionary of possible stems as stem:[full_word1, full_word2, ...]
    for i in range(0,len(word_list)):
        endings = lookup.find_endings(word_list[i],skip_zero=True)
        for stem,e in endings.items():
            if stem in stems.keys():
                stems[stem].append(word_list[i])
            else:
                stems[stem] = [word_list[i]]
    return stems


def get_missing_word_report(words, output_file_name):
    """
    Write a text file `output_file_name` from a word list `words` containing
    filtering and analysis of the missed words.
    """
    n_orig_words = len(words)
    
    words = sorted(list(set(words))) # Remove duplicates and whitespace
    words = [w.strip() for w in words if len(w) > 4] # Account for last \n character with < instead of <=
    
    gwords = [] # Good words
    twords = [] # Tentative words
    bad_words = [] # Throw out
    for w in words:
        # Nest ifs to save processing
        if w.isascii() and has_vowel(w) and not has_only_numeral(w):
            twords.append(w)
        else:
            bad_words.append(w)
    n_twords = len(twords)
    
    stems = get_stems(twords)
    if stems:
        for stem in stems.keys():
            if len(stems[stem]) > 1:
                for w in stems[stem]:
                    gwords.append(w)
        gwords = sorted(list(set(gwords)))
        n_gwords = len(gwords)
        
    
    f = open(output_file_name,'w')
    
    f.write('Original number of words: '+str(n_orig_words)+'\n')
    f.write('Number of words after winnowing: '+str(n_twords)+'\n')
    f.write('Number of words with valid Latin endings: '+str(n_gwords)+'\n')
    f.write('=====================================================\nGOOD WORD LIST: \n---------------------\n')
    for w in gwords:
        f.write(w+'\n')
    f.write('=====================================================\nTENTATIVE WORD LIST (Superset): \n---------------------\n')
    for w in twords:
        f.write(w+'\n')
    f.write('=====================================================\nPOSSIBLE WORDS WITH STEMS: \n---------------------\n')
    if stems:
        for stem in stems.keys():
            if len(stems[stem]) > 2:
                f.write('STEM: '+stem+'\n')
                for w in stems[stem]:
                    f.write('\t  -> '+w+'\n')
                f.write('DECLENSION ANALYSIS:\n')
                # Given a word stem, get possible inflections for each instance
                possible_infls = []
                for w in stems[stem]:
                    possible_infls.append(definitions.reverse_ending_lookup(w[len(stem):]))
                # possible_infls is now a list of lists of 'valid' inflections
                
                # Need to organize by part of speech
                possible_n_infls = []
                possible_adj_infls = []
                possible_v_infls = []
                
                for inst_infls in possible_infls: # For each instance inflection
                    
                    inst_n_infls = []
                    inst_adj_infls = []
                    inst_v_infls = []
                    
                    for infl in inst_infls:
                        if isinstance(infl,definitions.NounInfl):
                            inst_n_infls.append(infl)
                        elif isinstance(infl,definitions.AdjectiveInfl):
                            inst_adj_infls.append(infl)
                        elif isinstance(infl,definitions.VerbInfl) or isinstance(infl,definitions.VerbParticipleInfl):
                            inst_v_infls.append(infl)
                    possible_n_infls.append(inst_n_infls)
                    possible_adj_infls.append(inst_adj_infls)
                    possible_v_infls.append(inst_v_infls)
                
                # Use these to store number of occurrences
                noun_inflections_count = {
                        'N 1 0':0,'N 1 1':0,'N 1 6':0,'N 1 7':0,'N 1 8':0,
                        'N 2 0':0,'N 2 1':0,'N 2 2':0,'N 2 3':0,'N 2 4':0,'N 2 5':0,'N 2 6':0,'N 2 7':0,'N 2 8':0,'N 2 9':0,
                        'N 3 0':0,'N 3 1':0,'N 3 2':0,'N 3 3':0,'N 3 4':0,'N 3 6':0,'N 3 7':0,'N 3 8':0,'N 3 9':0,
                        'N 4 0':0,'N 4 1':0,'N 4 2':0,
                        'N 5 1':0
                        }
                adj_inflections_count = {
                        'ADJ 0 0':0,
                        'ADJ 1 0':0,'ADJ 1 1':0,'ADJ 1 2':0,'ADJ 1 3':0,'ADJ 1 4':0,'ADJ 1 5':0,
                        'ADJ 2 0':0,'ADJ 2 1':0,'ADJ 2 2':0,'ADJ 2 3':0,'ADJ 2 6':0,'ADJ 2 7':0,'ADJ 2 8':0,
                        'ADJ 3 0':0,'ADJ 3 1':0,'ADJ 3 2':0,'ADJ 3 3':0,'ADJ 3 6':0,
                        'ADJ 9 8':0,'ADJ 9 9':0
                        }
                v_inflections_count = {
                        'V 0 0':0,
                        'V 1 1':0,
                        'V 2 1':0,
                        'V 3 0':0,'V 3 1':0,'V 3 2':0,'V 3 3':0,'V 3 4':0,
                        'V 5 1':0,
                        'V 6 1':0,'V 6 3':0,
                        'V 7 1':0,'V 7 3':0,'V 7 4':0,
                        'V 8 1':0,
                        'V 9 8':0,'V 9 9':0
                        }
                
                # Now go by POS and compare declension/conjugation, and variant
                for inst_n_infls in possible_n_infls:
                    # Check each possible inflection of a given instance against the other inflections
                    for infl in inst_n_infls:
                        decl = infl.decl
                        var = infl.variant
                        s = 'N '+decl+' '+var
                        if s in noun_inflections_count.keys():
                            noun_inflections_count[s] += 1
                    
                for inst_adj_infls in possible_adj_infls:
                    # Check each possible inflection of a given instance against the other inflections
                    for infl in inst_adj_infls:
                        decl = infl.decl
                        var = infl.variant
                        s = 'ADJ '+decl+' '+var
                        if s in adj_inflections_count.keys():
                            adj_inflections_count[s] += 1
                for inst_v_infls in possible_v_infls:
                    # Check each possible inflection of a given instance against the other inflections
                    for infl in inst_v_infls:
                        conj = infl.conj
                        var = infl.variant
                        s = 'V '+conj+' '+var
                        if s in v_inflections_count.keys():
                            v_inflections_count[s] += 1
                for s,count in noun_inflections_count.items():
                    if count > 0:
                        f.write(s+'\t\t'+str(count)+'\n')
                for s,count in adj_inflections_count.items():
                    if count > 0:
                        f.write(s+'\t\t'+str(count)+'\n')
                for s,count in v_inflections_count.items():
                    if count > 0:
                        f.write(s+'\t\t'+str(count)+'\n')
    
    f.write('=====================================================\nTRASH BIN: \n---------------------\n')
    for w in bad_words:
        f.write(w+'\n')
    
    f.close()



def _format_entry_code():
    # Get Age, Area, Geography, Frequency, and Source codes
    age = input('''
Select AGE:
    X,   --              --  In use throughout the ages/unknown -- the default
    A,   --  archaic     --  Very early forms, obsolete by classical times
    B,   --  early       --  Early Latin, pre-classical, used for effect/poetry
    C,   --  classical   --  Limited to classical (~150 BC - 200 AD)
    D,   --  late        --  Late, post-classical (3rd-5th centuries)
    E,   --  later       --  Latin not in use in Classical times (6-10) Christian
    F,   --  medieval    --  Medieval (11th-15th centuries)
    G,   --  scholar     --  Latin post 15th - Scholarly/Scientific   (16-18)
    H    --  modern      --  Coined recently, words for new things (19-20)
> ''').upper()
    area = input('''
Select AREA:
    X,      --  All or none
    A,      --  Agriculture, Flora, Fauna, Land, Equipment, Rural
    B,      --  Biological, Medical, Body Parts  
    D,      --  Drama, Music, Theater, Art, Painting, Sculpture
    E,      --  Ecclesiastic, Biblical, Religious
    G,      --  Grammar, Retoric, Logic, Literature, Schools                     
    L,      --  Legal, Government, Tax, Financial, Political, Titles
    P,      --  Poetic
    S,      --  Science, Philosophy, Mathematics, Units/Measures
    T,      --  Technical, Architecture, Topography, Surveying
    W,      --  War, Military, Naval, Ships, Armor
    Y       --  Mythology
> ''').upper()
    geo = input('''
Select GEOGRAPHY:
    X,      --  All or none
    A,      --  Africa      
    B,      --  Britian     
    C,      --  China       
    D,      --  Scandinavia 
    E,      --  Egypt       
    F,      --  France, Gaul
    G,      --  Germany     
    H,      --  Greece      
    I,      --  Italy, Rome
    J,      --  India       
    K,      --  Balkans     
    N,      --  Netherlands
    P,      --  Persia      
    Q,      --  Near East   
    R,      --  Russia              
    S,      --  Spain, Iberia       
    U       --  Eastern Europe      
> ''').upper()
    freq = input('''
Select FREQUENCY: 
    X,    --              --  Unknown or unspecified
    A,    --  very freq   --  Very frequent, in all Elementry Latin books, top 1000+ words
    B,    --  frequent    --  Frequent, next 2000+ words
    C,    --  common      --  For Dictionary, in top 10,000 words
    D,    --  lesser      --  For Dictionary, in top 20,000 words
    E,    --  uncommon    --  2 or 3 citations
    F,    --  very rare   --  Having only single citation in OLD or L+S
    I,    --  inscription --  Only citation is inscription
    M,    --  graffiti    --  Presently not much used
    N     --  Pliny       --  Things that appear only in Pliny Natural History
> ''').upper()
    source = input('''
Select SOURCE:
    X,      --  General or unknown or too common to say
    A,      
    B,      --  C.H.Beeson, A Primer of Medieval Latin, 1925 (Bee)
    C,      --  Charles Beard, Cassell's Latin Dictionary 1892 (CAS)       
    D,      --  J.N.Adams, Latin Sexual Vocabulary, 1982 (Sex)
    E,      --  L.F.Stelten, Dictionary of Eccles. Latin, 1995 (Ecc)
    F,      --  Roy J. Deferrari, Dictionary of St. Thomas Aquinas, 1960 (DeF)
    G,      --  Gildersleeve + Lodge, Latin Grammar 1895 (G+L)
    H,      --  Collatinus Dictionary by Yves Ouvrard
    I,      --  Leverett, F.P., Lexicon of the Latin Language, Boston 1845
    J,     
    K,      --  Calepinus Novus, modern Latin, by Guy Licoppe (Cal)
    L,      --  Lewis, C.S., Elementary Latin Dictionary 1891
    M,      --  Latham, Revised Medieval Word List, 1980
    N,      --  Lynn Nelson, Wordlist
    O,      --  Oxford Latin Dictionary, 1982 (OLD)
    P,      --  Souter, A Glossary of Later Latin to 600 A.D., Oxford 1949
    Q,      --  Other, cited or unspecified dictionaries
    R,      --  Plater & White, A Grammar of the Vulgate, Oxford 1926
    S,      --  Lewis and Short, A Latin Dictionary, 1879 (L+S)
    T,      --  Found in a translation  --  no dictionary reference
    U,      --  Du Cange            
    V,      --  Vademecum in opus Saxonis - Franz Blatt (Saxo)
    W,      --  My personal guess   
    Y,      --  Temp special code
    Z       --  Sent by user --  no dictionary reference
            --  (Mostly John White of Blitz Latin)
> ''').upper()
    return age+' '+area+' '+geo+' '+freq+' '+source



def _format_noun_dictline_entry():
    noun_decls = \
'''
Select a declension:
   1   First declension nouns (-a -ae)
   2   Second declension nouns (-us/-um, -i)
   3   Third declension nouns (gen. -is)
   4   Fourth declension nouns (-us, -us)
   5   Fifth declension nouns (-es, -ei)
        dies diei  =>  di di
        res rei  =>  r r
   9   Abbreviations, indeclinable, not declined
> '''
    noun_decl1_vars = '''
Select a variant:
    1   Usual first declension (aqua, acquae => aqu aqu)
    6   First declension 'Greek' (epitome, epitomes => epitom epitom; musice, musices => music  music)
    7   (cometes, cometae => comet comet)
    8   (Archias, Archiae => Archi Archi, Aeneas, Aeneae => Aene  Aene)
> '''
    noun_decl2_vars = '''
Select a variant:
    1   Second declension nouns in "us"  amicus amici  =>  amic amic
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
> '''
    noun_decl3_vars = ''' 
Select a variant:
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
> '''
    noun_decl4_vars = ''' 
Select a variant:
    1   Fourth declension nouns M & F in "us", same as 0
        passus passus  =>  pass pass
        manus manus  =>  man man
    2   Fourth declension nouns N in "u"
        genu genus  =>  gen gen
        cornu cornus  =>  corn corn
> '''
    noun_decl9_vars = ''' 
Select a variant:
    8 For abbreviations, indeclinable, but a special case vis. capitalization
    9 For those other few nouns that are not declined, e.g., fas
> '''
    noun_decl_vars = ['',noun_decl1_vars,noun_decl2_vars,noun_decl3_vars,
    noun_decl4_vars,'','','','',noun_decl9_vars]

    decl = input(noun_decls)
    var = ''
    if decl in ['1','2','3','4','5','9']:
        var = input(noun_decl_vars[int(decl)])
        if decl == '1' and var not in ['1','6','7','8']:
            print("Unknown option. Quitting.")
            return 
        if decl == '2' and var not in ['1','2','3','4','5''6','7','8','9']:
            print("Unknown option. Quitting.")
            return 
        if decl == '3' and var not in ['1','2','3','4','6','7','8','9']:
            print("Unknown option. Quitting.")
            return 
        if decl == '4' and var not in ['1','2']:
            print("Unknown option. Quitting.")
            return 
    else:
        print("Unknown option. Quitting.")
        return 
    
    # Now we have the declension, we need the principal parts
    princ_parts_1 = input("Nominative first-person singular (first principal part) STEM: ")
    princ_parts_2 = input("Genitive first-person singular (second principal part) STEM: ")
    princ_parts = [princ_parts_1,princ_parts_2]

    # Get gender and kind
    noun_gend = input('''
Select gender:
          X,         --  all, none, or unknown
          M,         --  Masculine
          F,         --  Feminine
          N,         --  Neuter
          C          --  Common (masculine and/or feminine)
> ''').upper()
    noun_kind = input('''
Select noun kind: 
          X,            --  unknown, nondescript
          S,            --  Singular "only"           --  not really used
          M,            --  plural or Multiple "only" --  not really used
          A,            --  Abstract idea
          G,            --  Group/collective Name -- Roman(s)
          N,            --  proper Name
          P,            --  a Person
          T,            --  a Thing
          L,            --  Locale, name of country/city
          W             --  a place Where
> ''').upper()
    code = _format_entry_code()

    # FINAL OUTPUT
    print('\n\nDICTLINE ENTRY:')
    print(princ_parts[0]+' '+princ_parts[1]+'        N      '+decl+' '+var+' '+noun_gend+' '+noun_kind+'    '+code+' [senses]')


def _format_adj_dictline_entry():
    adj_decls = '''
Select a declension:
   0   Adjectives where i must be in stem (very rare)
   1   First/second declension adjectives (-us -a -um)
   2   An ADJ declension from the Greek - made up based on Greek nouns
         For the -os, -on adjectives, which OLD cites
         I am saying that -os is the ending for Common, not Masculine
         Like other ADJ 1 1, the stems are the same
         Plurals are the same as ADJ 1 1 
   3   Third declension adjectives (gen. -is; one, two, or three nom. endings)
   9   Indeclinable, abbreviations, etc
 > '''

    adj_decl1_vars = '''
Select a variant:
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
 > '''
    adj_decl2_vars = '''
Select a variant:
      1  -,  e,  -  the F part 
      2  -,  a,  -  the F part 
      3  es, es, es adjectives
      6  os, os, - 
      7  os, -,  -
      8  -,  -,  on 
 > '''
    adj_decl3_vars = '''
Select a variant:
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
 > '''
    adj_decl9_vars = '''
Select a variant:
      8  For ADJ abbreviations, indeclinable, but a special case vis. capitalization
      9  For adjective that is not declined                    
 > '''

    adj_decl_vars = ['',adj_decl1_vars,adj_decl2_vars,adj_decl3_vars,'','','','','',adj_decl9_vars]

    decl = input(adj_decls)
    var = ''
    if decl in ['0','1','2','3','9']:
        if decl == '0':
            var = '0'
        else:
            var = input(adj_decl_vars[int(decl)])
    else:
        print('Unknown option. Quitting.')
        return 

    # Now we have the declension, we need the principal parts
    princ_parts_1 = input("Nominative masculine first-person singular (first principal part) STEM: ").lower()
    princ_parts_2 = input("Genitive masculine first-person singular (second principal part) STEM: ").lower()
    #princ_parts_3 = input("") # Optional
    #princ_parts_4 = input("") # Optional
    princ_parts = [princ_parts_1,princ_parts_2]#,princ_parts_3,princ_parts_4]

    # Get adjective comparison
    adj_cmp = input('''
Select comparison type:
          X,         --  all, none, or unknown
          POS,       --  POSitive
          COMP,      --  COMParative
          SUPER      --  SUPERlative
> ''').upper()
    code = _format_entry_code()

    # FINAL OUTPUT
    print('\n\nDICTLINE ENTRY:')
    print(princ_parts[0]+' '+princ_parts[1]+'        ADJ   '+decl+' '+var+' '+adj_cmp+'    '+code+' [senses]')


def _format_v_dictline_entry():
    v_conjs = '''
Select a conjugation:
   1   First conjugation verbs (-are)
        voco vocare vocavi vocatus  =>  voc voc vocav vocat
        porto portave portavi portatus  =>  port port portav portat
   2   Second conjugation verbs (-ere)
        The characteristic 'e' is in the inflection, not carried in the stem
        moneo monere monui monitum  =>  mon mon monu monit
        habeo habere habui habitus  =>  hab hab habu habit
        deleo delere delevi deletus  =>  del del delev delet
        iubeo iubere iussi iussus  =>   iub iub iuss iuss
        video videre vidi visus  =>  vid vid vid vis
   3   Third AND fourth conjugation verbs (-ere, -ire)
 > '''
    v_conj3_vars = '''
Select a variant:
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
 > '''

    conj = input(v_conjs)
    var = ''
    if conj in ['1','2','3']:
        if conj in ['1','2']:
            # Set var to '1'
            var = '1'
        else:
            var = input(v_conj3_vars)
            if var not in ['1','2','3','4']:
                print("Unknown option. Quitting.")
                return 
    else:
        print("Unknown option. Quitting.")
        return 

    # Now we have the conjugation, we need the principal parts
    princ_parts_1 = input("First person singular present active indicative (first principal part) STEM: ").lower()
    princ_parts_2 = input("Present active infinitive (second principal part) STEM: ").lower()
    princ_parts_3 = input("First person singular perfect active indicate (third principal part) STEM: ").lower()
    princ_parts_4 = input("Perfect passive participle (fourth principal part) STEM: ").lower()
    princ_parts = [princ_parts_1,princ_parts_2,princ_parts_3,princ_parts_4]

    # Now get verb kind
    verb_kind = input('''
Select verb kind:
          X,         --  all, none, or unknown
          TO_BE,     --  only the verb TO BE (esse)
          TO_BEING,  --  compounds of the verb to be (esse)
          GEN,       --  verb taking the GENitive
          DAT,       --  verb taking the DATive  
          ABL,       --  verb taking the ABLative
          TRANS,     --  TRANSitive verb
          INTRANS,   --  INTRANSitive verb
          IMPERS,    --  IMPERSonal verb (implied subject 'it', 'they', 'God')
                     --  agent implied in action, subject in predicate
          DEP,       --  DEPonent verb
                     --  only passive form but with active meaning 
          SEMIDEP,   --  SEMIDEPonent verb (forms perfect as deponent) 
                     --  (perfect passive has active force)
          PERFDEF    --  PERFect DEFinite verb  
                     --  having only perfect stem, but with present force
> ''').upper()
    code = _format_entry_code()

    # TODO Get senses

    # FINAL OUTPUT
    print('\n\nDICTLINE ENTRY:')
    print(princ_parts[0]+' '+princ_parts[1]+' '+princ_parts[2]+' '+princ_parts[3]+' '+\
        '        V     '+conj+' '+var+' '+verb_kind+'  '+code+' [senses]')


def format_dictline_entry():
    """
    User-interactive method for making a DICTLINE.GEN entry from scratch
    Helps by listing options for each parameter so you don't have to
    memorize them or check the notes.txt doc.
    """
    # STRING DEFINITIONS
    parts_of_speech= \
'''
Select a part of speech: 
   N      Noun
   ADJ    Adjective
   V      Verb
> '''
    pos = input(parts_of_speech)
    if pos in ['N','n','noun']:
        _format_noun_dictline_entry()
    elif pos in ['ADJ','adj','Adj','adjective','A','a']:
        _format_adj_dictline_entry()
    elif pos in ['V','v','verb']:
        _format_v_dictline_entry()
    else:
        print("Unknown choice. Quitting.")
        return

def _process_vocab_list_opt(vocab_list,filt,full_info,markdown_fmt):
    """
    Method to parse the vocab_list argument to get_vocab_list
    Simply generates the full formatted vocab list for the file(s) given, 
    and subtracts those lines from the final version later
    """
    vocab_definitions = []

    if isinstance(vocab_list,list) or isinstance(vocab_list,tuple):
        for vl in vocab_list:
            vocab_definitions += _process_vocab_list_opt(vl,filt,full_info,markdown_fmt)  # Recursively go through lists
    else:
        if vocab_list == 'llpsi':
            print("Using vocab list LLPSI: Familia Romana")
            llpsi_fname = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/lingualatina_voclist.txt')
            with open(llpsi_fname,'r') as f:
                llpsi_text = ' '.join(f.readlines())
            vocab_definitions,_ = get_vocab_list(llpsi_text,filt,full_info,markdown_fmt,vocab_list=None)
        elif vocab_list[-4:] == '.txt':
            print("Creating vocab list from file {0}".format(vocab_list))
            with open(vocab_list,'r') as f:
                vl_text = ' '.join(f.readlines())
            vocab_definitions,_ = get_vocab_list(vl_text,filt,full_info,markdown_fmt,vocab_list=None)
    return vocab_definitions


def get_vocab_list(text, filt=MatchFilter(), full_info=False, markdown_fmt=False, vocab_list=None):
    """
    Take an arbitrarily long string (newlines and all) and process each word,
    then compile dictionary entries.

    vocab_list is used to remove well-known words. It can be a filename, a built-in vocab list from the following list:
        llpsi  -  Lingua Latina per se Illustrata: Familia Romana
    or it can be a list combining both.

    Return [definitions, missed words]
    """
    tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]', text)
    tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]
    tlist = list(set(tlist))

    vocab_definitions = []
    if vocab_list:
        vocab_definitions = _process_vocab_list_opt(vocab_list,filt,full_info,markdown_fmt)

    defns = set()
    missed = set()
    for w in tlist:
        # Patch the 'sum' problem for now...
        if w.replace('u','v').replace('i','j') in definitions.irreg_sum:
            defns.add('sum, esse, fui, futurus [irreg] to be, exist; (Medieval, in perfect tense) to go')
        else:
            ms = lookup.match_word(w)
            if len(ms) == 0:
                missed.add(w)
            # filt.remove_substantives(ms)
            wdefns = []
            for m in ms:
                if filt.check_dictline_word(m.dl_entry):

                    wdefns.append(lookup.get_dictionary_string(m, full_info=full_info, markdown_fmt=markdown_fmt))
            for wdefn in wdefns:
                if wdefn != '' and wdefn not in vocab_definitions:
                    defns.add(wdefn)

    defns_sort = sorted(defns)
    missed_sort = sorted(missed)
    return (defns_sort, missed_sort)


def find_example_sentences(text, word, word_filt=MatchFilter(), infl_filt=MatchFilter()):
    word_matches = lookup.match_word(word)

    if not word_matches:
        print("Word " + word + " doesn't seem to be in the dictionary. Check your spelling and try again.")
        return None
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    word_matches = [match for match in word_matches if word_filt.check_dictline_word(match.dl_entry)]
    if len(word_matches) > 1:
        print("Which word did you mean? ")
        for i, match in enumerate(word_matches):
            print(alphabet[i] + ") " + lookup.get_dictionary_string(match))
        chosen = False
        while not chosen:
            choice = input('WORD: ')
            if choice in alphabet[:len(word_matches)]:
                word_match = word_matches[alphabet.index(choice)]
                chosen = True
    else:
        word_match = word_matches[0]
    print("\nFinding example sentences of word: ", end='')
    print(lookup.get_dictionary_string(word_match))

    sentences = text.replace('\n', ' ').split('.')  # Try to roughly split into sentences
    matched_sentences = []
    for sentence in sentences:
        tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]', sentence)
        tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]

        for w in tlist:
            ms = lookup.match_word(w)
            for m in ms:
                if m.dl_entry == word_match.dl_entry and sentence.strip() + '.' not in matched_sentences:
                    matched_sentences.append(sentence.strip() + '.')

    print("Found %d sentences." % (len(matched_sentences)))
    return matched_sentences


def find_filtered_sentences(text, sentence_filt=MatchFilter(), strict=False):
    """
    Return a list of sentences for which all words pass through the match filter
    If strict is True, all matching inflections for each word must pass through the filter
    If False, at least one inflection must pass through
    """
    sentences = text.replace('\n', ' ').split('.')  # Roughly split into sentences
    matched_sentences = []
    for sentence in sentences:
        sentence_OK = True
        tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]', sentence)
        tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]

        for w in tlist:
            ms = lookup.match_word(w)
            for match in ms:
                entry = match.dl_entry
                sentence_OK &= sentence_filt.check_dictline_word(entry)

                ### Checking inflection
                pos = entry.pos
                infl = None
                if pos == 'V':
                    infl = definitions.build_inflection(part_of_speech=entry.pos, conj=entry.conj, ending=match.match_ending)
                elif pos in ['N', 'ADJ', 'PRON', 'NUM']:
                    infl = definitions.build_inflection(part_of_speech=entry.pos, decl=entry.decl, ending=match.match_ending)
                elif pos in ['PREP', 'PACK', 'TACKON', 'SUFFIX', 'PREFIX', 'X']:
                    infl = None
                elif pos in ['ADV', 'PREP', 'CONJ', 'INTERJ']:
                    infl = None
                if infl:
                    possible_infls = definitions.get_possible_inflections(infl, pos)

                    infls_OK = False
                    for minfl in possible_infls:
                        if strict:
                            infls_OK &= sentence_filt.check_inflection(minfl, pos)
                        else:
                            if sentence_filt.check_inflection(minfl, pos):
                                infls_OK = True
                    sentence_OK &= infls_OK
                    if not strict:
                        break
                ###

        if sentence and sentence_OK:
            matched_sentences.append(sentence)

    print("Found %d sentences." % (len(matched_sentences)))
    return matched_sentences


def get_glossary_from_file(fname,full_info=False,vocab_list=None):
    """
    Take a text file `fname`, process it for vocab words, and save them with
    proper formatting to a markdown file called '<fname>_vocab.md'

    vocab_list is used to remove well-known words. It can be a filename or a built-in vocab list from the following list:
        llpsi  -  Lingua Latina per se Illustrata: Familia Romana
    or it can be a list of vocab_list arguments, e.g. a list a filenames
    """
    # Filename to save to
    fname2 = fname[:fname.rfind('.')]+'_vocab.md'

    # TODO This needs some checks
    with open(fname,'r') as f:
        txt = f.readlines()
    txt = ''.join(txt)

    (vocab,missed) = get_vocab_list(txt,full_info=full_info,markdown_fmt=True,vocab_list=vocab_list)

    # Preprocess
    s = '  \n\n'  # Markdown newline character to separate lines
    voc1 = s.join(vocab)

    # Remove '|' line continuations
    stop = False
    idx_prev = len(voc1)
    while not stop:
        idx_bar = voc1.rfind('|',0,idx_prev)
        if idx_bar == -1:
            stop = True
        else:
            idx_newl = voc1.rfind('  \n\n',0,idx_bar)
            voc1 = voc1[ : idx_newl]+' '+voc1[idx_bar+1 : ]
            idx_prev = idx_newl

    with open(fname2,'w') as f:
        f.write(voc1)
    print("Saved vocab list to {0}.".format(fname2))

    print("\nIf you have pandoc, you can now convert this into e.g. an odt file with:")
    print("$ pandoc {0} -o tmp.html".format(fname2))
    print("$ pandoc tmp.html -o {0}".format(fname2[:fname2.rfind('.')]+'.odt'))


