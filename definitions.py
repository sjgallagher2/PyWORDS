# Python definitions useful for interpreting and working with dictionary entries, inflections, etc.

# Codes are used:
#   

# For convenience, here are dictionaries converting things
parts_of_speech = {
        'N'     : 'noun',
        'PRON'  : 'pronoun',
        'ADV'   : 'adverb',
        'ADJ'   : 'adjective',
        'NUM'   : 'numerical',
        'V'     : 'verb',
        'VPAR'  : 'verb participle',
        'INTERJ': 'interjection',
        'NUM'   : 'number',
        'CONJ'  : 'conjunction',
        'SUPINE' : 'supine',
        'PREP'  : 'preposition',
        'PACK'  : 'pack (internal use only)',
        'TACKON' : 'tackon (internal use only)',
        'PREFIX' : 'prefix (internal use only)',
        'SUFFIX' : 'suffix (internal use only)',
        'X'     : '' }
#TODO PACK, TACKON, PREFIX, SUFFIX
cases = {
        'NOM'   : 'nominative',
        'VOC'   : 'vocative',
        'GEN'   : 'genitive',
        'DAT'   : 'dative',
        'ACC'   : 'accusative',
        'LOC'   : 'locative',
        'ABL'   : 'ablative',
        'X'     : ''}
genders = {
        'M' : 'masculine',
        'F' : 'feminine',
        'N' : 'neuter',
        'C' : 'masculine/feminine',# (masc/fem depending on context)
        'X' : '' } 
persons = {
        '0' : '',
        '1' : 'first person',
        '2' : 'second person',
        '3' : 'third person'}
numbers = {
        'S'   : 'singular',
        'P'   : 'plural',
        'X'   : '' }
tenses = {
        'PRES'  : 'present',
        'IMPF'  : 'imperfect',
        'PERF'  : 'perfect',
        'FUT'   : 'future',
        'FUTP'  : 'future perfect',
        'PLUP'  : 'pluperfect',
        'INF'   : 'infinitive',
        'X'     : '' }
voices = {
        'ACTIVE'    : 'active',
        'PASSIVE'   : 'passive',
        'X'         : '' }
moods = {
        'IND' :'indicative',
        'SUB' :'subjunctive',
        'IMP' :'imperative',
        'INF' :'infinitive',
        'PPL' :'participle',
        'X'   :'' }
comparisons = {
        'POS'   : 'positive',
        'COMP'  : 'comparative',
        'SUPER' : 'superlative',
        'X'     : '' }

noun_declensions = {
        '1' : 'first declension',
        '2' : 'second declension',
        '3' : 'third declension',
        '4' : 'fourth declension',
        '5' : 'fifth declension',
        '9' : 'indeclinable or undeclined'}

verb_conjugations = {
        '0' : 'first conjugation',
        '1' : 'first conjugation',
        '2' : 'second conjugation',
        '3' : 'third conjugation',
        '5' : 'irregular',
        '6' : 'irregular',
        '7' : 'defective',
        '8' : 'irregular',
        '9' : 'indeclinable or undeclined' }

adj_declensions = {
        '0' : 'first/second declension',
        '1' : 'first/second declension',
        '2' : 'Greek declension',
        '3' : 'third declension',
        '9' : 'indeclinable or undeclined'}

noun_kinds = {
        'S' : 'singular only',
        'M' : 'plural or multiple only',
        'A' : 'abstract idea',
        'G' : 'group/collective name',
        'N' : 'proper name',
        'P' : 'person',
        'T' : 'thing',
        'L' : 'locale',
        'W' : 'where',
        'X' : '' }
pronoun_kinds = {
        'PERS'      : 'personal',
        'REL'       : 'relative',
        'REFLEX'    : 'reflexive',
        'DEMONS'    : 'demonstrative',
        'INTERR'    : 'interrogative',
        'INDEF'     : 'indefinite',
        'ADJECT'    : 'adjectival',
        'X'         : '' }

verb_kinds = {
        'TO_BE'     : 'to be',
        'TO_BEING'  : 'to be, compound',
        'GEN'       : 'takes genitive',
        'DAT'       : 'takes dative',
        'ABL'       : 'takes ablative',
        'TRANS'     : 'transitive',
        'INTRANS'   : 'intransitive',
        'IMPERS'    : 'impersonal',
        'DEP'       : 'deponent',
        'SEMIDEP'   : 'semideponent',
        'PERFDEF'   : 'perfect definite',
        'X'         : '' }

number_kinds = {
        'X': '',
        'CARD' : 'cardinal',
        'ORD' : 'ordinal',
        'DIST' : 'distributive',
        'ADVERB': 'numeral adverb'}

ages = {
        'A' : 'archaic',     # Very early forms, obsolete by classical times
        'B' :  'early',       # Early Latin, pre-classical, used for effect/poetry
        'C' :  'classical',   # Limited to classical (~150 BC - 200 AD)
        'D' :  'late',        # Late, post-classical (3rd-5th centuries)
        'E' :  'later',       # Latin not in use in Classical times (6-10) Christian
        'F' :  'medieval',    # Medieval (11th-15th centuries)
        'G' :  'scholar',     # Latin post 15th - Scholarly/Scientific   (16-18)
        'H' :  'modern',      # Coined recently, words for new things (19-20)
        'X' : 'common/unknown'}       # In use throughout the ages/unknown #the default
areas = {
        'A' : 'Agriculture, Flora, Fauna, Land, Equipment, Rural',
        'B' : 'Biological, Medical, Body Parts',
        'D' : 'Drama, Music, Theater, Art, Painting, Sculpture',
        'E' : 'Ecclesiastic, Biblical, Religious',
        'G' : 'Grammar, Retoric, Logic, Literature, Schools',
        'L' : 'Legal, Government, Tax, Financial, Political, Titles',
        'P' : 'Poetic',
        'S' : 'Science, Philosophy, Mathematics, Units/Measures',
        'T' : 'Technical, Architecture, Topography, Surveying',
        'W' : 'War, Military, Naval, Ships, Armor',
        'Y' : 'Mythology',
        'X' : '' }

geographies = {
        'A' : 'Africa',
        'B' : 'Britian',
        'C' : 'China',
        'D' : 'Scandinavia',
        'E' : 'Egypt',
        'F' : 'France, Gaul',
        'G' : 'Germany',
        'H' : 'Greece',
        'I' : 'Italy, Rome',
        'J' : 'India',
        'K' : 'Balkans',
        'N' : 'Netherlands',
        'P' : 'Persia',
        'Q' : 'Near East',
        'R' : 'Russia',
        'S' : 'Spain, Iberia',
        'U' : 'Eastern Europe',
        'X' : '' }

dict_frequencies = {
        'A' : 'very freq',   # Very frequent, in all Elementry Latin books, top 1000+ words
        'B' : 'frequent',    # Frequent, next 2000+ words
        'C' : 'common',      # For Dictionary, in top 10,000 words
        'D' : 'lesser',      # For Dictionary, in top 20,000 words
        'E' : 'uncommon',    # 2 or 3 citations
        'F' : 'very rare',   # Having only single citation in OLD or L+S
        'I' : 'inscription', # Only citation is inscription
        'M' : 'graffiti',    # Presently not much used
        'N' : 'Pliny',       # Things that appear only in Pliny Natural History
        'X' : 'unknown' }

inflection_frequencies = {
        'A' : 'most freq',   # Very frequent, the most common
        'B' : 'sometimes',   # sometimes, a not unusual VARIANT
        'C' : 'uncommon',    # occasionally seen
        'D' : 'infrequent',  # recognizable variant, but unlikely
        'E' : 'rare',        # for a few cases, very unlikely
        'F' : 'very rare',   # singular examples, 
        'I' : '',            # Presently not used
        'M' : '',            # Presently not used
        'N' : '',            # Presently not used
        'X' : 'unknown' }

source_types = {
        'X' : 'General or unknown or too common to say',
        'A' : '',
        'B' : 'C.H.Beeson, A Primer of Medieval Latin, 1925 (Bee)',
        'C' : 'Charles Beard, Cassell\'s Latin Dictionary 1892 (CAS)       ',
        'D' : 'J.N.Adams, Latin Sexual Vocabulary, 1982 (Sex)',
        'E' : 'L.F.Stelten, Dictionary of Eccles. Latin, 1995 (Ecc)',
        'F' : 'Roy J. Deferrari, Dictionary of St. Thomas Aquinas, 1960 (DeF)',
        'G' : 'Gildersleeve + Lodge, Latin Grammar 1895 (G+L)',
        'H' : 'Collatinus Dictionary by Yves Ouvrard',
        'I' : 'Leverett, F.P., Lexicon of the Latin Language, Boston 1845',
        'J' : '',
        'K' : 'Calepinus Novus, modern Latin, by Guy Licoppe (Cal)',
        'L' : 'Lewis, C.S., Elementary Latin Dictionary 1891',
        'M' : 'Latham, Revised Medieval Word List, 1980',
        'N' : 'Lynn Nelson, Wordlist',
        'O' : 'Oxford Latin Dictionary, 1982 (OLD)',
        'P' : 'Souter, A Glossary of Later Latin to 600 A.D., Oxford 1949',
        'Q' : 'Other, cited or unspecified dictionaries',
        'R' : 'Plater & White, A Grammar of the Vulgate, Oxford 1926',
        'S' : 'Lewis and Short, A Latin Dictionary, 1879 (L+S)',
        'T' : 'Found in a translation  # no dictionary reference',
        'U' : 'Du Cange',
        'V' : 'Vademecum in opus Saxonis - Franz Blatt (Saxo)',
        'W' : 'Whitaker\'s personal guess',
        'Y' : 'Temp special code',
        'Z' : 'Sent by user # no dictionary reference',
        'X' : 'General, unknown, or too common to say' }


#####################################
####### DICTIONARY ENTRIES ##########

class DictlineBaseEntry:
    '''
    dictline entry
    Base class for dictline entries, providing dictionary codes
    '''
    def __init__(self,pos,age,area,geog,freq,src,senses):
        self.pos=pos
        self.age=age
        self.area=area
        self.geog=geog
        self.freq=freq
        self.src=src
        self.senses=senses
    def get_part_of_speech(self):
        return parts_of_speech[self.pos]
    def get_age(self):
        return ages[self.age]
    def get_area(self):
        return areas[self.area]
    def get_geography(self):
        return geographies[self.geog]
    def get_frequency(self):
        return frequencies[self.frequency]
    def get_source(self):
        return source_types[self.src]
    def get_senses(self):
        return self.senses
        

class DictlineNounEntry (DictlineBaseEntry):
    '''
    dictline noun entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,decl,variant,gender,noun_kind,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.decl=decl # declension
        self.variant=variant # declension variant (see INFLECTS.LAT)
        self.gender=gender
        self.noun_kind=noun_kind

    def get_declension(self):
        return noun_declensions[self.decl]
    def get_gender(self):
        return genders[self.gender]
    def get_noun_kind(self):
        return noun_kinds[self.noun_kind]
    def __str__(self):
        return self.get_gender()+' '+self.get_declension()+' '+self.get_part_of_speech()+ \
                ' ('+self.get_noun_kind()+')'
class DictlineVerbEntry (DictlineBaseEntry):
    '''
    dictline verb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,conj,variant,verb_kind,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.conj=conj # conjugation
        self.variant=variant # conjugation variant (see INFLECTS.LAT)
        self.verb_kind=verb_kind
    def get_conjugation(self):
        return verb_conjugations[self.conj]
    def get_verb_kind(self):
        return verb_kinds[self.verb_kind]
    def __str__(self):
        return self.get_conjugation()+' '+self.get_part_of_speech()+\
                ' ('+self.get_verb_kind()+')'
class DictlineAdjectiveEntry (DictlineBaseEntry):
    '''
    dictline adjective entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,decl,variant,comparison,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.decl=decl # declension
        self.variant=variant # adjective variant (see INFLECTS.LAT)
        self.comparison=comparison
    def get_declension(self):
        return adj_declensions[self.decl]
    def get_comparison(self):
        return comparisons[self.comparison]
    def __str__(self):
        return self.get_declension()+' '+self.get_comparison()+' '+self.get_part_of_speech()
class DictlineAdverbEntry (DictlineBaseEntry):
    '''
    dictline adverb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,comparison,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.comparison=comparison
    def get_comparison(self):
        return comparisons[self.comparison]
    def __str__(self):
        if self.get_comparison():
            return self.get_comparison()+self.get_part_of_speech()
        else:
            return self.get_part_of_speech()
class DictlinePronounEntry (DictlineBaseEntry):
    '''
    dictline pronoun (and pack) entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,decl,variant,pronoun_kind,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.decl=decl # declension TODO 
        self.variant=variant 
        self.pronoun_kind=pronoun_kinds[pronoun_kind]
    def __str__(self):
        return self.get_part_of_speech()
class DictlineConjunctionEntry (DictlineBaseEntry):
    '''
    dictline conjunction entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
    def __str__(self):
        return self.get_part_of_speech()
class DictlineInterjectionEntry (DictlineBaseEntry):
    '''
    dictline interjection entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
    def __str__(self):
        return self.get_part_of_speech()
class DictlinePrepositionEntry (DictlineBaseEntry):
    '''
    dictline preposition entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,case,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.case = case
    def get_case(self):
        return cases[self.case]
    def __str__(self):
        if self.get_case():
            return self.get_part_of_speech()+' taking '+self.get_case()
        else:
            return self.get_part_of_speech()
class DictlineNumberEntry (DictlineBaseEntry):
    '''
    dictline number entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''
    def __init__(self,pos,decl,variant,number_kind,number,age,area,geog,freq,src,senses):
        super().__init__(pos,age,area,geog,freq,src,senses)
        self.decl=decl # declension
        self.variant=variant # adjective variant (see INFLECTS.LAT)
        self.number_kind=number_kind
        self.number = number

    def get_declension(self):
        return adj_declensions[self.decl]
    def get_number_kind(self):
        return number_kinds[self.number_kind]
    def get_number(self):
        return self.number
    def __str__(self):
        return self.get_declension()+' '+self.get_part_of_speech()+' (='+self.get_number()+\
                ', '+self.get_number_kind()


def build_dictline_entry(s):
    ps = s[:34].split()
    senses = s[34:]
    pos = parts_of_speech[ps[0]]
    if pos == 'noun':
        return DictlineNounEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],ps[9],senses)
    if pos == 'adjective':
        return DictlineAdjectiveEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'verb':
        return DictlineVerbEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'adverb':
        return DictlineAdverbEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],senses)
    if pos == 'conjunction':
        return DictlineConjunctionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],senses)
    if pos in ['pronoun','pack (internal use only)']:
        return DictlinePronounEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],senses)
    if pos == 'number':
        return DictlineNumberEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],ps[7],ps[8],ps[9],senses)
    if pos == 'preposition':
        return DictlinePrepositionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],ps[6],senses)
    if pos == 'interjection':
        return DictlineInterjectionEntry(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5],senses)



#####################################
######### INFLECTIONS ###############

# Inflection dictionaries include:
#   noun_inflections
#   verb_inflections
#   adjective_inflections
#   verb_participle_inflections
#   supine_inflections
#   pronoun_inflections
#   numeral_inflections
#   interjection_inflections
#   conjunction_inflections
#   preposition_inflections


# OR'd List of Endings
endings_list = ['', 'a', 'abam', 'abamini', 'abamur', 'abamus', 'abant', 'abantur', 'abar', 'abare', 'abaris',
        'abas', 'abat', 'abatis', 'abatur', 'abere', 'aberis', 'abimini', 'abimur', 'abimus', 'abis', 'abit',
        'abitis', 'abitur', 'abo', 'abor', 'abunt', 'abuntur', 'abus', 'ac', 'ad', 'ae', 'ai', 'am', 'amini',
        'amur', 'amus', 'an', 'anda', 'andae', 'andam', 'andarum', 'andas', 'ande', 'andi', 'andis', 'ando',
        'andorum', 'andos', 'andum', 'andus', 'ans', 'ant', 'antes', 'antia', 'antibus', 'anto', 'antor',
        'antur', 'ar', 'are', 'arem', 'aremini', 'aremur', 'aremus', 'arent', 'arentur', 'arer', 'arere',
        'areris', 'ares', 'aret', 'aretis', 'aretur', 'ari', 'arier', 'aris', 'arum', 'as', 'at', 'ate', 'atem',
        'ates', 'ati', 'atibus', 'atis', 'atium', 'ato', 'ator', 'atote', 'atum', 'atur', 'bam', 'bamini',
        'bamur', 'bamus', 'bant', 'bantur', 'bar', 'bare', 'baris', 'bas', 'bat', 'batis', 'batur', 'beris',
        'berit', 'bimini', 'bimur', 'bimus', 'bis', 'bit', 'bitis', 'bitur', 'bo', 'bor', 'bunt', 'buntur', 'd',
        'e', 'eam', 'eamini', 'eamur', 'eamus', 'eant', 'eantur', 'ear', 'eare', 'earis', 'eas', 'eat', 'eatis',
        'eatur', 'ebam', 'ebamini', 'ebamur', 'ebamus', 'ebant', 'ebantur', 'ebar', 'ebare', 'ebaris', 'ebas',
        'ebat', 'ebatis', 'ebatur', 'ebere', 'eberis', 'ebimini', 'ebimur', 'ebimus', 'ebis', 'ebit', 'ebitis',
        'ebitur', 'ebo', 'ebor', 'ebunt', 'ebuntur', 'ebus', 'ed', 'ei', 'eis', 'em', 'emini', 'emur', 'emus',
        'en', 'enda', 'endae', 'endam', 'endarum', 'endas', 'ende', 'endi', 'endis', 'endo', 'endorum', 'endos',
        'endum', 'endus', 'ens', 'ent', 'ente', 'entem', 'entes', 'enti', 'entia', 'entibus', 'entis', 'entium',
        'ento', 'entor', 'entum', 'entur', 'eo', 'eor', 'er', 'eram', 'eramus', 'erant', 'eras', 'erat',
        'eratis', 'ere', 'erem', 'eremini', 'eremur', 'eremus', 'erent', 'erentur', 'erer', 'erere', 'ereris',
        'eres', 'eret', 'eretis', 'eretur', 'eri', 'erier', 'erim', 'erimus', 'erint', 'eris', 'erit', 'eritis',
        'ero', 'erum', 'erunt', 'es', 'esse', 'est', 'este', 'estis', 'esto', 'estote', 'et', 'ete', 'etis',
        'eto', 'etor', 'etote', 'etur', 'eu', 'fore', 'forem', 'foremus', 'forent', 'fores', 'foret', 'foretis',
        'i', 'ia', 'iant', 'ias', 'iat', 'ib', 'ibam', 'ibamus', 'ibant', 'ibas', 'ibat', 'ibatis', 'ibus', 'ic',
        'id', 'iens', 'ier', 'ieri', 'ies', 'ih', 'ii', 'im', 'imini', 'imur', 'imus', 'int', 'ire', 'irem',
        'iremini', 'iremur', 'iremus', 'irent', 'irentur', 'irer', 'irere', 'ireris', 'ires', 'iret', 'iretis',
        'iretur', 'iri', 'irier', 'iris', 'is', 'isse', 'issem', 'issemus', 'issent', 'isses', 'isset',
        'issetis', 'isti', 'istis', 'it', 'ite', 'itis', 'ito', 'itor', 'itote', 'itur', 'iu', 'ium', 'ius',
        'jus', 'le', 'lem', 'lemus', 'lent', 'les', 'let', 'letis', 'm', 'mini', 'mur', 'mus', 'o', 'ob', 'obus',
        'oc', 'od', 'oe', 'om', 'on', 'or', 'orum', 'os', 're', 'rem', 'remini', 'remur', 'remus', 'rent',
        'rentur', 'rer', 'rere', 'reris', 'res', 'ret', 'retis', 'retur', 'ri', 'rier', 'ris', 's', 'se', 'sem',
        'semus', 'sent', 'ses', 'set', 'setis', 'setur', 't', 'te', 'tis', 'to', 'tor', 'tote', 'tur', 'u', 'ua',
        'ubus', 'uc', 'ud', 'ui', 'um', 'umus', 'un', 'unda', 'undae', 'undam', 'undarum', 'undas', 'unde',
        'undi', 'undis', 'undo', 'undorum', 'undos', 'undum', 'undus', 'unt', 'unte', 'untem', 'untes', 'unti',
        'untia', 'untibus', 'untis', 'untium', 'unto', 'untor', 'untur', 'ura', 'urae', 'uram', 'urarum', 'uras',
        'ure', 'uri', 'uris', 'uro', 'urorum', 'uros', 'urum', 'urus', 'us', 'uum', 'uus', 'yn', 'yos']

def interpret_inflection_key(s):
    ps = s.split()
    part_of_speech = parts_of_speech[ps[0]]
    if part_of_speech == 'noun':
        pos = parts_of_speech[ps[0]]
        decl = noun_declensions[ps[1]]
        # skip variant (for now)
        case = cases[ps[3]]
        number = numbers[ps[4]]
        gender = genders[ps[5]]
        # skip last two digits

        outs = case+' '+number+' form of '+gender+' '+ decl+' '+pos
        return outs
    elif part_of_speech == 'adjective':
        pos = parts_of_speech[ps[0]]
        decl = adj_declensions[ps[1]]
        # skip variant (for now)
        case = cases[ps[3]]
        number = numbers[ps[4]]
        gender = genders[ps[5]]
        compar = comparisons[ps[6]]

        outs = case+' '+number+' '+gender+' form of '+ decl+' '+compar +' '+pos
        return outs
    elif part_of_speech == 'verb':
        pos = parts_of_speech[ps[0]]
        conj = verb_conjugations[ps[1]]
        # skip variant (for now)
        tense = tenses[ps[3]]
        voice = voices[ps[4]]
        mood = moods[ps[5]]
        person = persons[ps[6]]
        number = numbers[ps[7]]

        outs = mood+' '+person+' '+tense+' '+number+' '+voice+' of '+conj+' '+pos

        return outs

    elif part_of_speech == 'verb participle':
        pos = parts_of_speech[ps[0]]
        conj = verb_conjugations[ps[1]]
        # skip variant (for now)
        case = cases[ps[3]]
        number = numbers[ps[4]]
        gender = genders[ps[5]]
        tense = tenses[ps[6]]
        voice = voices[ps[7]]+' participle'

        outs = case+' '+number+' '+gender+' '+tense+' '+voice+' of '+conj+' '+pos
        return outs
    elif part_of_speech == 'supine':
        pos = parts_of_speech[ps[0]]
        case = cases[ps[3]]
        number = numbers[ps[4]]
        gender = genders[ps[5]]

        outs = case+' '+number+' '+gender+' '+pos
        return outs
    # TODO
    elif part_of_speech == 'pronoun':
        outs = 'pronoun'
        return outs
    elif part_of_speech == 'number':
        outs = 'number'
        return outs
    elif part_of_speech in ['conjunction','interjection']:
        outs = parts_of_speech[ps[0]]
        return outs
    elif part_of_speech == 'preposition':
        pos = parts_of_speech[ps[0]]
        case = cases[ps[1]]
        outs = case+' '+pos
        return outs
    elif part_of_speech == 'adverb':
        pos = parts_of_speech[ps[0]]
        compare = comparisons[ps[1]]
        
        if compare:
            outs = compare+' '+pos
        else:
            outs = pos
        return outs
    else:
        print("Unknown part of speech: " + part_of_speech)

def reverse_ending_lookup(e):
    # Return a list of possible forms that use the ending given by e
    e = e.strip('-') # remove any dashes
    infls = []
    for entry,info in noun_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in verb_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in adjective_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in verb_participle_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in supine_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in pronoun_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in numeral_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in conjunction_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in adverb_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in interjection_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    for entry,info in preposition_inflections.items():
        if info['ending'] == e:
            infls.append(interpret_inflection_key(entry))
    return infls


class NounCode:
    '''Structural version of noun inflection codes, for easier searching'''
    def __init__(self,decl='',var='',case='',number='',gender=''):
        self.decl=decl
        self.var=var
        self.case=case
        self.number=number
        self.gender=gender
class AdjectiveCode:
    '''Structural version of adjective inflection codes, for easier searching'''
    def __init__(self,decl='',var='',case='',number='',gender='',comparison=''):
        self.decl=decl
        self.var=var
        self.case=case
        self.number=number
        self.gender=gender
        self.comparison=comparison
class VerbCode:
    '''Structural version of verb inflection codes, for easier searching'''
    def __init__(self,conj='',var='',tense='',voice='',mood='',person='',number=''):
        self.conj=conj
        self.var=var
        self.tense=tense
        self.voice=voice
        self.mood=mood
        self.person=person
        self.number=number
class VerbParticipleCode:
    '''Structural version of verb participle inflection codes, for easier searching'''
    def __init__(self,decl='',var='',case='',number='',gender='',tense='',voice=''):
        self.decl=decl
        self.var=var
        self.case=case
        self.number=number
        self.gender=gender
        self.tense=tense
        self.voice=voice
class PronounCode:
    '''Structural version of pronoun inflection codes, for easier searching'''
    def __init__(self,decl='',var='',case='',number='',gender=''):
        self.decl=decl
        self.var=var
        self.case=case
        self.number=number
        self.gender=gender
class NumberCode:
    '''Structural version of number inflection codes, for easier searching'''
    def __init__(self,decl='',var='',case='',number='',gender='',kind=''):
        self.decl=decl
        self.var=var
        self.case=case
        self.number=number
        self.gender=gender
        self.kind=kind



def get_matching_codes(code):
    '''
    Return a list of possible matching codes given the Code class with partial information
    '''
    if isinstance(code,NounCode):
        matches = [set(),set(),set(),set(),set()] # List of sets
        if code.decl:
            for infl in noun_inflections:
                if infl[2] == code.decl:
                    matches[0].add(infl)
        else:
            matches[0] = set(noun_inflections)
        if code.var:
            for infl in noun_inflections:
                if infl[4] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(noun_inflections)
        if code.case:
            for infl in noun_inflections:
                if code.case in infl[6:9]:
                    matches[2].add(infl)
        else:
            matches[2] = set(noun_inflections)
        if code.number:
            for infl in noun_inflections:
                if infl[10] == code.number:
                    matches[3].add(infl)
        else:
            matches[3] = set(noun_inflections)
        if code.gender:
            for infl in noun_inflections:
                if infl[12] == code.gender:
                    matches[4].add(infl)
        else:
            matches[4] = set(noun_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4])
    if isinstance(code,AdjectiveCode):
        matches = [set(),set(),set(),set(),set(),set()] # List of sets
        if code.decl:
            for infl in adjective_inflections:
                if infl[4] == code.decl:
                    matches[0].add(infl)
        else:
            matches[0] = set(adjective_inflections)
        if code.var:
            for infl in adjective_inflections:
                if infl[6] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(adjective_inflections)
        if code.case:
            for infl in adjective_inflections:
                if infl[8:11] == code.case:
                    matches[2].add(infl)
        else:
            matches[2] = set(adjective_inflections)
        if code.number:
            for infl in adjective_inflections:
                if infl[12] == code.number:
                    matches[3].add(infl)
        else:
            matches[3] = set(adjective_inflections)
        if code.gender:
            for infl in adjective_inflections:
                if infl[14] == code.gender:
                    matches[4].add(infl)
        else:
            matches[4] = set(adjective_inflections)
        if code.comparison:
            for infl in adjective_inflections:
                if code.comparison in infl[16:21] :
                    matches[5].add(infl)
        else:
            matches[5] = set(adjective_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4])
    if isinstance(code,VerbCode):
        matches = [set(),set(),set(),set(),set(),set(),set()] # List of sets
        if code.conj:
            for infl in verb_inflections:
                if infl[2] == code.conj:
                    matches[0].add(infl)
        else:
            matches[0] = set(verb_inflections)
        if code.var:
            for infl in verb_inflections:
                if infl[4] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(verb_inflections)
        if code.tense:
            for infl in verb_inflections:
                if code.tense in infl[6:10]:
                    matches[2].add(infl)
        else:
            matches[2] = set(verb_inflections)
        if code.voice:
            for infl in verb_inflections:
                if code.voice in infl[11:18]:
                    matches[3].add(infl)
        else:
            matches[3] = set(verb_inflections)
        if code.mood:
            for infl in verb_inflections:
                if code.mood in infl[19:22]:
                    matches[4].add(infl)
        else:
            matches[4] = set(verb_inflections)
        if code.person:
            for infl in verb_inflections:
                if infl[23] == code.person:
                    matches[5].add(infl)
        else:
            matches[5] = set(verb_inflections)
        if code.number:
            for infl in verb_inflections:
                if infl[25] == code.number:
                    matches[6].add(infl)
        else:
            matches[6] = set(verb_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4],matches[5],matches[6])
    if isinstance(code,VerbParticipleCode):
        matches = [set(),set(),set(),set(),set(),set(),set()] # List of sets
        if code.decl:
            for infl in verb_participle_inflections:
                if infl[5] == code.decl:
                    matches[0].add(infl)
        else:
            matches[0] = set(verb_participle_inflections)
        if code.var:
            for infl in verb_participle_inflections:
                if infl[7] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(verb_participle_inflections)
        if code.case:
            for infl in verb_participle_inflections:
                if infl[9:12] == code.case:
                    matches[2].add(infl)
        else:
            matches[2] = set(verb_participle_inflections)
        if code.number:
            for infl in verb_participle_inflections:
                if infl[13] == code.number:
                    matches[3].add(infl)
        else:
            matches[3] = set(verb_participle_inflections)
        if code.gender:
            for infl in verb_participle_inflections:
                if infl[15] == code.gender:
                    matches[4].add(infl)
        else:
            matches[4] = set(verb_participle_inflections)
        if code.tense:
            for infl in verb_participle_inflections:
                if code.tense in infl[17:21]:
                    matches[5].add(infl)
        else:
            matches[5] = set(verb_participle_inflections)
        if code.voice:
            for infl in verb_participle_inflections:
                if  code.voice in infl[22:30]:
                    matches[6].add(infl)
        else:
            matches[6] = set(verb_participle_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4])
    if isinstance(code,PronounCode):
        matches = [set(),set(),set(),set(),set(),set()] # List of sets
        if code.decl:
            for infl in pronoun_inflections:
                if infl[5] == code.decl:
                    matches[0].add(infl)
        else:
            matches[0] = set(pronoun_inflections)
        if code.var:
            for infl in pronoun_inflections:
                if infl[7] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(pronoun_inflections)
        if code.case:
            for infl in pronoun_inflections:
                if infl[9:12] == code.case:
                    matches[2].add(infl)
        else:
            matches[2] = set(pronoun_inflections)
        if code.number:
            for infl in pronoun_inflections:
                if infl[13] == code.number:
                    matches[3].add(infl)
        else:
            matches[3] = set(pronoun_inflections)
        if code.gender:
            for infl in pronoun_inflections:
                if infl[15] == code.gender:
                    matches[4].add(infl)
        else:
            matches[4] = set(pronoun_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4])
    if isinstance(code,NumberCode):
        matches = [set(),set(),set(),set(),set(),set()] # List of sets
        if code.decl:
            for infl in number_inflections:
                if infl[4] == code.decl:
                    matches[0].add(infl)
        else:
            matches[0] = set(number_inflections)
        if code.var:
            for infl in number_inflections:
                if infl[6] == code.var:
                    matches[1].add(infl)
        else:
            matches[1] = set(number_inflections)
        if code.case:
            for infl in number_inflections:
                if code.case in infl[8:11]:
                    matches[2].add(infl)
        else:
            matches[2] = set(number_inflections)
        if code.number:
            for infl in number_inflections:
                if infl[12] == code.number:
                    matches[3].add(infl)
        else:
            matches[3] = set(number_inflections)
        if code.gender:
            for infl in number_inflections:
                if infl[14] == code.gender:
                    matches[4].add(infl)
        else:
            matches[4] = set(number_inflections)
        if code.kind:
            for infl in number_inflections:
                if code.kind in infl[16:23]:
                    matches[5].add(infl)
        else:
            matches[5] = set(number_inflections)
        return matches[0].intersection(matches[1],matches[2],matches[3],matches[4],matches[5])
    return

def get_noun_case_endings(noun_code,frequency_limit='B'):
    '''
    Use code to find all case endings for a noun of given code information
    Code information should include:
        declension
        variant
        number
    If you include gender, be careful to use 'C' in place of 'M' or 'F' in most situations.
    
    The optional frequency_limit term puts a limit on how rare an inflection can be. 
    Poetic inflections should not be included in e.g. dictionary definitions. All inflections
    with frequency between 'A' and the frequency limit (inclusive) are used, any others
    are not included.
    '''
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    codes = get_matching_codes(noun_code)
    nom_endings = []
    gen_endings = []
    dat_endings = []
    acc_endings = []
    abl_endings = []
    for c in codes:
        infl = noun_inflections[c]
        if c[6:9] == 'NOM':
            f_idx = freqs.index(infl['frequency'])
            if f_idx <= flim_idx:
                nom_endings.append(infl)
        elif c[6:9] == 'GEN':
            f_idx = freqs.index(infl['frequency'])
            if f_idx <= flim_idx:
                gen_endings.append(infl)
        elif c[6:9] == 'DAT':
            f_idx = freqs.index(infl['frequency'])
            if f_idx <= flim_idx:
                dat_endings.append(infl)
        elif c[6:9] == 'ACC':
            f_idx = freqs.index(infl['frequency'])
            if f_idx <= flim_idx:
                acc_endings.append(infl)
        elif c[6:9] == 'ABL':
            f_idx = freqs.index(infl['frequency'])
            if f_idx <= flim_idx:
                abl_endings.append(infl)

    cases = {
            'nominative':nom_endings,
            'genitive':gen_endings,
            'dative':dat_endings,
            'accusative':acc_endings,
            'ablative':abl_endings
    }
    return cases

# Get singular indicative present tense first person ending, for dictionary formatting
def get_verb_sg_firstperson_ending(verb_conj,frequency_limit='B'):
    '''
    Get singular indicative present tense, first person ending, for dictionary formatting
    Note: Only conjugation is required, not variant
    '''
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    verb_code = VerbCode(conj=verb_conj,tense='PRES',mood='IND',voice='ACTIVE',person='1',number='S')
    codes = get_matching_codes(verb_code)
    for c in codes:
        f_idx = freqs.index(verb_inflections[c]['frequency'])
        if f_idx <= flim_idx:
            return verb_inflections[c]['ending']
    return None


    return endings
def get_verb_infinitive_ending(verb_conj,frequency_limit='B'):
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    endings=[]
    verb_code = VerbCode(conj=verb_conj,tense='PRES',mood='INF',voice='ACTIVE')
    codes = get_matching_codes(verb_code)
    for c in codes:
        f_idx = freqs.index(verb_inflections[c]['frequency'])
        if f_idx <= flim_idx:
            return verb_inflections[c]['ending']
    return None

def get_adj_sg_nom_endings(adj_decl,adj_var,frequency_limit='B'):
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    masc_ending = '' # masc, fem, and neut
    fem_ending = ''
    neut_ending = ''
    comm_ending = ''

    adj_code = AdjectiveCode(decl=adj_decl,var=adj_var,case='NOM',number='S')
    codes = get_matching_codes(adj_code)
    for c in codes:
        if c[14] == 'M':
            f_idx = freqs.index(adjective_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                masc_ending = adjective_inflections[c]['ending']
        elif c[14] == 'F':
            f_idx = freqs.index(adjective_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                fem_ending = adjective_inflections[c]['ending']
        elif c[14] == 'N':
            f_idx = freqs.index(adjective_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                neut_ending = adjective_inflections[c]['ending']
        elif c[14] == 'C':
            f_idx = freqs.index(adjective_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                comm_ending = adjective_inflections[c]['ending']
    if not fem_ending:
        adj_code.var = '0'
        codes = get_matching_codes(adj_code)
        for c in codes:
            if c[14] == 'F':
                f_idx = freqs.index(adjective_inflections[c]['frequency'])
                if f_idx <= flim_idx:
                    fem_ending = adjective_inflections[c]['ending']

    endings = {'masc':masc_ending,'fem':fem_ending,'neut':neut_ending}
    if comm_ending:
        endings['common'] = comm_ending
    return endings

def get_pronoun_sg_nom_endings(pronoun_decl,pronoun_var,frequency_limit='B'):
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    masc_ending = '' # masc, fem, and neut
    fem_ending = ''
    neut_ending = ''
    comm_ending = ''

    pron_code = PronounCode(decl=pronoun_decl,var=pronoun_var,case='NOM',number='S')
    codes = get_matching_codes(pron_code)
    for c in codes:
        if c[15] == 'M':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                masc_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'F':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                fem_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'N':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                neut_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'C':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                comm_ending = pronoun_inflections[c]['ending']
    if not fem_ending:
        pron_code.var = '0'
        codes = get_matching_codes(pron_code)
        for c in codes:
            if c[15] == 'F':
                f_idx = freqs.index(pronoun_inflections[c]['frequency'])
                if f_idx <= flim_idx:
                    fem_ending = pronoun_inflections[c]['ending']

    endings = {'masc':masc_ending,'fem':fem_ending,'neut':neut_ending}
    if comm_ending:
        endings['common'] = comm_ending
    return endings
def get_pronoun_pl_nom_endings(pronoun_decl,pronoun_var,frequency_limit='B'):
    freqs = ['X','A','B','C','D','E','F','I','M','N']
    flim_idx = freqs.index(frequency_limit)

    masc_ending = '' # masc, fem, and neut
    fem_ending = ''
    neut_ending = ''
    comm_ending = ''

    pron_code = PronounCode(decl=pronoun_decl,var=pronoun_var,case='NOM',number='P')
    codes = get_matching_codes(pron_code)
    for c in codes:
        if c[15] == 'M':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                masc_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'F':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                fem_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'N':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                neut_ending = pronoun_inflections[c]['ending']
        elif c[15] == 'C':
            f_idx = freqs.index(pronoun_inflections[c]['frequency'])
            if f_idx <= flim_idx:
                comm_ending = pronoun_inflections[c]['ending']
    if not fem_ending:
        pron_code.var = '0'
        codes = get_matching_codes(pron_code)
        for c in codes:
            if c[15] == 'F':
                f_idx = freqs.index(pronoun_inflections[c]['frequency'])
                if f_idx <= flim_idx:
                    fem_ending = pronoun_inflections[c]['ending']

    endings = {'masc':masc_ending,'fem':fem_ending,'neut':neut_ending}
    if comm_ending:
        endings['common'] = comm_ending
    return endings

# Inflections to endings

# Format example: 
#N    1 1 NOM S C  1 1 a     X A
# This means:
#   N       Noun
#   1 1     Declension 1, variant 1
#   NOM     Nominative
#   S       Singular
#   C       Common gender
#   1 1     ?, 1 character long
#   a       Ending
#   X A     Age and frequency

# This is gonna be bigger

adverb_inflections = {'ADV X 1 0':{'ending':'', 'age':'X','frequency':'A'},
        'ADV X 1 0':{'ending':'', 'age':'X', 'frequency':'A'},
        'ADV X 2 0':{'ending':'', 'age':'X', 'frequency':'A'},
        'ADV X 3 0':{'ending':'', 'age':'X', 'frequency':'A'},
        'ADV POS 1 0':{'ending':'', 'age':'X', 'frequency':'A'},
        'ADV COMP 1 0':{'ending':'', 'age':'X', 'frequency':'A'},
        'ADV SUPER 1 0':{'ending':'', 'age':'X', 'frequency':'A'}
}
preposition_inflections = {
        'PREP GEN 1 0':{'ending':'','age':'X','frequency':'A'},
        'PREP ACC 1 0':{'ending':'','age':'X','frequency':'A'},
        'PREP ABL 1 0':{'ending':'','age':'X','frequency':'A'}
}
conjunction_inflections = {
        'CONJ 1 0':{'ending':'','age':'X','frequency':'A'}
}
interjection_inflections = {
        'INTERJ 1 0':{'ending':'','age':'X','frequency':'A'}
}

noun_inflections = {
        'N 1 1 NOM S C 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 1 1 NOM S M 1 2' : {'ending':'as'  ,'age':'B', 'frequency':'D'} ,  # G&L 29 N1
        'N 1 1 VOC S C 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 1 1 GEN S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 1 GEN S C 2 2' : {'ending':'ai'  ,'age':'B', 'frequency':'C'} ,  # G&L 29 N2 A&G 43a  # Poetic
        'N 1 1 LOC S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 DAT S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 DAT S C 2 2' : {'ending':'ai'  ,'age':'B', 'frequency':'I'} ,  # G&L 29 N3
        'N 1 1 ABL S C 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 1 1 ABL S C 2 2' : {'ending':'ad'  ,'age':'B', 'frequency':'D'} ,  # G&L 29 N4
        'N 1 1 ACC S C 2 2' : {'ending':'am'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 NOM P C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 VOC P C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 GEN P C 2 4' : {'ending':'arum','age':'X', 'frequency':'A'} ,
        'N 1 0 GEN P C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'C'} ,  # G&L 29 R3
        'N 1 0 LOC P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 DAT P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 DAT P C 2 4' : {'ending':'abus','age':'D', 'frequency':'B'} ,  # G&L 29 R4
        'N 1 0 ABL P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 1 0 ABL P C 2 4' : {'ending':'abus','age':'D', 'frequency':'B'} ,  # G&L 29 R4
        'N 1 0 ACC P C 2 2' : {'ending':'as'  ,'age':'X', 'frequency':'A'} ,
        'N 1 6 NOM S C 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 1 6 VOC S C 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 1 6 GEN S C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 1 6 LOC S C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'D'} , # By rule  G&L 29 R 2, unlikely WAW
        'N 1 6 ABL S C 2 1' : {'ending':'e'  ,'age':'X', 'frequency':'A'} ,
        'N 1 6 ACC S C 2 2' : {'ending':'en'  ,'age':'X', 'frequency':'A'} ,
        'N 1 7 NOM S C 1 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 1 7 VOC S C 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 1 7 VOC S C 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'B'} ,
        'N 1 7 GEN S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 7 GEN S C 2 2' : {'ending':'ai'  ,'age':'B', 'frequency':'B'} ,   # G&L 29 N2 A&G 43a  # Poetic
        'N 1 7 LOC S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 7 ABL S C 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 1 7 ABL S C 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'B'} ,
        'N 1 7 ACC S C 2 2' : {'ending':'en'  ,'age':'X', 'frequency':'A'} ,
        'N 1 7 ACC S C 2 2' : {'ending':'am'  ,'age':'X', 'frequency':'B'} ,
        'N 1 8 NOM S M 1 2' : {'ending':'as'  ,'age':'X', 'frequency':'A'} ,
        'N 1 8 NOM S F 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,   # My guess from the Greek
        'N 1 8 VOC S C 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 1 8 GEN S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 8 GEN S C 2 2' : {'ending':'ai'  ,'age':'B', 'frequency':'B'} ,   # G&L 29 N2 A&G 43a  # Poetic
        'N 1 8 LOC S C 2 2' : {'ending':'ae'  ,'age':'X', 'frequency':'A'} ,
        'N 1 8 ACC S C 2 2' : {'ending':'an'  ,'age':'X', 'frequency':'A'} ,
        'N 1 8 ACC S C 2 2' : {'ending':'am'  ,'age':'X', 'frequency':'B'} ,
        'N 1 8 ABL S C 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 2 1 NOM S X 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,      # Hark 52
        'N 2 1 NOM S C 1 2' : {'ending':'os'  ,'age':'A', 'frequency':'B'} ,      # Hark 52
        'N 2 1 VOC S X 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,      
        'N 2 1 GEN S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,      
        'N 2 0 LOC S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,      
        'N 2 0 DAT S X 2 1' : {'ending':'o'   ,'age':'X', 'frequency':'A'} ,
        'N 2 0 ABL S X 2 1' : {'ending':'o'   ,'age':'X', 'frequency':'A'} ,
        'N 2 0 ACC S C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 1 ACC S N 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,      # GENDER exception for above
        'N 2 0 ACC S C 2 2' : {'ending':'om'  ,'age':'A', 'frequency':'B'} ,      # Hark 52
        'N 2 0 NOM P C 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,      # GENDER X  almost never 
        'N 2 1 NOM P N 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,      # A&G 48 a                
        'N 2 0 VOC P C 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,      # GENDER X  in plural
        'N 2 0 GEN P X 2 4' : {'ending':'orum','age':'X', 'frequency':'A'} ,
        'N 2 0 GEN P X 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'C'} ,      # G&L 33 R 4
        'N 2 0 LOC P X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,      # G&L 33 R 5
        'N 2 0 DAT P X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 2 0 ABL P X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 2 0 ACC P C 2 2' : {'ending':'os'  ,'age':'X', 'frequency':'A'} ,
        'N 2 1 ACC P N 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 2 2 NOM S N 1 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 2 NOM S N 1 2' : {'ending':'om'  ,'age':'A', 'frequency':'B'} ,      # Hark 52
        'N 2 2 VOC S N 1 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 2 GEN S N 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 2 2 ACC S N 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 0 NOM P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 2 0 VOC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 2 0 ACC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 2 3 NOM S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 3 VOC S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 3 GEN S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 2 4 NOM S C 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 2 4 VOC S C 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 2 4 NOM S N 1 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 4 VOC S N 1 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 4 GEN S X 2 1' : {'ending':'i'   ,'age':'D', 'frequency':'B'} ,
        'N 2 4 GEN S X 2 0' : {'ending':''    ,'age':'B', 'frequency':'A'} ,
        'N 2 4 ACC S X 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 5 NOM S M 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 2 5 VOC S M 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 5 GEN S M 2 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 5 GEN S M 2 1' : {'ending':'i'   ,'age':'E', 'frequency':'A'} ,  # Later Latin has filii
        'N 2 5 ACC S M 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 2 6 NOM S X 1 2' : {'ending':'os'  ,'age':'X', 'frequency':'A'} ,
        'N 2 6 VOC S X 1 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 2 6 GEN S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 2 6 ACC S C 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} ,
        'N 2 6 ACC S N 2 2' : {'ending':'os'  ,'age':'X', 'frequency':'A'} ,      
        'N 2 6 NOM P X 2 2' : {'ending':'oe'  ,'age':'B', 'frequency':'C'} ,    # G&L 66 N4
        'N 2 6 NOM P N 2 1' : {'ending':'e'   ,'age':'B', 'frequency':'C'} ,    # OLD cetus
        'N 2 6 ACC P N 2 1' : {'ending':'e'   ,'age':'B', 'frequency':'C'} ,    # OLD cetus
        'N 2 7 NOM S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 7 VOC S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 2 7 VOC S X 2 0' : {'ending':''    ,'age':'X', 'frequency':'D'} , #chelys L+S
        'N 2 7 GEN S X 2 1' : {'ending':'o'   ,'age':'X', 'frequency':'A'} ,
        'N 2 7 GEN S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'B'} ,
        'N 2 7 GEN S X 2 2' : {'ending':'yos' ,'age':'X', 'frequency':'D'} , #Hack for ys->yos
        'N 2 7 ACC S X 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} ,
        'N 2 7 ACC S X 2 2' : {'ending':'yn'  ,'age':'X', 'frequency':'D'} , #Hack for ys->yn (on)
        'N 2 7 ACC S X 2 1' : {'ending':'o'   ,'age':'X', 'frequency':'B'} ,
        'N 2 8 NOM S N 1 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} ,
        'N 2 8 VOC S N 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} ,
        'N 2 8 GEN S N 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 2 8 ACC S N 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} ,
        'N 2 9 NOM S C 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 2 9 VOC S C 2 1' : {'ending':'u'  ,'age':'X', 'frequency':'A'} ,
        'N 2 9 GEN S C 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 2 9 ACC S C 2 2' : {'ending':'un'  ,'age':'X', 'frequency':'A'} ,
        'N 3 0 NOM S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 3 0 VOC S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 3 0 GEN S X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 3 0 LOC S X 2 1' : {'ending':'i'   ,'age':'B', 'frequency':'A'} ,   # G&L 37 5 early like DAT
        'N 3 0 LOC S X 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,   # G&L 37 5 later like ABL
        'N 3 0 DAT S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 3 0 DAT S X 2 1' : {'ending':'e'   ,'age':'B', 'frequency':'B'} ,
        'N 3 0 ABL S C 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 3 1 ACC S C 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,
        'N 3 0 NOM P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 3 0 NOM P C 2 2' : {'ending':'is'  ,'age':'A', 'frequency':'B'} ,
        #N 3 0 NOM P C 2 3' : {'ending':'eis' ,'age':'A', 'frequency':'C'} ,   # Deleted for false positives (JFW)
        'N 3 0 VOC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 3 1 GEN P C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 3 1 GEN P C 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'B'} ,     # G&L 38 2
        'N 3 0 LOC P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        'N 3 0 DAT P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        'N 3 0 ABL P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        'N 3 1 ACC P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'C'} ,     # G&L 57 4
        'N 3 1 ACC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 3 2 ABL S N 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 3 2 ACC S N 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 3 2 NOM P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 2 VOC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 2 GEN P N 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 3 2 GEN P N 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'B'} ,     # G&L 38 2
        'N 3 2 ACC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 3 ABL S C 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'B'} ,     # G&L 57 2
        'N 3 3 ACC S C 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,
        'N 3 3 ACC S C 2 2' : {'ending':'im'  ,'age':'X', 'frequency':'B'} ,     # G&L 57 1
        'N 3 3 NOM P C 2 2' : {'ending':'is'  ,'age':'B', 'frequency':'C'} ,     # G&L 38 1, 57 4
        'N 3 3 GEN P C 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'A'} ,
        'N 3 3 GEN P C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'B'} ,     # G&L 57 3
        'N 3 3 ACC P C 2 2' : {'ending':'is'  ,'age':'B', 'frequency':'A'} ,     # G&L 57 5
        'N 3 3 ACC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'B'} ,
        'N 3 3 ACC P C 2 3' : {'ending':'eis' ,'age':'A', 'frequency':'C'} ,     # G&L 57 5
        'N 3 4 ABL S N 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 3 4 ACC S N 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 3 4 NOM P N 2 2' : {'ending':'ia'  ,'age':'X', 'frequency':'A'} ,
        'N 3 4 VOC P N 2 2' : {'ending':'ia'  ,'age':'X', 'frequency':'A'} ,
        'N 3 4 GEN P N 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'A'} ,
        'N 3 4 GEN P N 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'B'} ,     # G&L 57 3
        'N 3 4 ACC P N 2 2' : {'ending':'ia'  ,'age':'X', 'frequency':'A'} ,
        'N 3 6 GEN S C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 3 6 ACC S C 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 6 ACC S C 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'B'} ,
        'N 3 6 GEN S C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,  
        'N 3 6 ACC S C 2 2' : {'ending':'as'  ,'age':'X', 'frequency':'A'} ,
        'N 3 7 GEN S X 2 2' : {'ending':'os'  ,'age':'X', 'frequency':'A'} ,
        'N 3 7 ABL S N 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 3 7 ACC S X 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 7 ACC S X 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,
        'N 3 7 NOM P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 7 VOC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 7 GEN P X 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,  
        'N 3 7 ACC P C 2 2' : {'ending':'as'  ,'age':'X', 'frequency':'A'} ,  
        'N 3 7 ACC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,  
        #N 3 0 VOC S X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} ,
        'N 3 8 VOC S X 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 3 8 VOC S X 2 2' : {'ending':'eu'  ,'age':'X', 'frequency':'A'} ,   # G&L 65
        #N 3 0 GEN S X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 3 8 GEN S X 2 2' : {'ending':'os'  ,'age':'B', 'frequency':'C'} ,
        'N 3 8 GEN S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'B'} ,
        'N 3 8 ACC S X 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,
        'N 3 8 ACC S X 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'B'} ,
        'N 3 8 ACC S X 2 2' : {'ending':'en'  ,'age':'X', 'frequency':'B'} ,    # G&L 65
        'N 3 8 GEN P C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 3 8 GEN P C 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'B'} ,    
        'N 3 8 ACC P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        #N 3 0 NOM S X 1 0' : {'ending':'NULL','age':'X', 'frequency':'A'} ,
        'N 3 9 NOM S X 1 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} , #JFW, 1st stem
        #N 3 0 VOC S X 1 0' : {'ending':'NULL','age':'X', 'frequency':'A'} ,
        'N 3 9 GEN S X 2 2' : {'ending':'os'  ,'age':'X', 'frequency':'A'} ,
        #N 3 9 GEN S X 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'B'} , #duplicates N 3 0
        #N 3 0 DAT S X 2 1' : {'ending':'i'   ,'age':'D', 'frequency':'A'} ,
        'N 3 9 ABL S X 2 1' : {'ending':'i'   ,'age':'X', 'frequency':'A'} ,
        'N 3 9 ACC S X 1 2' : {'ending':'in'  ,'age':'X', 'frequency':'A'} , #JFW, 1st stem
        'N 3 9 ACC S X 2 2' : {'ending':'in'  ,'age':'X', 'frequency':'A'} ,
        'N 3 9 ACC S X 1 2' : {'ending':'on'  ,'age':'X', 'frequency':'B'} , #JFW, 1st stem
        'N 3 9 ACC S X 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'B'} ,
        'N 3 9 ACC S X 1 1' : {'ending':'a'   ,'age':'X', 'frequency':'B'} , #JFW, 1st stem
        'N 3 9 ACC S X 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'B'} ,
        #N 3 0 NOM P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        #N 3 0 NOM P C 2 2' : {'ending':'is'  ,'age':'A', 'frequency':'B'} ,
        #N 3 0 VOC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 3 9 NOM P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 9 VOC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 3 9 GEN P X 2 3' : {'ending':'ium' ,'age':'X', 'frequency':'A'} ,  
        'N 3 9 GEN P X 2 2' : {'ending':'on'  ,'age':'X', 'frequency':'A'} , #JFW, Greek GEN plural
        #N 3 0 DAT P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        #N 3 0 ABL P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        #N 3 0 ACC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 3 9 ACC P C 2 2' : {'ending':'is'  ,'age':'X', 'frequency':'A'} ,
        'N 3 9 ACC P C 2 2' : {'ending':'as'  ,'age':'X', 'frequency':'B'} ,  
        'N 3 9 ACC P N 2 1' : {'ending':'a'   ,'age':'X', 'frequency':'A'} ,
        'N 4 1 NOM S C 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 VOC S C 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 GEN S C 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 GEN S C 2 2' : {'ending':'os'  ,'age':'A', 'frequency':'C'} ,    # G&L 61 N 1
        'N 4 1 GEN S C 2 1' : {'ending':'i'   ,'age':'A', 'frequency':'B'} ,    # G&L 61 N 1
        'N 4 1 DAT S C 2 2' : {'ending':'ui'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 DAT S C 2 1' : {'ending':'u'   ,'age':'D', 'frequency':'C'} ,   # G&L 61
        'N 4 0 ABL S X 2 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 1 ACC S C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 NOM P C 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 NOM P C 2 3' : {'ending':'uus' ,'age':'D', 'frequency':'C'} ,   # G&L 61 N 3
        'N 4 1 VOC P C 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 VOC P C 2 3' : {'ending':'uus' ,'age':'D', 'frequency':'C'} ,   # G&L 61 N 3
        'N 4 0 GEN P X 2 3' : {'ending':'uum' ,'age':'X', 'frequency':'A'} ,
        'N 4 0 GEN P X 2 2' : {'ending':'um'  ,'age':'C', 'frequency':'C'} ,   # G&L 61 N 4
        'N 4 0 DAT P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        'N 4 0 DAT P X 2 4' : {'ending':'ubus','age':'B', 'frequency':'C'} ,   # G&L 61 R 1
        'N 4 0 ABL P X 2 4' : {'ending':'ibus','age':'X', 'frequency':'A'} ,
        'N 4 0 ABL P X 2 4' : {'ending':'ubus','age':'B', 'frequency':'C'} ,   # G&L 61 R 1
        'N 4 1 ACC P C 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 1 ACC P C 2 3' : {'ending':'uus' ,'age':'D', 'frequency':'C'} ,   # G&L 61 N 3
        'N 4 2 NOM S N 1 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 2 VOC S N 1 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 2 GEN S N 2 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 2 DAT S N 2 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 2 ACC S N 2 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 2 NOM P N 2 2' : {'ending':'ua'  ,'age':'X', 'frequency':'A'} ,
        'N 4 2 VOC P N 2 2' : {'ending':'ua'  ,'age':'X', 'frequency':'A'} ,
        'N 4 2 ACC P N 2 2' : {'ending':'ua'  ,'age':'X', 'frequency':'A'} ,
        'N 4 3 NOM S C 1 2' : {'ending':'us'  ,'age':'X', 'frequency':'A'} ,
        'N 4 3 VOC S C 1 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 3 GEN S C 2 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 3 DAT S C 2 1' : {'ending':'u'   ,'age':'X', 'frequency':'A'} ,
        'N 4 3 ACC S C 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,  # Stelten, Dict. of Eccl. Latin
        'N 4 3 ACC S C 2 2' : {'ending':'um'  ,'age':'X', 'frequency':'A'} ,  # Collins, Primer of Eccl. Latin
        'N 5 1 NOM S C 1 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 VOC S C 1 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 GEN S C 2 2' : {'ending':'ei'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 GEN S C 2 1' : {'ending':'e'   ,'age':'B', 'frequency':'B'} , # G&L 63 N
        'N 5 1 GEN S C 2 1' : {'ending':'i'   ,'age':'A', 'frequency':'D'} , # L+S (dii)
        'N 5 1 DAT S C 2 2' : {'ending':'ei'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 DAT S C 2 1' : {'ending':'e'   ,'age':'B', 'frequency':'C'} , # G&L 63 N2
        'N 5 1 DAT S C 2 1' : {'ending':'i'   ,'age':'B', 'frequency':'F'} , # G&L 63 N2
        'N 5 1 ABL S C 2 1' : {'ending':'e'   ,'age':'X', 'frequency':'A'} ,
        'N 5 1 ACC S C 2 2' : {'ending':'em'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 NOM P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 VOC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'} ,
        'N 5 1 GEN P C 2 4' : {'ending':'erum','age':'X', 'frequency':'A'} ,
        'N 5 1 DAT P C 2 4' : {'ending':'ebus','age':'X', 'frequency':'A'} ,
        'N 5 1 ABL P C 2 4' : {'ending':'ebus','age':'X', 'frequency':'A'} ,
        'N 5 1 ABL P C 2 3' : {'ending':'eis' ,'age':'X', 'frequency':'B'}, # JFW, eg 'cum plebeis' (Justinian)
        'N 5 1 ACC P C 2 2' : {'ending':'es'  ,'age':'X', 'frequency':'A'},
        'N 9 8 X   X X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'},
        'N 9 9 X   X X 1 0' : {'ending':''    ,'age':'X', 'frequency':'A'} }


# ADJECTIVES
adjective_inflections = {
        'ADJ 1 1 NOM S M POS   1 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 1 1 GEN S M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 1 DAT S M POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 0 ACC S M POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 0 ABL S M POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 1 VOC S M POS   1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 1 0 NOM P M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 0 GEN P M POS   2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'ADJ 1 0 DAT P X POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 1 0 ACC P M POS   2 2' : {'ending':'os','age':'X','frequency':'A'},
        'ADJ 1 0 ABL P X POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 1 0 VOC P M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 0 NOM S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 1 GEN S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 1 DAT S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 0 ACC S F POS   2 2' : {'ending':'am','age':'X','frequency':'A'},
        'ADJ 1 0 ABL S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 0 VOC S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 0 NOM P F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 0 GEN P F POS   2 4' : {'ending':'arum','age':'X','frequency':'A'},
        'ADJ 1 0 ACC P F POS   2 2' : {'ending':'as','age':'X','frequency':'A'},
        'ADJ 1 0 VOC P F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 1 NOM S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 1 GEN S N POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 1 DAT S N POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 1 ACC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 0 ABL S N POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 1 VOC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 0 NOM P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 0 GEN P N POS   2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'ADJ 1 0 ACC P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 0 VOC P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 0 0 NOM S C COMP  3 2' : {'ending':'or','age':'X','frequency':'A'},
        'ADJ 0 0 GEN S C COMP  3 4' : {'ending':'oris','age':'X','frequency':'A'},
        'ADJ 0 0 DAT S X COMP  3 3' : {'ending':'ori','age':'X','frequency':'A'},
        'ADJ 0 0 ACC S C COMP  3 4' : {'ending':'orem','age':'X','frequency':'A'},
        'ADJ 0 0 ABL S X COMP  3 3' : {'ending':'ore','age':'X','frequency':'A'},
        'ADJ 0 0 ABL S X COMP  3 3' : {'ending':'ori','age':'X','frequency':'A'},
        'ADJ 0 0 VOC S C COMP  3 2' : {'ending':'or','age':'X','frequency':'A'},
        'ADJ 0 0 NOM P C COMP  3 4' : {'ending':'ores','age':'X','frequency':'A'},
        'ADJ 0 0 GEN P X COMP  3 4' : {'ending':'orum','age':'X','frequency':'A'},
        'ADJ 0 0 DAT P X COMP  3 6' : {'ending':'oribus','age':'X','frequency':'A'},
        'ADJ 0 0 ACC P C COMP  3 4' : {'ending':'ores','age':'X','frequency':'A'},
        'ADJ 0 0 ABL P X COMP  3 6' : {'ending':'oribus','age':'X','frequency':'A'},
        'ADJ 0 0 VOC P C COMP  3 4' : {'ending':'ores','age':'X','frequency':'A'},
        'ADJ 0 0 NOM S N COMP  3 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 0 0 GEN S N COMP  3 4' : {'ending':'oris','age':'X','frequency':'A'},
        #ADJ0 0 DAT S N COMP 3' : {'ending':'3','age':'o','frequency':'i'},      
        'ADJ 0 0 ACC S N COMP 3 2' : {'ending':'us','age':'X','frequency':'A'},
        #ADJ0 0 ABL S N COMP 3' : {'ending':'3','age':'o','frequency':'e'},       X
        'ADJ 0 0 VOC S N COMP 3 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 0 0 NOM P N COMP 3 3' : {'ending':'ora','age':'X','frequency':'A'},
        #ADJ0 0 GEN P N COMP 3' : {'ending':'4','age':'o','frequency':'u'},m    
        #ADJ0 0 DAT P N COMP 3' : {'ending':'6','age':'o','frequency':'i'},bus    X
        'ADJ 0 0 ACC P N COMP 3 3' : {'ending':'ora','age':'X','frequency':'A'},
        #ADJ0 0 ABL P N COMP 3' : {'ending':'6','age':'o','frequency':'i'},bus   
        'ADJ 0 0 VOC P N COMP 3 3' : {'ending':'ora','age':'X','frequency':'A'},
        'ADJ 0 0 NOM S M SUPER 4 3' : {'ending':'mus','age':'X','frequency':'A'},
        'ADJ 0 0 GEN S M SUPER 4 2' : {'ending':'mi','age':'X','frequency':'A'},
        'ADJ 0 0 DAT S M SUPER 4 2' : {'ending':'mo','age':'X','frequency':'A'},
        'ADJ 0 0 ACC S M SUPER 4 3' : {'ending':'mum','age':'X','frequency':'A'},
        'ADJ 0 0 ABL S M SUPER 4 2' : {'ending':'mo','age':'X','frequency':'A'},
        'ADJ 0 0 VOC S M SUPER 4 2' : {'ending':'me','age':'X','frequency':'A'},
        'ADJ 0 0 NOM P M SUPER 4 2' : {'ending':'mi','age':'X','frequency':'A'},
        'ADJ 0 0 GEN P M SUPER 4 5' : {'ending':'morum','age':'X','frequency':'A'},
        'ADJ 0 0 DAT P X SUPER 4 3' : {'ending':'mis','age':'X','frequency':'A'},
        'ADJ 0 0 ACC P M SUPER 4 3' : {'ending':'mos','age':'X','frequency':'A'},
        'ADJ 0 0 ABL P X SUPER 4 3' : {'ending':'mis','age':'X','frequency':'A'},
        'ADJ 0 0 VOC P M SUPER 4 2' : {'ending':'mi','age':'X','frequency':'A'},
        'ADJ 0 0 NOM S F SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        'ADJ 0 0 GEN S F SUPER 4 3' : {'ending':'mae','age':'X','frequency':'A'},
        'ADJ 0 0 DAT S F SUPER 4 3' : {'ending':'mae','age':'X','frequency':'A'},
        'ADJ 0 0 ACC S F SUPER 4 3' : {'ending':'mam','age':'X','frequency':'A'},
        'ADJ 0 0 ABL S F SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        'ADJ 0 0 VOC S F SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        'ADJ 0 0 NOM P F SUPER 4 3' : {'ending':'mae','age':'X','frequency':'A'},
        'ADJ 0 0 GEN P F SUPER 4 5' : {'ending':'marum','age':'X','frequency':'A'},
        #ADJ0 0 DAT P F SUPER 4 3 mis       X
        'ADJ 0 0 ACC P F SUPER 4 3' : {'ending':'mas','age':'X','frequency':'A'},
        #ADJ 0 0 ABL P F SUPER 4' 3 mis       X
        'ADJ 0 0 VOC P F SUPER 4 3' : {'ending':'mae','age':'X','frequency':'A'},
        'ADJ 0 0 NOM S N SUPER 4 3' : {'ending':'mum','age':'X','frequency':'A'},
        'ADJ 0 0 GEN S N SUPER 4 2' : {'ending':'mi','age':'X','frequency':'A'},
        'ADJ 0 0 DAT S N SUPER 4 2' : {'ending':'mo','age':'X','frequency':'A'},
        'ADJ 0 0 ACC S N SUPER 4 3' : {'ending':'mum','age':'X','frequency':'A'},
        'ADJ 0 0 ABL S N SUPER 4 2' : {'ending':'mo','age':'X','frequency':'A'},
        'ADJ 0 0 VOC S N SUPER 4 3' : {'ending':'mum','age':'X','frequency':'A'},
        'ADJ 0 0 NOM P N SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        'ADJ 0 0 GEN P N SUPER 4 5' : {'ending':'morum','age':'X','frequency':'A'},
        #ADJ 0 0 DAT P N SUPER 4 3' : {'ending':'mis','age':'X','frequency':' '},       
        'ADJ 0 0 ACC P N SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        #ADJ 0 0 ABL P N SUPER 4 3' : {'ending':'mis','age':'','frequency':' '},       
        'ADJ 0 0 VOC P N SUPER 4 2' : {'ending':'ma','age':'X','frequency':'A'},
        'ADJ 1 2 NOM S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 1 2 GEN S M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 2 DAT S M POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 2 VOC S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},
        'ADJ 1 2 GEN S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 2 DAT S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 1 2 NOM S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 2 GEN S N POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 2 DAT S N POS   2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 1 2 ACC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 2 VOC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 3 NOM S M POS   1 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 1 3 GEN S X POS   2 3' : {'ending':'ius','age':'X','frequency':'A'},
        'ADJ 1 3 DAT S X POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 3 DAT S X POS   2 1' : {'ending':'o','age':'X','frequency':'D'},    # G&L  76 29
        'ADJ 1 3 VOC S M POS   1 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 1 3 NOM S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 3 ACC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 3 VOC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 4 NOM S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},
        'ADJ 1 4 GEN S X POS   2 3' : {'ending':'ius','age':'X','frequency':'A'},
        'ADJ 1 4 DAT S X POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 4 VOC S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 1 4 NOM S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 4 ACC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 4 VOC S N POS   2 2' : {'ending':'um','age':'X','frequency':'A'},
        'ADJ 1 5 NOM S M POS   1 2' : {'ending':'us','age':'X','frequency':'A'},
        'ADJ 1 5 GEN S X POS   2 2' : {'ending':'us','age':'X','frequency':'C'},     # G&L 76 1 R1
        'ADJ 1 5 GEN S X POS   2 4' : {'ending':'enus','age':'X','frequency':'A'},     # G&L 76 1 R1
        'ADJ 1 5 GEN S M POS   2 1' : {'ending':'i','age':'X','frequency':'D'},     # OLD
        'ADJ 1 5 DAT S X POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 1 5 DAT S M POS   2 1' : {'ending':'o','age':'X','frequency':'C'},     # A&G  113 N
        'ADJ 1 5 DAT S M POS   2 0' : {'ending':'','age':'B','frequency':'C'},   # G&L 76 2 N1
       #'ADJ 1 0 ACC S M POS   2 2' : {'ending':'u','age':'X','frequency':'A'},
       #'ADJ 1 0 ABL S M POS   2 2' : {'ending':'o','age':'X','frequency':'A'},    
        'ADJ 1 5 VOC S M POS   1 2' : {'ending':'us','age':'X','frequency':'A'},
       #'ADJ 1 5 NOM S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 1 5 GEN S F POS   2 2' : {'ending':'ae','age':'X','frequency':'D'},   # A&G  113 N
        'ADJ 1 5 DAT S F POS   2 2' : {'ending':'ae','age':'X','frequency':'D'},   # A&G  113 N
       #'ADJ1 0 ACC S F POS  2 2 am        X A
       #'ADJ1 0 ABL S F POS  2 1 a         X A
       #'ADJ1 0 VOC S F POS  2 1 a         X A
        'ADJ 1 5 NOM S N POS   2 2' : {'ending':'ud','age':'X','frequency':'A'},
        'ADJ 1 5 NOM S N POS   2 1' : {'ending':'d','age':'X','frequency':'E'},     # A&G  113 N
       #'ADJ 1 5 NOM S N POS   2 2' : {'ending':'ut','age':'X','frequency':'D'},     # OLD
        'ADJ 1 5 GEN S N POS   2 1' : {'ending':'s','age':'B','frequency':'E'},     # G&L  76 4 N
        'ADJ 1 5 GEN S N POS   2 1' : {'ending':'i','age':'X','frequency':'D'},     # OLD
        'ADJ 1 5 ACC S N POS   2 2' : {'ending':'ud','age':'X','frequency':'A'},
        'ADJ 1 5 ACC S N POS   2 1' : {'ending':'d','age':'B','frequency':'E'},     # G&L  76 4 N
        'ADJ 1 5 ACC S N POS   2 2' : {'ending':'ut','age':'X','frequency':'D'},     # OLD
       #ADJ1 0 ABL S N POS  2' 1 o         X A
        'ADJ 1 5 VOC S N POS   2 2' : {'ending':'ud','age':'X','frequency':'A'},
        'ADJ 1 5 ABL P N POS   2 3' : {'ending':'eis','age':'X','frequency':'A'},
        'ADJ 2 1 NOM S F X     1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 1 VOC S F X     1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 1 GEN S F X     2 2' : {'ending':'es','age':'X','frequency':'A'},
        'ADJ 2 1 LOC S F X     2 2' : {'ending':'es','age':'X','frequency':'A'},  # By rule  G&L 29 R 2, unlikely WAW
        'ADJ 2 1 DAT S F X     2 2' : {'ending':'ae','age':'X','frequency':'A'}, 
        'ADJ 2 1 ABL S F X     2 1' : {'ending':'e','age':'X','frequency':'A'}, 
        'ADJ 2 1 ACC S F X     2 2' : {'ending':'en','age':'X','frequency':'A'},
        'ADJ 2 2 NOM S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 2 2 GEN S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 2 DAT S F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 2 ACC S F POS   2 2' : {'ending':'am','age':'X','frequency':'A'},
        'ADJ 2 2 ABL S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 2 2 VOC S F POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 2 3 NOM S X X     1 2' : {'ending':'es','age':'X','frequency':'A'},
        'ADJ 2 3 VOC S X X     1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 3 VOC S X X     1 1' : {'ending':'a','age':'X','frequency':'B'},
        'ADJ 2 3 GEN S X X     2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 3 LOC S X X     2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 3 DAT S X X     2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 3 ABL S X X     2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 3 ABL S X X     2 1' : {'ending':'a','age':'X','frequency':'B'},
        'ADJ 2 3 ACC S X X     2 2' : {'ending':'en','age':'X','frequency':'A'},
        'ADJ 2 3 ACC S X X     2 2' : {'ending':'am','age':'X','frequency':'B'},
        'ADJ 2 6 NOM S C X     1 2' : {'ending':'os','age':'X','frequency':'A'},
        'ADJ 2 6 VOC S C X     1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 6 GEN S C X     2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 2 6 DAT S C X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 6 ABL S C X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 6 ACC S C X     2 2' : {'ending':'on','age':'X','frequency':'A'},
        'ADJ 2 7 NOM S M X     1 2' : {'ending':'os','age':'X','frequency':'A'},
        'ADJ 2 7 VOC S M X     1 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 2 7 GEN S M X     2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 2 7 DAT S M X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 7 ABL S M X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 7 ACC S M X     2 2' : {'ending':'on','age':'X','frequency':'A'},
        'ADJ 2 8 NOM S N X     1 2' : {'ending':'on','age':'X','frequency':'A'},
        'ADJ 2 8 VOC S N X     2 2' : {'ending':'on','age':'X','frequency':'A'},
        'ADJ 2 8 GEN S N X     2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 2 8 DAT S N X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 8 ABL S N X     2 1' : {'ending':'o','age':'X','frequency':'A'},
        'ADJ 2 8 ACC S N X     2 2' : {'ending':'on','age':'X','frequency':'A'},
        'ADJ 2 0 NOM P M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 2 0 GEN P M POS   2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'ADJ 2 0 DAT P X POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 2 0 ACC P M POS   2 2' : {'ending':'os','age':'X','frequency':'A'},
        'ADJ 2 0 ABL P X POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 2 0 VOC P M POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 2 0 NOM P F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 0 GEN P F POS   2 4' : {'ending':'arum','age':'X','frequency':'A'},
        'ADJ 2 0 ACC P F POS   2 2' : {'ending':'as','age':'X','frequency':'A'},
        'ADJ 2 0 VOC P F POS   2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'ADJ 2 0 NOM P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 2 0 GEN P N POS   2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'ADJ 2 0 ACC P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 2 0 VOC P N POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 3 1 NOM S X POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 0 GEN S X POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 0 DAT S X POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 3 0 ACC S C POS   2 2' : {'ending':'em','age':'X','frequency':'A'},
        'ADJ 3 0 ABL S X POS   2 1' : {'ending':'i','age':'X','frequency':'A'},
        'ADJ 3 0 ABL S X POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 1 VOC S X POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 0 NOM P C POS   2 2' : {'ending':'es','age':'X','frequency':'A'},
        'ADJ 3 0 GEN P X POS   2 3' : {'ending':'ium','age':'X','frequency':'A'},
        'ADJ 3 0 GEN P X POS   2 2' : {'ending':'um','age':'X','frequency':'A'}, # T  
        'ADJ 3 0 DAT P X POS   2 4' : {'ending':'ibus','age':'X','frequency':'A'},
        'ADJ 3 0 ACC P C POS   2 2' : {'ending':'es','age':'X','frequency':'A'},
        'ADJ 3 0 ACC P C POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 0 ABL P X POS   2 4' : {'ending':'ibus','age':'X','frequency':'A'},
        'ADJ 3 0 VOC P C POS   2 2' : {'ending':'es','age':'X','frequency':'A'},
        #ADJ3 1 NOM S N POS  1' 0           X
        #ADJ3 0 GEN S N POS  2' 2 is        X
        #ADJ3 0 DAT S N POS  2' 1 i         X
        'ADJ 3 1 ACC S N POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        #ADJ3 0 ABL S N POS  2' 1 i      
        #ADJ3 1 VOC S N POS  1' 0           X
        'ADJ 3 0 NOM P N POS   2 2' : {'ending':'ia','age':'X','frequency':'A'},
        #ADJ3 0 GEN P N POS  2' 3 ium    
        #ADJ3 0 DAT P N POS  2' 4 ibus      X
        'ADJ 3 0 ACC P N POS   2 2' : {'ending':'ia','age':'X','frequency':'A'},
        #ADJ3 0 ABL P N POS  2' 4 ibus      X
        'ADJ 3 0 VOC P N POS   2 2' : {'ending':'ia','age':'X','frequency':'A'},
        'ADJ 3 2 NOM S C POS   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 2 VOC S C POS   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 2 NOM S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 2 ACC S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 2 VOC S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 2 NOM P C POS   2 3' : {'ending':'eis','age':'F','frequency':'B'}, #Erasmus and neoLatin (JFW)
        'ADJ 3 2 ACC P C POS   2 3' : {'ending':'eis','age':'F','frequency':'B'}, #Erasmus and neoLatin (JFW) 
        'ADJ 3 3 NOM S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 3 VOC S M POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 3 NOM S F POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 3 VOC S F POS   2 2' : {'ending':'is','age':'X','frequency':'A'},
        'ADJ 3 3 NOM S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 3 ACC S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 3 VOC S N POS   2 1' : {'ending':'e','age':'X','frequency':'A'},
        'ADJ 3 6 NOM S X POS   1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 6 GEN S X POS   2 2' : {'ending':'os','age':'X','frequency':'A'},
        'ADJ 3 6 ACC S C POS   2 1' : {'ending':'a','age':'X','frequency':'A'},
        'ADJ 3 6 ACC S N POS   2 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 3 6 VOC S X POS   1 0' : {'ending':'','age':'X','frequency':'A'},
        'ADJ 3 6 ACC P C POS   2 2' : {'ending':'as','age':'X','frequency':'A'},
        'ADJ 9 8 X   X X X     1 0' : {'ending':'','age':'X','frequency':'A'},       
        'ADJ 9 9 X   X X X     1 0' : {'ending':'','age':'X','frequency':'A'} }

verb_inflections = {'V 1 1 PRES ACTIVE  IND 1 S 1 1': {'ending':'o','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IND 2 S 2 2' : {'ending':'as','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IND 3 S 2 2' : {'ending':'at','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IND 1 P 2 4' : {'ending':'amus','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IND 2 P 2 4' : {'ending':'atis','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IND 3 P 1 3' : {'ending':'ant','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 1 S 1 4' : {'ending':'abam','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 2 S 1 4' : {'ending':'abas','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'abat','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 1 P 1 6' : {'ending':'abamus','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 2 P 1 6' : {'ending':'abatis','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  IND 3 P 1 5' : {'ending':'abant','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 1 S 1 3' : {'ending':'abo','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 2 S 1 4' : {'ending':'abis','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 3 S 1 4' : {'ending':'abit','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 1 P 1 6' : {'ending':'abimus','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 2 P 1 6' : {'ending':'abitis','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IND 3 P 1 5' : {'ending':'abunt','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 1 S 3 1' : {'ending':'i','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 2 S 3 4' : {'ending':'isti','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 3 S 3 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 1 P 3 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 2 P 3 5' : {'ending':'istis','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 3 P 3 5' : {'ending':'erunt','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  IND 3 P 3 3' : {'ending':'ere','age':'X','frequency':'B'},
        'V 0 0 PLUP ACTIVE  IND 1 S 3 4' : {'ending':'eram','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  IND 2 S 3 4' : {'ending':'eras','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  IND 3 S 3 4' : {'ending':'erat','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  IND 1 P 3 6' : {'ending':'eramus','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  IND 2 P 3 6' : {'ending':'eratis','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  IND 3 P 3 5' : {'ending':'erant','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 1 S 3 3' : {'ending':'ero','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 2 S 3 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 3 S 3 4' : {'ending':'erit','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 1 P 3 6' : {'ending':'erimus','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 2 P 3 6' : {'ending':'eritis','age':'X','frequency':'A'},
        'V 0 0 FUTP ACTIVE  IND 3 P 3 5' : {'ending':'erint','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 1 S 1 2' : {'ending':'or','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 2 S 2 4' : {'ending':'aris','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 2 S 2 3' : {'ending':'are','age':'B','frequency':'B'},    # G+L 130 1
        'V 1 1 PRES PASSIVE IND 3 S 2 4' : {'ending':'atur','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 1 P 2 4' : {'ending':'amur','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 2 P 2 5' : {'ending':'amini','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IND 3 P 1 5' : {'ending':'antur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 1 S 1 4' : {'ending':'abar','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 2 S 1 6' : {'ending':'abaris','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 2 S 1 5' : {'ending':'abare','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 3 S 1 6' : {'ending':'abatur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 1 P 1 6' : {'ending':'abamur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 2 P 1 7' : {'ending':'abamini','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE IND 3 P 1 7' : {'ending':'abantur','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 1 S 1 4' : {'ending':'abor','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 2 S 1 6' : {'ending':'aberis','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 2 S 1 5' : {'ending':'abere','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 3 S 1 6' : {'ending':'abitur','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 1 P 1 6' : {'ending':'abimur','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 2 P 1 7' : {'ending':'abimini','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IND 3 P 1 7' : {'ending':'abuntur','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 1 S 1 2' : {'ending':'em','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 2 S 1 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 3 S 1 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 1 P 1 4' : {'ending':'emus','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 2 P 1 4' : {'ending':'etis','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  SUB 3 P 1 3' : {'ending':'ent','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 1 S 2 4' : {'ending':'arem','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 2 S 2 4' : {'ending':'ares','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 3 S 2 4' : {'ending':'aret','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 1 P 2 6' : {'ending':'aremus','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 2 P 2 6' : {'ending':'aretis','age':'X','frequency':'A'},
        'V 1 1 IMPF ACTIVE  SUB 3 P 2 5' : {'ending':'arent','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 1 S 3 4' : {'ending':'erim','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 2 S 3 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 3 S 3 4' : {'ending':'erit','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 1 P 3 6' : {'ending':'erimus','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 2 P 3 6' : {'ending':'eritis','age':'X','frequency':'A'},
        'V 0 0 PERF ACTIVE  SUB 3 P 3 5' : {'ending':'erint','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 1 S 3 5' : {'ending':'issem','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 2 S 3 5' : {'ending':'isses','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 3 S 3 5' : {'ending':'isset','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 1 P 3 7' : {'ending':'issemus','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 2 P 3 7' : {'ending':'issetis','age':'X','frequency':'A'},
        'V 0 0 PLUP ACTIVE  SUB 3 P 3 6' : {'ending':'issent','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 1 S 1 2' : {'ending':'er','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 2 S 1 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 2 S 1 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 3 S 1 4' : {'ending':'etur','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 1 P 1 4' : {'ending':'emur','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 2 P 1 5' : {'ending':'emini','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE SUB 3 P 1 5' : {'ending':'entur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 1 S 2 4' : {'ending':'arer','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 2 S 2 6' : {'ending':'areris','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'arere','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 3 S 2 6' : {'ending':'aretur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 1 P 2 6' : {'ending':'aremur','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 2 P 2 7' : {'ending':'aremini','age':'X','frequency':'A'},
        'V 1 1 IMPF PASSIVE SUB 3 P 2 7' : {'ending':'arentur','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  IMP 2 P 2 3' : {'ending':'ate','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'ato','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'ato','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IMP 2 P 2 5' : {'ending':'atote','age':'X','frequency':'A'},
        'V 1 1 FUT  ACTIVE  IMP 3 P 2 4' : {'ending':'anto','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IMP 2 S 2 3' : {'ending':'are','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE IMP 2 P 2 5' : {'ending':'amini','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IMP 2 S 2 4' : {'ending':'ator','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IMP 3 S 2 4' : {'ending':'ator','age':'X','frequency':'A'},
        'V 1 1 FUT  PASSIVE IMP 3 P 2 5' : {'ending':'antor','age':'X','frequency':'A'},
        'V 1 1 PRES ACTIVE  INF 0 X 2 3' : {'ending':'are','age':'X','frequency':'A'},
        'V 1 1 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE INF 0 X 2 3' : {'ending':'ari','age':'X','frequency':'A'},
        'V 1 1 PRES PASSIVE INF 0 X 2 5' : {'ending':'arier','age':'B','frequency':'B'},
        'V 2 1 PRES ACTIVE  IND 1 S 1 2' : {'ending':'eo','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IND 2 S 2 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IND 3 S 2 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IND 1 P 2 4' : {'ending':'emus','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IND 2 P 2 4' : {'ending':'etis','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IND 3 P 1 3' : {'ending':'ent','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 1 S 1 4' : {'ending':'ebam','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 2 S 1 4' : {'ending':'ebas','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'ebat','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 1 P 1 6' : {'ending':'ebamus','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 2 P 1 6' : {'ending':'ebatis','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  IND 3 P 1 5' : {'ending':'ebant','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 1 S 1 3' : {'ending':'ebo','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 2 S 1 4' : {'ending':'ebis','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 3 S 1 4' : {'ending':'ebit','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 1 P 1 6' : {'ending':'ebimus','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 2 P 1 6' : {'ending':'ebitis','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IND 3 P 1 5' : {'ending':'ebunt','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 1 S 1 3' : {'ending':'eor','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 2 S 2 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 2 S 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 3 S 2 4' : {'ending':'etur','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 1 P 2 4' : {'ending':'emur','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 2 P 2 5' : {'ending':'emini','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IND 3 P 1 5' : {'ending':'entur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 1 S 1 4' : {'ending':'ebar','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 2 S 1 6' : {'ending':'ebaris','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 2 S 1 5' : {'ending':'ebare','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 3 S 1 6' : {'ending':'ebatur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 1 P 1 6' : {'ending':'ebamur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 2 P 1 7' : {'ending':'ebamini','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE IND 3 P 1 7' : {'ending':'ebantur','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 1 S 1 4' : {'ending':'ebor','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 2 S 1 6' : {'ending':'eberis','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 2 S 1 5' : {'ending':'ebere','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 3 S 1 6' : {'ending':'ebitur','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 1 P 1 6' : {'ending':'ebimur','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 2 P 1 7' : {'ending':'ebimini','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IND 3 P 1 7' : {'ending':'ebuntur','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 1 S 1 3' : {'ending':'eam','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 2 S 1 3' : {'ending':'eas','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 3 S 1 3' : {'ending':'eat','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 1 P 1 5' : {'ending':'eamus','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 2 P 1 5' : {'ending':'eatis','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  SUB 3 P 1 4' : {'ending':'eant','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 1 S 2 4' : {'ending':'erem','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 2 S 2 4' : {'ending':'eres','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 3 S 2 4' : {'ending':'eret','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 1 P 2 6' : {'ending':'eremus','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 2 P 2 6' : {'ending':'eretis','age':'X','frequency':'A'},
        'V 2 1 IMPF ACTIVE  SUB 3 P 2 5' : {'ending':'erent','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 1 S 1 3' : {'ending':'ear','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 2 S 1 5' : {'ending':'earis','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 2 S 1 4' : {'ending':'eare','age':'B','frequency':'B'},
        'V 2 1 PRES PASSIVE SUB 3 S 1 5' : {'ending':'eatur','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 1 P 1 5' : {'ending':'eamur','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 2 P 1 6' : {'ending':'eamini','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE SUB 3 P 1 6' : {'ending':'eantur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 1 S 2 4' : {'ending':'erer','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 2 S 2 6' : {'ending':'ereris','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'erere','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 3 S 2 6' : {'ending':'eretur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 1 P 2 6' : {'ending':'eremur','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 2 P 2 7' : {'ending':'eremini','age':'X','frequency':'A'},
        'V 2 1 IMPF PASSIVE SUB 3 P 2 7' : {'ending':'erentur','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  IMP 2 P 2 3' : {'ending':'ete','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'eto','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'eto','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IMP 2 P 2 5' : {'ending':'etote','age':'X','frequency':'A'},
        'V 2 1 FUT  ACTIVE  IMP 3 P 2 4' : {'ending':'ento','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IMP 2 S 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE IMP 2 P 2 5' : {'ending':'emini','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IMP 2 S 2 4' : {'ending':'etor','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IMP 3 S 2 4' : {'ending':'etor','age':'X','frequency':'A'},
        'V 2 1 FUT  PASSIVE IMP 3 P 2 5' : {'ending':'entor','age':'X','frequency':'A'},
        'V 2 1 PRES ACTIVE  INF 0 X 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 2 1 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE INF 0 X 2 3' : {'ending':'eri','age':'X','frequency':'A'},
        'V 2 1 PRES PASSIVE INF 0 X 2 5' : {'ending':'erier','age':'B','frequency':'B'},
        'V 3 0 PRES ACTIVE  IND 1 S 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IND 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IND 1 P 2 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IND 2 P 2 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 1 S 1 4' : {'ending':'ebam','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 2 S 1 4' : {'ending':'ebas','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'ebat','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 1 P 1 6' : {'ending':'ebamus','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 2 P 1 6' : {'ending':'ebatis','age':'X','frequency':'A'},
        'V 3 0 IMPF ACTIVE  IND 3 P 1 5' : {'ending':'ebant','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 1 S 1 2' : {'ending':'am','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 2 S 1 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 3 S 1 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 1 P 1 4' : {'ending':'emus','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 2 P 1 4' : {'ending':'etis','age':'X','frequency':'A'},
        'V 3 0 FUT  ACTIVE  IND 3 P 1 3' : {'ending':'ent','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE IND 1 S 1 2' : {'ending':'or','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE IND 2 S 2 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE IND 2 S 2 3' : {'ending':'ere','age':'B','frequency':'C'},  # G+L 130 1
        'V 3 1 PRES PASSIVE IND 3 S 2 4' : {'ending':'itur','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE IND 1 P 2 4' : {'ending':'imur','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE IND 2 P 2 5' : {'ending':'imini','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE IND 3 P 1 5' : {'ending':'untur','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 1 S 1 4' : {'ending':'ebar','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 2 S 1 6' : {'ending':'ebaris','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 2 S 1 5' : {'ending':'ebare','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 3 S 1 6' : {'ending':'ebatur','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 1 P 1 6' : {'ending':'ebamur','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 2 P 1 7' : {'ending':'ebamini','age':'X','frequency':'A'},
        'V 3 0 IMPF PASSIVE IND 3 P 1 7' : {'ending':'ebantur','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 1 S 1 2' : {'ending':'ar','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 2 S 1 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 2 S 1 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 3 S 1 4' : {'ending':'etur','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 1 P 1 4' : {'ending':'emur','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 2 P 1 5' : {'ending':'emini','age':'X','frequency':'A'},
        'V 3 0 FUT  PASSIVE IND 3 P 1 5' : {'ending':'entur','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 1 S 1 2' : {'ending':'am','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 2 S 1 2' : {'ending':'as','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 3 S 1 2' : {'ending':'at','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 1 P 1 4' : {'ending':'amus','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 2 P 1 4' : {'ending':'atis','age':'X','frequency':'A'},
        'V 3 0 PRES ACTIVE  SUB 3 P 1 3' : {'ending':'ant','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 1 S 2 4' : {'ending':'erem','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 2 S 2 4' : {'ending':'eres','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 3 S 2 4' : {'ending':'eret','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 1 P 2 6' : {'ending':'eremus','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 2 P 2 6' : {'ending':'eretis','age':'X','frequency':'A'},
        'V 3 1 IMPF ACTIVE  SUB 3 P 2 5' : {'ending':'erent','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 1 S 1 2' : {'ending':'ar','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 2 S 1 4' : {'ending':'aris','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 2 S 1 3' : {'ending':'are','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 3 S 1 4' : {'ending':'atur','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 1 P 1 4' : {'ending':'amur','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 2 P 1 5' : {'ending':'amini','age':'X','frequency':'A'},
        'V 3 0 PRES PASSIVE SUB 3 P 1 5' : {'ending':'antur','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 1 S 2 4' : {'ending':'erer','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 2 S 2 6' : {'ending':'ereris','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'erere','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 3 S 2 6' : {'ending':'eretur','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 1 P 2 6' : {'ending':'eremur','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 2 P 2 7' : {'ending':'eremini','age':'X','frequency':'A'},
        'V 3 1 IMPF PASSIVE SUB 3 P 2 7' : {'ending':'erentur','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  IMP 2 S 2 0' : {'ending':'','age':'X','frequency':'A'},# For stem in -c 
        'V 3 1 PRES ACTIVE  IMP 2 P 2 3' : {'ending':'ite','age':'X','frequency':'A'},
        'V 3 1 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 3 1 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 3 1 FUT  ACTIVE  IMP 2 P 2 5' : {'ending':'itote','age':'X','frequency':'A'},
        'V 3 1 FUT  ACTIVE  IMP 3 P 2 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE IMP 2 S 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE IMP 2 P 2 5' : {'ending':'imini','age':'X','frequency':'A'},
        'V 3 1 FUT  PASSIVE IMP 2 S 2 4' : {'ending':'itor','age':'X','frequency':'A'},
        'V 3 1 FUT  PASSIVE IMP 3 S 2 4' : {'ending':'itor','age':'X','frequency':'A'},
        'V 3 1 FUT  PASSIVE IMP 3 P 2 5' : {'ending':'untor','age':'X','frequency':'A'},
        'V 3 1 PRES ACTIVE  INF 0 X 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 3 1 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE INF 0 X 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'V 3 1 PRES PASSIVE INF 0 X 2 3' : {'ending':'ier','age':'B','frequency':'B'},
        'V 3 2 PRES ACTIVE  IND 2 S 1 1' : {'ending':'s','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  IND 3 S 1 1' : {'ending':'t','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  IND 1 P 1 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  IND 2 P 1 3' : {'ending':'tis','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE IND 2 S 2 3' : {'ending':'ris','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE IND 2 S 2 2' : {'ending':'re','age':'B','frequency':'C'},
        'V 3 2 PRES PASSIVE IND 3 S 1 3' : {'ending':'tur','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 1 S 2 3' : {'ending':'rem','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 2 S 2 3' : {'ending':'res','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 3 S 2 3' : {'ending':'ret','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 1 P 2 5' : {'ending':'remus','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 2 P 2 5' : {'ending':'retis','age':'X','frequency':'A'},
        'V 3 2 IMPF ACTIVE  SUB 3 P 2 4' : {'ending':'rent','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 1 S 2 3' : {'ending':'rer','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'reris','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 2 S 2 4' : {'ending':'rere','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 3 S 2 5' : {'ending':'retur','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 1 P 2 5' : {'ending':'remur','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 2 P 2 6' : {'ending':'remini','age':'X','frequency':'A'},
        'V 3 2 IMPF PASSIVE SUB 3 P 2 6' : {'ending':'rentur','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  IMP 2 S 1 0' : {'ending':'','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  IMP 2 P 1 2' : {'ending':'te','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE IMP 2 S 1 2' : {'ending':'re','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE IMP 2 P 1 5' : {'ending':'imini','age':'X','frequency':'A'},
        'V 3 2 FUT  ACTIVE  IMP 2 S 1 2' : {'ending':'to','age':'X','frequency':'A'},
        'V 3 2 FUT  ACTIVE  IMP 3 S 1 2' : {'ending':'to','age':'X','frequency':'A'},
        'V 3 2 FUT  ACTIVE  IMP 2 P 1 4' : {'ending':'tote','age':'X','frequency':'A'},
        'V 3 2 FUT  ACTIVE  IMP 3 P 1 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 3 2 FUT  PASSIVE IMP 2 S 1 3' : {'ending':'tor','age':'X','frequency':'A'},
        'V 3 2 FUT  PASSIVE IMP 3 S 1 3' : {'ending':'tor','age':'X','frequency':'A'},
        'V 3 2 FUT  PASSIVE IMP 3 P 1 5' : {'ending':'untor','age':'X','frequency':'A'},
        'V 3 2 PRES ACTIVE  INF 0 X 2 2' : {'ending':'re','age':'X','frequency':'A'},
        'V 3 2 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE INF 0 X 2 2' : {'ending':'ri','age':'X','frequency':'A'},
        'V 3 2 PRES PASSIVE INF 0 X 2 4' : {'ending':'rier','age':'B','frequency':'B'}, 
        'V 3 3 PRES ACTIVE  IND 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 3 3 PRES ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 3 3 PRES ACTIVE  IND 1 P 2 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 3 3 PRES ACTIVE  IND 2 P 2 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 3 3 PRES PASSIVE IND 2 S 2 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 3 3 PRES PASSIVE IND 3 S 2 4' : {'ending':'itur','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 1 S 1 4' : {'ending':'erem','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 2 S 1 4' : {'ending':'eres','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 3 S 1 4' : {'ending':'eret','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 1 P 1 6' : {'ending':'eremus','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 2 P 1 6' : {'ending':'eretis','age':'X','frequency':'A'},
        'V 3 3 IMPF ACTIVE  SUB 3 P 1 5' : {'ending':'erent','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 1 S 2 4' : {'ending':'erer','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 2 S 2 6' : {'ending':'ereris','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 3 S 2 6' : {'ending':'eretur','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 1 P 2 6' : {'ending':'eremur','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 2 P 2 7' : {'ending':'eremini','age':'X','frequency':'A'},
        'V 3 3 IMPF PASSIVE SUB 3 P 2 7' : {'ending':'erentur','age':'X','frequency':'A'},
        'V 3 3 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'i','age':'B','frequency':'B'},
        'V 3 3 PRES ACTIVE  IMP 2 P 2 3' : {'ending':'ite','age':'B','frequency':'B'},
        'V 3 3 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'ito','age':'B','frequency':'B'},
        'V 3 3 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'ito','age':'B','frequency':'B'},    
        'V 3 3 FUT  ACTIVE  IMP 2 P 2 5' : {'ending':'itote','age':'B','frequency':'C'},  # OLD
        'V 3 3 PRES ACTIVE  INF 0 X 2 4' : {'ending':'iere','age':'B','frequency':'C'},  # G&L 173 N1
        'V 3 3 PRES ACTIVE  INF 0 X 2 4' : {'ending':'ieri','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IND 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IND 1 P 2 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IND 2 P 2 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  IND 1 S 2 3' : {'ending':'bam','age':'E','frequency':'D'},
        'V 3 4 IMPF ACTIVE  IND 2 S 2 3' : {'ending':'bas','age':'E','frequency':'D'}, 
        'V 3 4 IMPF ACTIVE  IND 3 S 2 3' : {'ending':'bat','age':'E','frequency':'D'},
        'V 3 4 IMPF ACTIVE  IND 1 P 2 5' : {'ending':'bamus','age':'E','frequency':'D'},
        'V 3 4 IMPF ACTIVE  IND 2 P 2 5' : {'ending':'batis','age':'E','frequency':'D'},
        'V 3 4 IMPF ACTIVE  IND 3 P 2 4' : {'ending':'bant','age':'E','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 1 S 1 2' : {'ending':'bo','age':'X','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 2 S 1 3' : {'ending':'bis','age':'X','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 3 S 1 3' : {'ending':'bit','age':'X','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 1 P 1 5' : {'ending':'bimus','age':'X','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 2 P 1 5' : {'ending':'bitis','age':'X','frequency':'D'},
        'V 3 4 FUT  ACTIVE  IND 3 P 1 4' : {'ending':'bunt','age':'X','frequency':'D'},
        'V 3 4 PRES PASSIVE IND 2 S 2 4' : {'ending':'iris','age':'X','frequency':'A'},
        'V 3 4 PRES PASSIVE IND 2 S 2 3' : {'ending':'ire','age':'B','frequency':'D'},  # G+L 130 1
        'V 3 4 PRES PASSIVE IND 3 S 2 4' : {'ending':'itur','age':'X','frequency':'A'},
        'V 3 4 FUT  PASSIVE IND 1 S 1 3' : {'ending':'bor','age':'E','frequency':'E'},
        'V 3 4 FUT  PASSIVE IND 2 S 1 5' : {'ending':'beris','age':'E','frequency':'E'},
        'V 3 4 FUT  PASSIVE IND 3 S 1 5' : {'ending':'berit','age':'E','frequency':'E'},
        'V 3 4 FUT  PASSIVE IND 1 P 1 5' : {'ending':'bimur','age':'E','frequency':'E'},
        'V 3 4 FUT  PASSIVE IND 2 P 1 6' : {'ending':'bimini','age':'E','frequency':'E'},
        'V 3 4 FUT  PASSIVE IND 3 P 1 6' : {'ending':'buntur','age':'E','frequency':'E'},
        'V 3 4 IMPF ACTIVE  SUB 1 S 2 4' : {'ending':'irem','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  SUB 2 S 2 4' : {'ending':'ires','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  SUB 3 S 2 4' : {'ending':'iret','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  SUB 1 P 2 6' : {'ending':'iremus','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  SUB 2 P 2 6' : {'ending':'iretis','age':'X','frequency':'A'},
        'V 3 4 IMPF ACTIVE  SUB 3 P 2 5' : {'ending':'irent','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 1 S 2 4' : {'ending':'irer','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 2 S 2 6' : {'ending':'ireris','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'irere','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 3 S 2 6' : {'ending':'iretur','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 1 P 2 6' : {'ending':'iremur','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 2 P 2 7' : {'ending':'iremini','age':'X','frequency':'A'},
        'V 3 4 IMPF PASSIVE SUB 3 P 2 7' : {'ending':'irentur','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  IMP 2 P 2 3' : {'ending':'ite','age':'X','frequency':'A'},
        'V 3 4 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 3 4 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 3 4 FUT  ACTIVE  IMP 2 P 2 5' : {'ending':'itote','age':'X','frequency':'A'},
        'V 3 4 FUT  ACTIVE  IMP 3 P 1 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 3 4 PRES PASSIVE IMP 2 S 2 3' : {'ending':'ire','age':'X','frequency':'A'},
        'V 3 4 PRES PASSIVE IMP 2 P 2 5' : {'ending':'imini','age':'X','frequency':'A'},
        'V 3 4 FUT  PASSIVE IMP 2 S 2 4' : {'ending':'itor','age':'X','frequency':'A'},
        'V 3 4 FUT  PASSIVE IMP 3 S 2 4' : {'ending':'itor','age':'X','frequency':'A'},
        'V 3 4 FUT  PASSIVE IMP 3 P 1 5' : {'ending':'untor','age':'X','frequency':'A'},
        'V 3 4 PRES ACTIVE  INF 0 X 2 3' : {'ending':'ire','age':'X','frequency':'A'},
        'V 3 4 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 3 4 PRES PASSIVE INF 0 X 2 3' : {'ending':'iri','age':'X','frequency':'A'},
        'V 3 4 PRES PASSIVE INF 0 X 2 5' : {'ending':'irier','age':'B','frequency':'B'}, 
        'V 5 0 PRES ACTIVE  IND 1 S 1 2' : {'ending':'um','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  IND 2 S 2 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  IND 3 S 2 3' : {'ending':'est','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  IND 1 P 1 4' : {'ending':'umus','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  IND 2 P 2 5' : {'ending':'estis','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 1 S 2 4' : {'ending':'eram','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 2 S 2 4' : {'ending':'eras','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 3 S 2 4' : {'ending':'erat','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 1 P 2 6' : {'ending':'eramus','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 2 P 2 6' : {'ending':'eratis','age':'X','frequency':'A'},
        'V 5 0 IMPF ACTIVE  IND 3 P 2 5' : {'ending':'erant','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 1 S 2 3' : {'ending':'ero','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 2 S 2 4' : {'ending':'eris','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 3 S 2 4' : {'ending':'erit','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 1 P 2 6' : {'ending':'erimus','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 2 P 2 6' : {'ending':'eritis','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 3 P 2 5' : {'ending':'erunt','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  IND 3 P 2 5' : {'ending':'erint','age':'E','frequency':'D'},
        'V 5 0 PRES ACTIVE  SUB 1 S 1 2' : {'ending':'im','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  SUB 2 S 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  SUB 3 S 1 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  SUB 1 P 1 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  SUB 2 P 1 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 5 0 PRES ACTIVE  SUB 3 P 1 3' : {'ending':'int','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 1 S 2 5' : {'ending':'essem','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 2 S 2 5' : {'ending':'esses','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 3 S 2 5' : {'ending':'esset','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 1 P 2 7' : {'ending':'essemus','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 2 P 2 7' : {'ending':'essetis','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 3 P 2 6' : {'ending':'essent','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 1 S 2 5' : {'ending':'forem','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 2 S 2 5' : {'ending':'fores','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 3 S 2 5' : {'ending':'foret','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 1 P 2 7' : {'ending':'foremus','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 2 P 2 7' : {'ending':'foretis','age':'X','frequency':'A'},
        'V 5 1 IMPF ACTIVE  SUB 3 P 2 6' : {'ending':'forent','age':'X','frequency':'A'},
        'V 5 1 PRES ACTIVE  IMP 2 S 2 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 5 1 PRES ACTIVE  IMP 2 P 2 4' : {'ending':'este','age':'X','frequency':'A'},
        'V 5 1 FUT  ACTIVE  IMP 2 S 2 4' : {'ending':'esto','age':'X','frequency':'A'},
        'V 5 1 FUT  ACTIVE  IMP 3 S 2 4' : {'ending':'esto','age':'X','frequency':'A'},
        'V 5 1 FUT  ACTIVE  IMP 2 P 2 6' : {'ending':'estote','age':'X','frequency':'A'},
        'V 5 1 FUT  ACTIVE  IMP 3 P 1 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 5 1 PRES ACTIVE  INF 0 X 2 4' : {'ending':'esse','age':'X','frequency':'A'},
        'V 5 0 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 5 0 FUT  ACTIVE  INF 0 X 2 4' : {'ending':'fore','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 1 S 1 2' : {'ending':'em','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 2 S 1 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 3 S 1 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 1 P 1 4' : {'ending':'emus','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 2 P 1 4' : {'ending':'etis','age':'X','frequency':'A'},
        'V 5 2 IMPF ACTIVE  SUB 3 P 1 3' : {'ending':'ent','age':'X','frequency':'A'},
        'V 5 2 FUT  ACTIVE  IND 3 P 2 5' : {'ending':'erint','age':'X','frequency':'E'},
        'V 5 2 PRES ACTIVE  INF 0 X 1 1' : {'ending':'e','age':'X','frequency':'A'},
        'V 5 2 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 1 S 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 2 S 2 1' : {'ending':'s','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 3 S 2 1' : {'ending':'t','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 1 P 2 3' : {'ending':'mus','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 2 P 2 3' : {'ending':'tis','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 1 S 2 3' : {'ending':'bam','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 2 S 2 3' : {'ending':'bas','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 3 S 2 3' : {'ending':'bat','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 1 P 2 5' : {'ending':'bamus','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 2 P 2 5' : {'ending':'batis','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 3 P 2 4' : {'ending':'bant','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  IND 1 S 2 4' : {'ending':'ebam','age':'D','frequency':'B'},
        'V 6 1 IMPF ACTIVE  IND 2 S 2 4' : {'ending':'ebas','age':'D','frequency':'B'},
        'V 6 1 IMPF ACTIVE  IND 3 S 2 4' : {'ending':'ebat','age':'D','frequency':'B'},
        'V 6 1 IMPF ACTIVE  IND 1 P 2 6' : {'ending':'ebamus','age':'D','frequency':'B'},
        'V 6 1 IMPF ACTIVE  IND 2 P 2 6' : {'ending':'ebatis','age':'D','frequency':'B'},
        'V 6 1 IMPF ACTIVE  IND 3 P 2 5' : {'ending':'ebant','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 1 S 2 2' : {'ending':'bo','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 2 S 2 3' : {'ending':'bis','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 3 S 2 3' : {'ending':'bit','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 1 P 2 5' : {'ending':'bimus','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 2 P 2 5' : {'ending':'bitis','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 3 P 2 4' : {'ending':'bunt','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IND 1 S 2 2' : {'ending':'am','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 2 S 2 2' : {'ending':'es','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 3 S 2 2' : {'ending':'et','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 1 P 2 4' : {'ending':'emus','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 2 P 2 4' : {'ending':'etis','age':'D','frequency':'B'},
        'V 6 1 FUT  ACTIVE  IND 3 P 2 3' : {'ending':'ent','age':'D','frequency':'B'},
        'V 6 1 PRES PASSIVE IND 1 S 1 2' : {'ending':'or','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 2 S 2 3' : {'ending':'ris','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 2 S 2 2' : {'ending':'re','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 3 S 2 3' : {'ending':'tur','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 1 P 2 3' : {'ending':'mur','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 2 P 2 4' : {'ending':'mini','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IND 3 P 1 5' : {'ending':'untur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 1 S 2 3' : {'ending':'bar','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 2 S 2 5' : {'ending':'baris','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 2 S 2 4' : {'ending':'bare','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 3 S 2 5' : {'ending':'batur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 1 P 2 5' : {'ending':'bamur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 2 P 2 6' : {'ending':'bamini','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE IND 3 P 2 6' : {'ending':'bantur','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 1 S 2 3' : {'ending':'bor','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 2 S 2 5' : {'ending':'beris','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 2 S 2 4' : {'ending':'bere','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 3 S 2 5' : {'ending':'bitur','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 1 P 2 5' : {'ending':'bimur','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 2 P 2 6' : {'ending':'bimini','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 3 P 2 6' : {'ending':'buntur','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IND 1 S 2 2' : {'ending':'ar','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 2 S 2 4' : {'ending':'eris','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 2 S 2 3' : {'ending':'ere','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 3 S 2 4' : {'ending':'etur','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 1 P 2 4' : {'ending':'emur','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 2 P 2 5' : {'ending':'emini','age':'E','frequency':'C'},
        'V 6 1 FUT  PASSIVE IND 3 P 2 5' : {'ending':'entur','age':'E','frequency':'C'},
        'V 6 1 PRES ACTIVE  SUB 1 S 1 2' : {'ending':'am','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  SUB 2 S 1 2' : {'ending':'as','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  SUB 3 S 1 2' : {'ending':'at','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  SUB 1 P 1 4' : {'ending':'amus','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  SUB 2 P 1 4' : {'ending':'atis','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  SUB 3 P 1 3' : {'ending':'ant','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 1 S 2 3' : {'ending':'rem','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 2 S 2 3' : {'ending':'res','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 3 S 2 3' : {'ending':'ret','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 1 P 2 5' : {'ending':'remus','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 2 P 2 5' : {'ending':'retis','age':'X','frequency':'A'},
        'V 6 1 IMPF ACTIVE  SUB 3 P 2 4' : {'ending':'rent','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 1 S 1 2' : {'ending':'ar','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 2 S 2 4' : {'ending':'aris','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 2 S 2 3' : {'ending':'are','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 3 S 2 4' : {'ending':'atur','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 1 P 2 4' : {'ending':'amur','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 2 P 2 5' : {'ending':'amini','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE SUB 3 P 1 5' : {'ending':'antur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 1 S 2 3' : {'ending':'rer','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 2 S 2 5' : {'ending':'reris','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 2 S 2 4' : {'ending':'rere','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 3 S 2 5' : {'ending':'retur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 1 P 2 5' : {'ending':'remur','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 2 P 2 6' : {'ending':'remini','age':'X','frequency':'A'},
        'V 6 1 IMPF PASSIVE SUB 3 P 2 6' : {'ending':'rentur','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IMP 2 S 2 0' : {'ending':'','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  IMP 2 P 2 2' : {'ending':'te','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IMP 2 S 2 2' : {'ending':'to','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IMP 3 S 2 2' : {'ending':'to','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IMP 2 P 2 4' : {'ending':'tote','age':'X','frequency':'A'},
        'V 6 1 FUT  ACTIVE  IMP 3 P 1 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IMP 2 S 2 3' : {'ending':'ere','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE IMP 2 P 2 4' : {'ending':'mini','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IMP 2 S 2 3' : {'ending':'tor','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IMP 3 S 2 3' : {'ending':'tor','age':'X','frequency':'A'},
        'V 6 1 FUT  PASSIVE IMP 3 P 1 5' : {'ending':'untor','age':'X','frequency':'A'},
        'V 6 1 PRES ACTIVE  INF 0 X 2 2' : {'ending':'re','age':'X','frequency':'A'},
        'V 6 1 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE INF 0 X 2 2' : {'ending':'ri','age':'X','frequency':'A'},
        'V 6 1 PRES PASSIVE INF 0 X 2 4' : {'ending':'rier','age':'B','frequency':'B'},
        'V 6 2 PRES ACTIVE  IND 1 S 1 1' : {'ending':'o','age':'X','frequency':'A'},
        #V 6 2 PRES ACTIVE  IND 2 S 1 3 vis           X
        #V 6 2 PRES ACTIVE  IND 3 S 1 4 vult          X
        'V 6 2 PRES ACTIVE  IND 1 P 1 4' : {'ending':'umus','age':'X','frequency':'A'},
        #V 6 2 PRES ACTIVE  IND 2 P 1 6 vultis      
        'V 6 2 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 1 S 1 4' : {'ending':'ebam','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 2 S 1 4' : {'ending':'ebas','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'ebat','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 1 P 1 6' : {'ending':'ebamus','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 2 P 1 6' : {'ending':'ebatis','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  IND 3 P 1 5' : {'ending':'ebant','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 1 S 1 2' : {'ending':'am','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 2 S 1 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 3 S 1 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 1 P 1 4' : {'ending':'emus','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 2 P 1 4' : {'ending':'etis','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IND 3 P 1 3' : {'ending':'ent','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 1 S 2 2' : {'ending':'im','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 1 P 2 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 2 P 2 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  SUB 3 P 2 3' : {'ending':'int','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 1 S 2 3' : {'ending':'lem','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 2 S 2 3' : {'ending':'les','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 3 S 2 3' : {'ending':'let','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 1 P 2 5' : {'ending':'lemus','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 2 P 2 5' : {'ending':'letis','age':'X','frequency':'A'},
        'V 6 2 IMPF ACTIVE  SUB 3 P 2 4' : {'ending':'lent','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  IMP 2 S 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  IMP 2 P 1 3' : {'ending':'ite','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IMP 2 S 1 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IMP 3 S 1 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IMP 2 P 1 5' : {'ending':'itote','age':'X','frequency':'A'},
        'V 6 2 FUT  ACTIVE  IMP 3 P 1 4' : {'ending':'unto','age':'X','frequency':'A'},
        'V 6 2 PRES ACTIVE  INF 0 X 2 2' : {'ending':'le','age':'X','frequency':'A'},
        'V 6 2 PERF ACTIVE  INF 0 X 3 4' : {'ending':'isse','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  IND 1 S 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  IND 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 1 S 1 4' : {'ending':'ebam','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 2 S 1 4' : {'ending':'ebas','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'ebat','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 1 P 1 6' : {'ending':'ebamus','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 2 P 1 6' : {'ending':'ebatis','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 3 P 1 5' : {'ending':'ebant','age':'X','frequency':'A'},
        'V 7 1 IMPF ACTIVE  IND 1 S 2 4' : {'ending':'ibam','age':'B','frequency':'B'},    # G&L 175 N
        'V 7 1 IMPF ACTIVE  IND 2 S 2 4' : {'ending':'ibas','age':'B','frequency':'B'},
        'V 7 1 IMPF ACTIVE  IND 3 S 2 4' : {'ending':'ibat','age':'B','frequency':'B'},
        'V 7 1 IMPF ACTIVE  IND 1 P 2 6' : {'ending':'ibamus','age':'B','frequency':'B'},
        'V 7 1 IMPF ACTIVE  IND 2 P 2 6' : {'ending':'ibatis','age':'B','frequency':'B'},
        'V 7 1 IMPF ACTIVE  IND 3 P 2 5' : {'ending':'ibant','age':'B','frequency':'B'},
        'V 7 1 PERF ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},    # Kludge KEY 3
        'V 7 1 PRES ACTIVE  SUB 2 S 2 3' : {'ending':'ias','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  SUB 3 S 2 3' : {'ending':'iat','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  SUB 3 P 2 4' : {'ending':'iant','age':'X','frequency':'A'},
        'V 7 1 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'i','age':'B','frequency':'D'},
        'V 7 2 PRES ACTIVE  IND 1 S 2 2' : {'ending':'am','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IND 2 S 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IND 1 P 2 4' : {'ending':'imus','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IND 2 P 2 4' : {'ending':'itis','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IND 3 P 1 3' : {'ending':'unt','age':'X','frequency':'A'},
        'V 7 2 IMPF ACTIVE  IND 3 S 1 4' : {'ending':'ebat','age':'X','frequency':'A'},
        'V 7 2 FUT  ACTIVE  IND 2 S 1 2' : {'ending':'es','age':'X','frequency':'A'},
        'V 7 2 FUT  ACTIVE  IND 3 S 1 2' : {'ending':'et','age':'X','frequency':'A'},
        'V 7 2 PERF ACTIVE  IND 1 S 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'V 7 2 PERF ACTIVE  IND 2 S 2 4' : {'ending':'isti','age':'X','frequency':'A'},
        'V 7 2 PERF ACTIVE  IND 3 S 2 2' : {'ending':'it','age':'X','frequency':'A'},
        'V 7 2 PRES ACTIVE  IMP 2 S 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'V 7 2 FUT  ACTIVE  IMP 2 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 7 2 FUT  ACTIVE  IMP 3 S 2 3' : {'ending':'ito','age':'X','frequency':'A'},
        'V 7 3 PRES ACTIVE  IND 2 S 2 0' : {'ending':'','age':'B','frequency':'B'},  # es
        'V 7 3 PRES ACTIVE  IND 3 S 2 1' : {'ending':'t','age':'B','frequency':'B'},    # est
        'V 7 3 PRES ACTIVE  IND 2 P 2 3' : {'ending':'tis','age':'B','frequency':'B'},    # estis
        'V 7 3 PRES ACTIVE  IND 3 S 2 3' : {'ending':'tur','age':'B','frequency':'B'},    # estur
        'V 7 3 PRES ACTIVE  SUB 1 S 1 2' : {'ending':'im','age':'B','frequency':'B'}, 
        'V 7 3 PRES ACTIVE  SUB 2 S 1 2' : {'ending':'is','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  SUB 3 S 1 2' : {'ending':'it','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  SUB 1 P 1 4' : {'ending':'imus','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  SUB 2 P 1 4' : {'ending':'itis','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  SUB 3 P 1 3' : {'ending':'int','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 1 S 2 3' : {'ending':'sem','age':'B','frequency':'B'},    # essem G&L 172
        'V 7 3 IMPF ACTIVE  SUB 2 S 2 3' : {'ending':'ses','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 3 S 2 3' : {'ending':'set','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 1 P 2 5' : {'ending':'semus','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 2 P 2 5' : {'ending':'setis','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 3 P 2 4' : {'ending':'sent','age':'B','frequency':'B'},
        'V 7 3 IMPF ACTIVE  SUB 3 S 2 5' : {'ending':'setur','age':'B','frequency':'B'},    # essetur 
        'V 7 3 PRES ACTIVE  IMP 2 S 2 0' : {'ending':'','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  IMP 2 P 2 2' : {'ending':'te','age':'B','frequency':'B'},
        'V 7 3 FUT  ACTIVE  IMP 2 S 2 2' : {'ending':'to','age':'B','frequency':'B'},
        'V 7 3 FUT  ACTIVE  IMP 3 S 2 2' : {'ending':'to','age':'B','frequency':'B'},
        'V 7 3 FUT  ACTIVE  IMP 2 P 2 4' : {'ending':'tote','age':'B','frequency':'B'},
        'V 7 3 PRES ACTIVE  INF 0 X 2 2' : {'ending':'se','age':'B','frequency':'B'},
        'V 8 0 FUTP ACTIVE  IND 1 S 3 1' : {'ending':'o','age':'B','frequency':'C'},
        'V 8 0 FUTP ACTIVE  IND 2 S 3 2' : {'ending':'is','age':'B','frequency':'C'},
        'V 8 0 FUTP ACTIVE  IND 3 S 3 2' : {'ending':'it','age':'B','frequency':'C'},
        'V 8 0 FUTP ACTIVE  IND 1 P 3 4' : {'ending':'imus','age':'B','frequency':'C'},
        'V 8 0 FUTP ACTIVE  IND 2 P 3 4' : {'ending':'itis','age':'B','frequency':'C'},
        'V 8 0 FUTP ACTIVE  IND 3 P 3 3' : {'ending':'int','age':'B','frequency':'C'},
        'V 8 0 PERF ACTIVE  SUB 1 S 3 2' : {'ending':'im','age':'B','frequency':'C'},
        'V 8 0 PERF ACTIVE  SUB 2 S 3 2' : {'ending':'is','age':'B','frequency':'C'},
        'V 8 0 PERF ACTIVE  SUB 3 S 3 2' : {'ending':'it','age':'B','frequency':'C'},
        'V 8 0 PERF ACTIVE  SUB 1 P 3 4' : {'ending':'imus','age':'B','frequency':'D'},
        'V 8 0 PERF ACTIVE  SUB 2 P 3 4' : {'ending':'itis','age':'B','frequency':'D'},
        'V 8 0 PERF ACTIVE  SUB 3 P 3 3' : {'ending':'int','age':'B','frequency':'D'},  
        'V 8 0 PLUP ACTIVE  SUB 1 S 3 2' : {'ending':'em','age':'B','frequency':'E'},
        'V 8 0 PLUP ACTIVE  SUB 2 S 3 2' : {'ending':'es','age':'B','frequency':'E'},
        'V 8 0 PLUP ACTIVE  SUB 3 S 3 2' : {'ending':'et','age':'B','frequency':'E'},
        'V 8 0 PLUP ACTIVE  SUB 1 P 3 4' : {'ending':'emus','age':'B','frequency':'E'},
        'V 8 0 PLUP ACTIVE  SUB 2 P 3 4' : {'ending':'etis','age':'B','frequency':'E'},
        'V 8 0 PLUP ACTIVE  SUB 3 P 3 3' : {'ending':'ent','age':'B','frequency':'E'},
        'V 8 0 PRES ACTIVE  INF 0 X 2 1' : {'ending':'e','age':'B','frequency':'C'},
        'V 9 8 X    X       X   0 X 1 0' : {'ending':'','age':'X','frequency':'A'},
        'V 9 9 X    X       X   0 X 1 0' : {'ending':'','age':'X','frequency':'A'}}

verb_participle_inflections = {'VPAR 1 0 NOM S X PRES ACTIVE  PPL 1 3' : {'ending':'as','age':'X','frequency':'A'},
        'VPAR 1 0 GEN S X PRES ACTIVE  PPL 1 5' : {'ending':'atis','age':'X','frequency':'A'},
        'VPAR 1 0 DAT S X PRES ACTIVE  PPL 1 4' : {'ending':'ati','age':'X','frequency':'A'},
        'VPAR 1 0 ACC S C PRES ACTIVE  PPL 1 5' : {'ending':'atem','age':'X','frequency':'A'},
        'VPAR 1 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'ati','age':'X','frequency':'A'},
        'VPAR 1 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'ate','age':'X','frequency':'A'},
        'VPAR 1 0 VOC S X PRES ACTIVE  PPL 1 3' : {'ending':'as','age':'X','frequency':'A'},
        'VPAR 1 0 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'ates','age':'X','frequency':'A'},
        'VPAR 1 0 GEN P X PRES ACTIVE  PPL 1 6' : {'ending':'atium','age':'X','frequency':'A'},
        'VPAR 1 0 GEN P X PRES ACTIVE  PPL 1 5' : {'ending':'atum','age':'X','frequency':'C'},  # Virgil examples
        'VPAR 1 0 DAT P X PRES ACTIVE  PPL 1 7' : {'ending':'atibus','age':'X','frequency':'A'},
        'VPAR 1 0 ACC P C PRES ACTIVE  PPL 1 5' : {'ending':'antes','age':'X','frequency':'A'},
        'VPAR 1 0 ABL P X PRES ACTIVE  PPL 1 7' : {'ending':'antibus','age':'X','frequency':'A'},
        'VPAR 1 0 VOC P C PRES ACTIVE  PPL 1 5' : {'ending':'antes','age':'X','frequency':'A'},
        'VPAR 1 0 ACC S N PRES ACTIVE  PPL 1 3' : {'ending':'ans','age':'X','frequency':'A'},
        'VPAR 1 0 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'antia','age':'X','frequency':'A'},
        'VPAR 1 0 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'antia','age':'X','frequency':'A'},
        'VPAR 1 0 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'antia','age':'X','frequency':'A'},
        'VPAR 2 0 NOM S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 2 0 GEN S X PRES ACTIVE  PPL 1 5' : {'ending':'entis','age':'X','frequency':'A'},
        'VPAR 2 0 DAT S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 2 0 ACC S C PRES ACTIVE  PPL 1 5' : {'ending':'entem','age':'X','frequency':'A'},
        'VPAR 2 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 2 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'ente','age':'X','frequency':'A'},
        'VPAR 2 0 VOC S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 2 0 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 2 0 GEN P X PRES ACTIVE  PPL 1 6' : {'ending':'entium','age':'X','frequency':'A'},
        'VPAR 2 0 GEN P X PRES ACTIVE  PPL 1 5' : {'ending':'entum','age':'X','frequency':'C'},  # Virgil examples
        'VPAR 2 0 DAT P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 2 0 ACC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 2 0 ABL P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 2 0 VOC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 2 0 ACC S N PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 2 0 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 2 0 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 2 0 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 3 0 NOM S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 3 0 GEN S X PRES ACTIVE  PPL 1 5' : {'ending':'entis','age':'X','frequency':'A'},
        'VPAR 3 0 DAT S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 3 0 ACC S C PRES ACTIVE  PPL 1 5' : {'ending':'entem','age':'X','frequency':'A'},
        'VPAR 3 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 3 0 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'ente','age':'X','frequency':'A'},
        'VPAR 3 0 VOC S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 3 0 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 3 0 GEN P X PRES ACTIVE  PPL 1 6' : {'ending':'entium','age':'X','frequency':'A'},
        'VPAR 3 0 GEN P X PRES ACTIVE  PPL 1 5' : {'ending':'entum','age':'X','frequency':'C'},  # Virgil examples
        'VPAR 3 0 DAT P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 3 0 ACC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 3 0 ABL P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 3 0 VOC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 3 0 ACC S N PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 3 0 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 3 0 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 3 0 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 5 1 NOM S X PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 5 1 NOM S X PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 5 1 GEN S X PRES ACTIVE  PPL 2 5' : {'ending':'entis','age':'X','frequency':'A'},
        'VPAR 5 1 DAT S X PRES ACTIVE  PPL 2 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 5 1 ACC S C PRES ACTIVE  PPL 2 5' : {'ending':'entem','age':'X','frequency':'A'},
        'VPAR 5 1 ABL S X PRES ACTIVE  PPL 2 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 5 1 ABL S X PRES ACTIVE  PPL 2 4' : {'ending':'ente','age':'X','frequency':'A'},
        'VPAR 5 1 VOC S X PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 5 1 NOM P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 5 1 GEN P X PRES ACTIVE  PPL 2 6' : {'ending':'entium','age':'X','frequency':'A'},
        'VPAR 5 1 DAT P X PRES ACTIVE  PPL 2 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 5 1 ACC P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 5 1 ABL P X PRES ACTIVE  PPL 2 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 5 1 VOC P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 5 1 ACC S N PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 5 1 NOM P N PRES ACTIVE  PPL 2 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 5 1 ACC P N PRES ACTIVE  PPL 2 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 5 1 VOC P N PRES ACTIVE  PPL 2 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 6 1 NOM S X PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 1 GEN S X PRES ACTIVE  PPL 1 5' : {'ending':'untis','age':'X','frequency':'A'},
        'VPAR 6 1 DAT S X PRES ACTIVE  PPL 1 4' : {'ending':'unti','age':'X','frequency':'A'},
        'VPAR 6 1 ACC S C PRES ACTIVE  PPL 1 5' : {'ending':'untem','age':'X','frequency':'A'},
        'VPAR 6 1 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'unti','age':'X','frequency':'A'},
        'VPAR 6 1 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'unte','age':'X','frequency':'A'},
        'VPAR 6 1 VOC S X PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 1 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'untes','age':'X','frequency':'A'},
        'VPAR 6 1 GEN P X PRES ACTIVE  PPL 1 6' : {'ending':'untium','age':'X','frequency':'A'},
        'VPAR 6 1 DAT P X PRES ACTIVE  PPL 1 7' : {'ending':'untibus','age':'X','frequency':'A'},
        'VPAR 6 1 ACC P C PRES ACTIVE  PPL 1 5' : {'ending':'untes','age':'X','frequency':'A'},
        'VPAR 6 1 ABL P X PRES ACTIVE  PPL 1 7' : {'ending':'untibus','age':'X','frequency':'A'},
        'VPAR 6 1 VOC P C PRES ACTIVE  PPL 1 5' : {'ending':'untes','age':'X','frequency':'A'},
        'VPAR 6 1 ACC S N PRES ACTIVE  PPL 2 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 1 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'untia','age':'X','frequency':'A'},
        'VPAR 6 1 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'untia','age':'X','frequency':'A'},
        'VPAR 6 1 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'untia','age':'X','frequency':'A'},
        'VPAR 6 1 GEN S X PRES ACTIVE  PPL 2 5' : {'ending':'entis','age':'E','frequency':'D'},
        'VPAR 6 1 DAT S X PRES ACTIVE  PPL 2 4' : {'ending':'enti','age':'E','frequency':'D'},
        'VPAR 6 1 ACC S C PRES ACTIVE  PPL 2 5' : {'ending':'entem','age':'E','frequency':'D'},
        'VPAR 6 1 ABL S X PRES ACTIVE  PPL 2 4' : {'ending':'enti','age':'E','frequency':'D'},
        'VPAR 6 1 ABL S X PRES ACTIVE  PPL 2 4' : {'ending':'ente','age':'E','frequency':'D'},
        #VPAR 6 1 VOC S X PRES ACTIVE  PPL 2' : '3','age':'e','frequency':'s'},          E D
        'VPAR 6 1 NOM P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'E','frequency':'D'},
        'VPAR 6 1 GEN P X PRES ACTIVE  PPL 2 6' : {'ending':'entium','age':'E','frequency':'D'},
        'VPAR 6 1 DAT P X PRES ACTIVE  PPL 2 7' : {'ending':'entibus','age':'E','frequency':'D'},
        'VPAR 6 1 ACC P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'E','frequency':'D'},
        'VPAR 6 1 ABL P X PRES ACTIVE  PPL 2 7' : {'ending':'entibus','age':'E','frequency':'D'},
        'VPAR 6 1 VOC P C PRES ACTIVE  PPL 2 5' : {'ending':'entes','age':'E','frequency':'D'},
        #VPAR 6 1 ACC S N PRES ACTIVE  PPL 2' : '3','age':'e','frequency':'s'},         E D
        'VPAR 6 2 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'E','frequency':'D'},
        'VPAR 6 2 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'E','frequency':'D'},
        'VPAR 6 2 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'E','frequency':'D'},
        'VPAR 6 2 NOM S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 2 GEN S X PRES ACTIVE  PPL 1 5' : {'ending':'entis','age':'X','frequency':'A'},
        'VPAR 6 2 DAT S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 6 2 ACC S C PRES ACTIVE  PPL 1 5' : {'ending':'entem','age':'X','frequency':'A'},
        'VPAR 6 2 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'enti','age':'X','frequency':'A'},
        'VPAR 6 2 ABL S X PRES ACTIVE  PPL 1 4' : {'ending':'ente','age':'X','frequency':'A'},
        'VPAR 6 2 VOC S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 2 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 6 2 GEN P X PRES ACTIVE  PPL 1 6' : {'ending':'entium','age':'X','frequency':'A'},
        'VPAR 6 2 DAT P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 6 2 ACC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 6 2 ABL P X PRES ACTIVE  PPL 1 7' : {'ending':'entibus','age':'X','frequency':'A'},
        'VPAR 6 2 VOC P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'X','frequency':'A'},
        'VPAR 6 2 ACC S N PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'X','frequency':'A'},
        'VPAR 6 2 NOM P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 6 2 ACC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 6 2 VOC P N PRES ACTIVE  PPL 1 5' : {'ending':'entia','age':'X','frequency':'A'},
        'VPAR 7 2 NOM S X PRES ACTIVE  PPL 1 3' : {'ending':'ens','age':'E','frequency':'A'},
        'VPAR 7 2 NOM P C PRES ACTIVE  PPL 1 5' : {'ending':'entes','age':'E','frequency':'A'},
        'VPAR 0 0 NOM S M PERF PASSIVE PPL 4 2' : {'ending':'us','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S M PERF PASSIVE PPL 4 1' : {'ending':'i','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S M PERF PASSIVE PPL 4 1' : {'ending':'o','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S M PERF PASSIVE PPL 4 2' : {'ending':'um','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S M PERF PASSIVE PPL 4 1' : {'ending':'o','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S M PERF PASSIVE PPL 4 1' : {'ending':'e','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P M PERF PASSIVE PPL 4 1' : {'ending':'i','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P M PERF PASSIVE PPL 4 4' : {'ending':'orum','age':'X','frequency':'A'},
        'VPAR 0 0 DAT P X PERF PASSIVE PPL 4 2' : {'ending':'is','age':'X','frequency':'A'},
        'VPAR 0 0 ACC P M PERF PASSIVE PPL 4 2' : {'ending':'os','age':'X','frequency':'A'},
        'VPAR 0 0 ABL P X PERF PASSIVE PPL 4 2' : {'ending':'is','age':'X','frequency':'A'},
        'VPAR 0 0 VOC P M PERF PASSIVE PPL 4 1' : {'ending':'i','age':'X','frequency':'A'},
        'VPAR 0 0 NOM S F PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S F PERF PASSIVE PPL 4 2' : {'ending':'ae','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S F PERF PASSIVE PPL 4 2' : {'ending':'ae','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S F PERF PASSIVE PPL 4 2' : {'ending':'am','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S F PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S F PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P F PERF PASSIVE PPL 4 2' : {'ending':'ae','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P F PERF PASSIVE PPL 4 4' : {'ending':'arum','age':'X','frequency':'A'},
        #VPAR 0 0 DAT P F PERF PASSIVE PPL 4' : '2','age':'i','frequency':' '},        
        'VPAR 0 0 ACC P F PERF PASSIVE PPL 4 2' : {'ending':'as','age':'X','frequency':'A'},
        #VPAR 0 0 ABL P F PERF PASSIVE PPL 4' : '2','age':'i','frequency':' '},        
        'VPAR 0 0 VOC P F PERF PASSIVE PPL 4 2' : {'ending':'ae','age':'X','frequency':'A'},
        'VPAR 0 0 NOM S N PERF PASSIVE PPL 4 2' : {'ending':'um','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S N PERF PASSIVE PPL 4 1' : {'ending':'i','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S N PERF PASSIVE PPL 4 1' : {'ending':'o','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S N PERF PASSIVE PPL 4 2' : {'ending':'um','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S N PERF PASSIVE PPL 4 1' : {'ending':'o','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S N PERF PASSIVE PPL 4 2' : {'ending':'um','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P N PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P N PERF PASSIVE PPL 4 4' : {'ending':'orum','age':'X','frequency':'A'},
        #VPAR 0 0 DAT P N PERF PASSIVE PPL 4 2 is         
        'VPAR 0 0 ACC P N PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        #VPAR 0 0 ABL P N PERF PASSIVE PPL 4 2 is           X
        'VPAR 0 0 VOC P N PERF PASSIVE PPL 4 1' : {'ending':'a','age':'X','frequency':'A'},
        'VPAR 0 0 NOM S M FUT  ACTIVE  PPL 4 4' : {'ending':'urus','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S M FUT  ACTIVE  PPL 4 3' : {'ending':'uri','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S M FUT  ACTIVE  PPL 4 3' : {'ending':'uro','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S M FUT  ACTIVE  PPL 4 4' : {'ending':'urum','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S M FUT  ACTIVE  PPL 4 3' : {'ending':'uro','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S M FUT  ACTIVE  PPL 4 3' : {'ending':'ure','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P M FUT  ACTIVE  PPL 4 3' : {'ending':'uri','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P M FUT  ACTIVE  PPL 4 6' : {'ending':'urorum','age':'X','frequency':'A'},
        'VPAR 0 0 DAT P X FUT  ACTIVE  PPL 4 4' : {'ending':'uris','age':'X','frequency':'A'},
        'VPAR 0 0 ACC P M FUT  ACTIVE  PPL 4 4' : {'ending':'uros','age':'X','frequency':'A'},
        'VPAR 0 0 ABL P X FUT  ACTIVE  PPL 4 4' : {'ending':'uris','age':'X','frequency':'A'},
        'VPAR 0 0 VOC P M FUT  ACTIVE  PPL 4 3' : {'ending':'uri','age':'X','frequency':'A'},
        'VPAR 0 0 NOM S F FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S F FUT  ACTIVE  PPL 4 4' : {'ending':'urae','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S F FUT  ACTIVE  PPL 4 4' : {'ending':'urae','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S F FUT  ACTIVE  PPL 4 4' : {'ending':'uram','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S F FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S F FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P F FUT  ACTIVE  PPL 4 4' : {'ending':'urae','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P F FUT  ACTIVE  PPL 4 6' : {'ending':'urarum','age':'X','frequency':'A'},
        #VPAR 0 0 DAT P F FUT  ACTIVE  PPL 4 4 uris         X
        'VPAR 0 0 ACC P F FUT  ACTIVE  PPL 4 4' : {'ending':'uras','age':'X','frequency':'A'},
        #VPAR 0 0 ABL P F FUT  ACTIVE  PPL 4 4 uris         X
        'VPAR 0 0 VOC P F FUT  ACTIVE  PPL 4 4' : {'ending':'urae','age':'X','frequency':'A'},
        'VPAR 0 0 NOM S N FUT  ACTIVE  PPL 4 4' : {'ending':'urum','age':'X','frequency':'A'},
        'VPAR 0 0 GEN S N FUT  ACTIVE  PPL 4 3' : {'ending':'uri','age':'X','frequency':'A'},
        'VPAR 0 0 DAT S N FUT  ACTIVE  PPL 4 3' : {'ending':'uro','age':'X','frequency':'A'},
        'VPAR 0 0 ACC S N FUT  ACTIVE  PPL 4 4' : {'ending':'urum','age':'X','frequency':'A'},
        'VPAR 0 0 ABL S N FUT  ACTIVE  PPL 4 3' : {'ending':'uro','age':'X','frequency':'A'},
        'VPAR 0 0 VOC S N FUT  ACTIVE  PPL 4 4' : {'ending':'urum','age':'X','frequency':'A'},
        'VPAR 0 0 NOM P N FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        'VPAR 0 0 GEN P N FUT  ACTIVE  PPL 4 6' : {'ending':'urorum','age':'X','frequency':'A'},
        #VPAR 0 0 DAT P N FUT  ACTIVE  PPL 4 4 uris         X
        'VPAR 0 0 ACC P N FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        #VPAR 0 0 ABL P N FUT  ACTIVE  PPL 4 4 uris         X
        'VPAR 0 0 VOC P N FUT  ACTIVE  PPL 4 3' : {'ending':'ura','age':'X','frequency':'A'},
        'VPAR 1 0 NOM S M FUT  PASSIVE PPL 1 5' : {'ending':'andus','age':'X','frequency':'A'},
        'VPAR 1 0 GEN S M FUT  PASSIVE PPL 1 4' : {'ending':'andi','age':'X','frequency':'A'},
        'VPAR 1 0 DAT S M FUT  PASSIVE PPL 1 4' : {'ending':'ando','age':'X','frequency':'A'},
        'VPAR 1 0 ACC S M FUT  PASSIVE PPL 1 5' : {'ending':'andum','age':'X','frequency':'A'},
        'VPAR 1 0 ABL S M FUT  PASSIVE PPL 1 4' : {'ending':'ando','age':'X','frequency':'A'},
        'VPAR 1 0 VOC S M FUT  PASSIVE PPL 1 4' : {'ending':'ande','age':'X','frequency':'A'},
        'VPAR 1 0 NOM P M FUT  PASSIVE PPL 1 4' : {'ending':'andi','age':'X','frequency':'A'},
        'VPAR 1 0 GEN P M FUT  PASSIVE PPL 1 7' : {'ending':'andorum','age':'X','frequency':'A'},
        'VPAR 1 0 DAT P X FUT  PASSIVE PPL 1 5' : {'ending':'andis','age':'X','frequency':'A'},
        'VPAR 1 0 ACC P M FUT  PASSIVE PPL 1 5' : {'ending':'andos','age':'X','frequency':'A'},
        'VPAR 1 0 ABL P X FUT  PASSIVE PPL 1 5' : {'ending':'andis','age':'X','frequency':'A'},
        'VPAR 1 0 VOC P M FUT  PASSIVE PPL 1 4' : {'ending':'andi','age':'X','frequency':'A'},
        'VPAR 1 0 NOM S F FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        'VPAR 1 0 GEN S F FUT  PASSIVE PPL 1 5' : {'ending':'andae','age':'X','frequency':'A'},
        'VPAR 1 0 DAT S F FUT  PASSIVE PPL 1 5' : {'ending':'andae','age':'X','frequency':'A'},
        'VPAR 1 0 ACC S F FUT  PASSIVE PPL 1 5' : {'ending':'andam','age':'X','frequency':'A'},
        'VPAR 1 0 ABL S F FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        'VPAR 1 0 VOC S F FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        'VPAR 1 0 NOM P F FUT  PASSIVE PPL 1 5' : {'ending':'andae','age':'X','frequency':'A'},
        'VPAR 1 0 GEN P F FUT  PASSIVE PPL 1 7' : {'ending':'andarum','age':'X','frequency':'A'},
        #VPAR 1 0 DAT P F FUT  PASSIVE PPL 1 5 andis        X
        'VPAR 1 0 ACC P F FUT  PASSIVE PPL 1 5' : {'ending':'andas','age':'X','frequency':'A'},
        #VPAR 1 0 ABL P F FUT  PASSIVE PPL 1 5 andis        
        'VPAR 1 0 VOC P F FUT  PASSIVE PPL 1 5' : {'ending':'andae','age':'X','frequency':'A'},
        'VPAR 1 0 NOM S N FUT  PASSIVE PPL 1 5' : {'ending':'andum','age':'X','frequency':'A'},
        'VPAR 1 0 GEN S N FUT  PASSIVE PPL 1 4' : {'ending':'andi','age':'X','frequency':'A'},
        'VPAR 1 0 DAT S N FUT  PASSIVE PPL 1 4' : {'ending':'ando','age':'X','frequency':'A'},
        'VPAR 1 0 ACC S N FUT  PASSIVE PPL 1 5' : {'ending':'andum','age':'X','frequency':'A'},
        'VPAR 1 0 ABL S N FUT  PASSIVE PPL 1 4' : {'ending':'ando','age':'X','frequency':'A'},
        'VPAR 1 0 VOC S N FUT  PASSIVE PPL 1 5' : {'ending':'andum','age':'X','frequency':'A'},
        'VPAR 1 0 NOM P N FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        'VPAR 1 0 GEN P N FUT  PASSIVE PPL 1 7' : {'ending':'andorum','age':'X','frequency':'A'},
        #VPAR 1 0 DAT P N FUT  PASSIVE PPL 1 5 andis        X
        'VPAR 1 0 ACC P N FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        #VPAR 1 0 ABL P N FUT  PASSIVE PPL 1 5 andis      
        'VPAR 1 0 VOC P N FUT  PASSIVE PPL 1 4' : {'ending':'anda','age':'X','frequency':'A'},
        'VPAR 2 0 NOM S M FUT  PASSIVE PPL 1 5' : {'ending':'endus','age':'X','frequency':'A'},
        'VPAR 2 0 GEN S M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'X','frequency':'A'},
        'VPAR 2 0 DAT S M FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'X','frequency':'A'},
        'VPAR 2 0 ACC S M FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'X','frequency':'A'},
        'VPAR 2 0 ABL S M FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'X','frequency':'A'},
        'VPAR 2 0 VOC S M FUT  PASSIVE PPL 1 4' : {'ending':'ende','age':'X','frequency':'A'},
        'VPAR 2 0 NOM P M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'X','frequency':'A'},
        'VPAR 2 0 GEN P M FUT  PASSIVE PPL 1 7' : {'ending':'endorum','age':'X','frequency':'A'},
        'VPAR 2 0 DAT P X FUT  PASSIVE PPL 1 5' : {'ending':'endis','age':'X','frequency':'A'},
        'VPAR 2 0 ACC P M FUT  PASSIVE PPL 1 5' : {'ending':'endos','age':'X','frequency':'A'},
        'VPAR 2 0 ABL P X FUT  PASSIVE PPL 1 5' : {'ending':'endis','age':'X','frequency':'A'},
        'VPAR 2 0 VOC P M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'X','frequency':'A'},
        'VPAR 2 0 NOM S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        'VPAR 2 0 GEN S F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'X','frequency':'A'},
        'VPAR 2 0 DAT S F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'X','frequency':'A'},
        'VPAR 2 0 ACC S F FUT  PASSIVE PPL 1 5' : {'ending':'endam','age':'X','frequency':'A'},
        'VPAR 2 0 ABL S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        'VPAR 2 0 VOC S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        'VPAR 2 0 NOM P F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'X','frequency':'A'},
        'VPAR 2 0 GEN P F FUT  PASSIVE PPL 1 7' : {'ending':'endarum','age':'X','frequency':'A'},
        #VPAR 2 0 DAT P F FUT  PASSIVE PPL 1 5 endis        X 
        'VPAR 2 0 ACC P F FUT  PASSIVE PPL 1 5' : {'ending':'endas','age':'X','frequency':'A'},
        #VPAR 2 0 ABL P F FUT  PASSIVE PPL 1 5 endis        X
        'VPAR 2 0 VOC P F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'X','frequency':'A'},
        'VPAR 2 0 NOM S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'X','frequency':'A'},
        'VPAR 2 0 GEN S N FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'X','frequency':'A'},
        'VPAR 2 0 DAT S N FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'X','frequency':'A'},
        'VPAR 2 0 ACC S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'X','frequency':'A'},
        'VPAR 2 0 ABL S N FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'X','frequency':'A'},
        'VPAR 2 0 VOC S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'X','frequency':'A'},
        'VPAR 2 0 NOM P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        'VPAR 2 0 GEN P N FUT  PASSIVE PPL 1 7' : {'ending':'endorum','age':'X','frequency':'A'},
        #VPAR 2 0 DAT P N FUT  PASSIVE PPL 1 5 endis        X
        'VPAR 2 0 ACC P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        #VPAR 2 0 ABL P N FUT  PASSIVE PPL 1 5 endis        X
        'VPAR 2 0 VOC P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'X','frequency':'A'},
        'VPAR 3 0 NOM S M FUT  PASSIVE PPL 1 5' : {'ending':'endus','age':'D','frequency':'A'},
        'VPAR 3 0 GEN S M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'D','frequency':'A'},
        'VPAR 3 0 DAT S M FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'D','frequency':'A'},
        'VPAR 3 0 ACC S M FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'D','frequency':'A'},
        'VPAR 3 0 ABL S M FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'D','frequency':'A'},
        'VPAR 3 0 VOC S M FUT  PASSIVE PPL 1 4' : {'ending':'ende','age':'D','frequency':'A'},
        'VPAR 3 0 NOM P M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'D','frequency':'A'},
        'VPAR 3 0 GEN P M FUT  PASSIVE PPL 1 7' : {'ending':'endorum','age':'D','frequency':'A'},
        'VPAR 3 0 DAT P X FUT  PASSIVE PPL 1 5' : {'ending':'endis','age':'D','frequency':'A'},
        'VPAR 3 0 ACC P M FUT  PASSIVE PPL 1 5' : {'ending':'endos','age':'D','frequency':'A'},
        'VPAR 3 0 ABL P X FUT  PASSIVE PPL 1 5' : {'ending':'endis','age':'D','frequency':'A'},
        'VPAR 3 0 VOC P M FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'D','frequency':'A'},
        'VPAR 3 0 NOM S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        'VPAR 3 0 GEN S F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'D','frequency':'A'},
        'VPAR 3 0 DAT S F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'D','frequency':'A'},
        'VPAR 3 0 ACC S F FUT  PASSIVE PPL 1 5' : {'ending':'endam','age':'D','frequency':'A'},
        'VPAR 3 0 ABL S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        'VPAR 3 0 VOC S F FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        'VPAR 3 0 NOM P F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'D','frequency':'A'},
        'VPAR 3 0 GEN P F FUT  PASSIVE PPL 1 7' : {'ending':'endarum','age':'D','frequency':'A'},
        #VPAR 3 0 DAT P F FUT  PASSIVE PPL 1,5,edis     D
        'VPAR 3 0 ACC P F FUT  PASSIVE PPL 1 5' : {'ending':'endas','age':'D','frequency':'A'},
        #VPAR 3 0 ABL P F FUT  PASSIVE PPL 1 5 endis        D
        'VPAR 3 0 VOC P F FUT  PASSIVE PPL 1 5' : {'ending':'endae','age':'D','frequency':'A'},
        'VPAR 3 0 NOM S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'D','frequency':'A'},
        'VPAR 3 0 GEN S N FUT  PASSIVE PPL 1 4' : {'ending':'endi','age':'D','frequency':'A'},
        'VPAR 3 0 DAT S N FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'D','frequency':'A'},
        'VPAR 3 0 ACC S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'D','frequency':'A'},
        'VPAR 3 0 ABL S N FUT  PASSIVE PPL 1 4' : {'ending':'endo','age':'D','frequency':'A'},
        'VPAR 3 0 VOC S N FUT  PASSIVE PPL 1 5' : {'ending':'endum','age':'D','frequency':'A'},
        'VPAR 3 0 NOM P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        'VPAR 3 0 GEN P N FUT  PASSIVE PPL 1 7' : {'ending':'endorum','age':'D','frequency':'A'},
        #VPAR 3 0 DAT P N FUT  PASSIVE PPL 1 5 endis        D
        'VPAR 3 0 ACC P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        #VPAR 3 0 ABL P N FUT  PASSIVE PPL 1 5 endis        D
        'VPAR 3 0 VOC P N FUT  PASSIVE PPL 1 4' : {'ending':'enda','age':'D','frequency':'A'},
        'VPAR 3 0 NOM S M FUT  PASSIVE PPL 1 5' : {'ending':'undus','age':'B','frequency':'A'},
        'VPAR 3 0 GEN S M FUT  PASSIVE PPL 1 4' : {'ending':'undi','age':'B','frequency':'A'},
        'VPAR 3 0 DAT S M FUT  PASSIVE PPL 1 4' : {'ending':'undo','age':'B','frequency':'A'},
        'VPAR 3 0 ACC S M FUT  PASSIVE PPL 1 5' : {'ending':'undum','age':'B','frequency':'A'},
        'VPAR 3 0 ABL S M FUT  PASSIVE PPL 1 4' : {'ending':'undo','age':'B','frequency':'A'},
        'VPAR 3 0 VOC S M FUT  PASSIVE PPL 1 4' : {'ending':'unde','age':'B','frequency':'A'},
        'VPAR 3 0 NOM P M FUT  PASSIVE PPL 1 4' : {'ending':'undi','age':'B','frequency':'A'},
        'VPAR 3 0 GEN P M FUT  PASSIVE PPL 1 7' : {'ending':'undorum','age':'B','frequency':'A'},
        'VPAR 3 0 DAT P X FUT  PASSIVE PPL 1 5' : {'ending':'undis','age':'B','frequency':'A'},
        'VPAR 3 0 ACC P M FUT  PASSIVE PPL 1 5' : {'ending':'undos','age':'B','frequency':'A'},
        'VPAR 3 0 ABL P X FUT  PASSIVE PPL 1 5' : {'ending':'undis','age':'B','frequency':'A'},
        'VPAR 3 0 VOC P M FUT  PASSIVE PPL 1 4' : {'ending':'undi','age':'B','frequency':'A'},
        'VPAR 3 0 NOM S F FUT  PASSIVE PPL 1 4' : {'ending':'unda','age':'B','frequency':'A'},
        'VPAR 3 0 GEN S F FUT  PASSIVE PPL 1 5' : {'ending':'undae','age':'B','frequency':'A'},
        'VPAR 3 0 DAT S F FUT  PASSIVE PPL 1 5' : {'ending':'undae','age':'B','frequency':'A'},
        'VPAR 3 0 ACC S F FUT  PASSIVE PPL 1 5' : {'ending':'undam','age':'B','frequency':'A'},
        'VPAR 3 0 ABL S F FUT  PASSIVE PPL 1 4' : {'ending':'unda','age':'B','frequency':'A'},
        'VPAR 3 0 VOC S F FUT  PASSIVE PPL 1 4' : {'ending':'unda','age':'B','frequency':'A'},
        'VPAR 3 0 NOM P F FUT  PASSIVE PPL 1 5' : {'ending':'undae','age':'B','frequency':'A'},
        'VPAR 3 0 GEN P F FUT  PASSIVE PPL 1 7' : {'ending':'undarum','age':'B','frequency':'A'},
        #VPAR 3 0 DAT P F FUT  PASSIVE PPL 1 5 undis        B
        'VPAR 3 0 ACC P F FUT  PASSIVE PPL 1 5' : {'ending':'undas','age':'B','frequency':'A'},
        #VPAR 3 0 ABL P F FUT  PASSIVE PPL 1 5 undis        B
        'VPAR 3 0 VOC P F FUT  PASSIVE PPL 1 5' : {'ending':'undae','age':'B','frequency':'A'},
        'VPAR 3 0 NOM S N FUT  PASSIVE PPL 1 5' : {'ending':'undum','age':'B','frequency':'A'},
        'VPAR 3 0 GEN S N FUT  PASSIVE PPL 1 4' : {'ending':'undi','age':'B','frequency':'A'},
        'VPAR 3 0 DAT S N FUT  PASSIVE PPL 1 4' : {'ending':'undo','age':'B','frequency':'A'},
        'VPAR 3 0 ACC S N FUT  PASSIVE PPL 1 5' : {'ending':'undum','age':'B','frequency':'A'},
        'VPAR 3 0 ABL S N FUT  PASSIVE PPL 1 4' : {'ending':'undo','age':'B','frequency':'A'},
        'VPAR 3 0 VOC S N FUT  PASSIVE PPL 1 5' : {'ending':'undum','age':'B','frequency':'A'},
        'VPAR 3 0 NOM P N FUT  PASSIVE PPL 1 4' : {'ending':'unda','age':'B','frequency':'A'},
        'VPAR 3 0 GEN P N FUT  PASSIVE PPL 1 7': {'ending':'undorum','age':'B','frequency':'A'},
        #VPAR 3 0 DAT P N FUT  PASSIVE PPL 1 5 undis        B 
        'VPAR 3 0 ACC P N FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'B','frequency':'A'},
        #VPAR 3 0 ABL P N FUT  PASSIVE PPL 1 5 undis        B
        'VPAR 3 0 VOC P N FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'B','frequency':'A'},
        'VPAR 6 1 NOM S M FUT  PASSIVE PPL 1 5': {'ending':'undus','age':'X','frequency':'A'},
        'VPAR 6 1 GEN S M FUT  PASSIVE PPL 1 4': {'ending':'undi','age':'X','frequency':'A'},
        'VPAR 6 1 DAT S M FUT  PASSIVE PPL 1 4': {'ending':'undo','age':'X','frequency':'A'},
        'VPAR 6 1 ACC S M FUT  PASSIVE PPL 1 5': {'ending':'undum','age':'X','frequency':'A'},
        'VPAR 6 1 ABL S M FUT  PASSIVE PPL 1 4': {'ending':'undo','age':'X','frequency':'A'},
        'VPAR 6 1 VOC S M FUT  PASSIVE PPL 1 4': {'ending':'unde','age':'X','frequency':'A'},
        'VPAR 6 1 NOM P M FUT  PASSIVE PPL 1 4': {'ending':'undi','age':'X','frequency':'A'},
        'VPAR 6 1 GEN P M FUT  PASSIVE PPL 1 7': {'ending':'undorum','age':'X','frequency':'A'},
        'VPAR 6 1 DAT P X FUT  PASSIVE PPL 1 5': {'ending':'undis','age':'X','frequency':'A'},
        'VPAR 6 1 ACC P M FUT  PASSIVE PPL 1 5': {'ending':'undos','age':'X','frequency':'A'},
        'VPAR 6 1 ABL P X FUT  PASSIVE PPL 1 5': {'ending':'undis','age':'X','frequency':'A'},
        'VPAR 6 1 VOC P M FUT  PASSIVE PPL 1 4': {'ending':'undi','age':'X','frequency':'A'},
        'VPAR 6 1 NOM S F FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'},
        'VPAR 6 1 GEN S F FUT  PASSIVE PPL 1 5': {'ending':'undae','age':'X','frequency':'A'},
        'VPAR 6 1 DAT S F FUT  PASSIVE PPL 1 5': {'ending':'undae','age':'X','frequency':'A'},
        'VPAR 6 1 ACC S F FUT  PASSIVE PPL 1 5': {'ending':'undam','age':'X','frequency':'A'},
        'VPAR 6 1 ABL S F FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'},
        'VPAR 6 1 VOC S F FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'},
        'VPAR 6 1 NOM P F FUT  PASSIVE PPL 1 5': {'ending':'undae','age':'X','frequency':'A'},
        'VPAR 6 1 GEN P F FUT  PASSIVE PPL 1 7': {'ending':'undarum','age':'X','frequency':'A'},
        #VPAR 6 1 DAT P F FUT  PASSIVE PPL 1 5 undis        X
        'VPAR 6 1 ACC P F FUT  PASSIVE PPL 1 5': {'ending':'undas','age':'X','frequency':'A'},
        #VPAR 6 1 ABL P F FUT  PASSIVE PPL 1 5 undis        X
        'VPAR 6 1 VOC P F FUT  PASSIVE PPL 1 5': {'ending':'undae','age':'X','frequency':'A'},
        'VPAR 6 1 NOM S N FUT  PASSIVE PPL 1 5': {'ending':'undum','age':'X','frequency':'A'},
        'VPAR 6 1 GEN S N FUT  PASSIVE PPL 1 4': {'ending':'undi','age':'X','frequency':'A'},
        'VPAR 6 1 DAT S N FUT  PASSIVE PPL 1 4': {'ending':'undo','age':'X','frequency':'A'},
        'VPAR 6 1 ACC S N FUT  PASSIVE PPL 1 5': {'ending':'undum','age':'X','frequency':'A'},
        'VPAR 6 1 ABL S N FUT  PASSIVE PPL 1 4': {'ending':'undo','age':'X','frequency':'A'},
        'VPAR 6 1 VOC S N FUT  PASSIVE PPL 1 5': {'ending':'undum','age':'X','frequency':'A'},
        'VPAR 6 1 NOM P N FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'},
        'VPAR 6 1 GEN P N FUT  PASSIVE PPL 1 7': {'ending':'undorum','age':'X','frequency':'A'},
        #VPAR 6 1 DAT P N FUT  PASSIVE PPL 1 5 undis        X
        'VPAR 6 1 ACC P N FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'},
        #VPAR 6 1 ABL P N FUT  PASSIVE PPL 1 5 undis         X
        'VPAR 6 1 VOC P N FUT  PASSIVE PPL 1 4': {'ending':'unda','age':'X','frequency':'A'} }

supine_inflections = {'SUPINE 0 0 ACC S N  4 2': {'ending':'um','age':'X','frequency':'A'},
        'SUPINE 0 0 ABL S N  4 1':{'ending':'u','age':'X','frequency':'A'}}

pronoun_inflections = { 
        'PRON 9 9 X   X X 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 1 0 GEN S X 2 3' : {'ending':'jus','age':'X','frequency':'A'},
        'PRON 1 0 DAT S X 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 1 0 ACC S M 1 2' : {'ending':'em','age':'X','frequency':'A'},
        'PRON 1 0 ABL S M 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 1 0 ACC S F 1 2' : {'ending':'am','age':'X','frequency':'A'},
        'PRON 1 0 ABL S N 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 1 0 NOM P M 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 1 0 GEN P M 1 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 1 0 DAT P X 1 4' : {'ending':'ib','age':'X','frequency':'A'},
        # Alternatively
        'PRON 1 0 DAT P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 1 0 ACC P M 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 1 0 ABL P X 1 4' : {'ending':'ib','age':'X','frequency':'A'},
        # Alternatively
        'PRON 1 0 ABL P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 1 0 NOM P F 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 1 0 GEN P F 1 4' : {'ending':'ar','age':'X','frequency':'A'},
        'PRON 1 0 ACC P F 1 2' : {'ending':'as','age':'X','frequency':'A'},
        'PRON 1 0 GEN P N 1 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 1 1 NOM S M 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 1 2 NOM S C 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 1 5 ABL S F 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 1 3 NOM S F 1 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 1 3 ABL S F 1 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 1 4 NOM S F 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 1 4 ABL S F 1 1' : {'ending':'a','age':'X','frequency':'A'},
        #PRON 1 5 NOM S F 1 2 is                          X A  
        #PRON 1 5 ABL S F 1 1 o                           X A
        'PRON 1 6 NOM S N 1 2' : {'ending':'id','age':'X','frequency':'A'},
        'PRON 1 6 ACC S N 1 2' : {'ending':'id','age':'X','frequency':'A'},
        'PRON 1 7 NOM S N 1 2' : {'ending':'od','age':'X','frequency':'A'},
        'PRON 1 7 ACC S N 1 2' : {'ending':'od','age':'X','frequency':'A'},
        'PRON 1 8 NOM P N 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 1 8 ACC P N 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 1 9 NOM P N 1 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 1 9 ACC P N 1 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 3 0 NOM S M 1 2' : {'ending':'ic','age':'X','frequency':'A'},
        'PRON 3 0 GEN S X 2 3' : {'ending':'iu','age':'X','frequency':'A'},
        'PRON 3 0 DAT S X 2 2' : {'ending':'ic','age':'X','frequency':'A'},
        'PRON 3 0 ACC S M 1 3' : {'ending':'un','age':'X','frequency':'A'},
        'PRON 3 0 ABL S M 1 2' : {'ending':'oc','age':'X','frequency':'A'},
        'PRON 3 0 NOM P M 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 3 0 NOM P M 1 2' : {'ending':'ii','age':'E','frequency':'C'},  # Souter/Vulgate
        'PRON 3 0 GEN P M 1 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 3 0 DAT P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 3 0 DAT P X 1 4' : {'ending':'ib','age':'B','frequency':'E'},
        'PRON 3 0 DAT P X 1 3' : {'ending':'ii','age':'E','frequency':'C'},  # Souter/Vulgate
        'PRON 3 0 ACC P M 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 3 0 ABL P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 3 0 ABL P X 1 4' : {'ending':'ib','age':'B','frequency':'E'},
        'PRON 3 0 ABL P X 1 3' : {'ending':'ii','age':'E','frequency':'C'},  # Souter/Vulgate
        'PRON 3 0 NOM S F 1 3' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 3 0 ACC S F 1 3' : {'ending':'an','age':'X','frequency':'A'},
        'PRON 3 0 ABL S F 1 2' : {'ending':'ac','age':'X','frequency':'A'},
        'PRON 3 0 NOM P F 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 3 0 GEN P F 1 4' : {'ending':'ar','age':'X','frequency':'A'},
        'PRON 3 0 ACC P F 1 2' : {'ending':'as','age':'X','frequency':'A'},
        'PRON 3 1 NOM S N 1 2' : {'ending':'oc','age':'X','frequency':'A'},
        'PRON 3 1 ACC S N 1 2' : {'ending':'oc','age':'X','frequency':'A'},
        'PRON 3 0 ABL S N 1 2' : {'ending':'oc','age':'X','frequency':'A'},
        'PRON 3 0 NOM P N 1 3' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 3 0 GEN P N 1 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 3 0 ACC P N 1 3' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 3 2 NOM S N 1 2' : {'ending':'uc','age':'X','frequency':'A'},
        'PRON 3 2 ACC S N 1 2' : {'ending':'uc','age':'X','frequency':'A'},
        'PRON 4 1 NOM S M 1 1' : {'ending':'s','age':'X','frequency':'A'},
        'PRON 4 0 GEN S X 2 3' : {'ending':'iu','age':'X','frequency':'A'},
        'PRON 4 0 DAT S X 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 4 1 ACC S M 2 2' : {'ending':'um','age':'X','frequency':'A'},
        'PRON 4 0 ABL S M 2 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 4 0 NOM P M 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 4 0 NOM P M 1 1' : {'ending':'i','age':'X','frequency':'B'},  # A&G 102
        'PRON 4 1 GEN P M 2 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 4 0 DAT P X 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 4 0 DAT P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 4 0 DAT P X 1 1' : {'ending':'s','age':'X','frequency':'C'}, 
        'PRON 4 0 ACC P M 2 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 4 0 ABL P X 2 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 4 0 ABL P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 4 0 ABL P X 1 1' : {'ending':'s','age':'X','frequency':'C'},
        'PRON 4 0 NOM S F 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 4 1 ACC S F 2 2' : {'ending':'am','age':'X','frequency':'A'},
        'PRON 4 0 ABL S F 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 4 0 NOM P F 2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 4 1 GEN P F 2 4' : {'ending':'ar','age':'X','frequency':'A'},
        'PRON 4 0 ACC P F 2 2' : {'ending':'as','age':'X','frequency':'A'},
        'PRON 4 1 NOM S N 1 1' : {'ending':'d','age':'X','frequency':'A'},
        'PRON 4 1 ACC S N 1 1' : {'ending':'d','age':'X','frequency':'A'},
        'PRON 4 0 ABL S N 2 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 4 0 NOM P N 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 4 1 GEN P N 2 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 4 0 ACC P N 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 4 2 NOM S M 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 4 2 ACC S M 2 2' : {'ending':'un','age':'X','frequency':'A'},
        'PRON 4 2 GEN P M 2 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 4 2 ACC S F 2 2' : {'ending':'an','age':'X','frequency':'A'},
        'PRON 4 2 GEN P F 2 4' : {'ending':'ar','age':'X','frequency':'A'},
        'PRON 4 2 NOM S N 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 4 2 ACC S N 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 4 2 NOM P N 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 4 2 GEN P N 2 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 4 2 ACC P N 2 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 5 1 NOM S C 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 5 1 VOC S C 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 5 1 GEN S C 2 2' : {'ending':'ei','age':'X','frequency':'A'},
        'PRON 5 1 GEN S C 2 2' : {'ending':'is','age':'B','frequency':'C'},   # G&L 100.2 + poets
        'PRON 5 1 DAT S C 2 3' : {'ending':'ih','age':'X','frequency':'A'},
        'PRON 5 1 DAT S C 2 1' : {'ending':'i','age':'X','frequency':'C'},   # G&L 100.2 + poets
        'PRON 5 1 ACC S C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 1 ABL S C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 1 ACC S C 2 2' : {'ending':'ed','age':'A','frequency':'E'},
        'PRON 5 1 ABL S C 2 2' : {'ending':'ed','age':'A','frequency':'E'},
        'PRON 5 1 ACC S C 2 3' : {'ending':'em','age':'X','frequency':'D'},
        'PRON 5 1 ABL S C 2 3' : {'ending':'em','age':'X','frequency':'D'},
        'PRON 5 1 VOC P C 2 1' : {'ending':'i','age':'D','frequency':'B'},   # G&L 100 2.2  VOC of nos
        'PRON 5 2 NOM S C 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 5 2 VOC S C 1 0' : {'ending':'','age':'X','frequency':'A'},
        'PRON 5 2 GEN S C 2 2' : {'ending':'ui','age':'X','frequency':'A'},
        'PRON 5 2 GEN S C 2 2' : {'ending':'is','age':'B','frequency':'C'},  # G&L 101 N1
        'PRON 5 2 DAT S C 2 3' : {'ending':'ib','age':'X','frequency':'A'},
        'PRON 5 2 DAT S C 2 4' : {'ending':'ib','age':'B','frequency':'I'},  # G&L 101 N1
        'PRON 5 2 DAT S C 2 3' : {'ending':'ib','age':'B','frequency':'I'},  # G&L 101 N1
        'PRON 5 2 ACC S C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 2 ACC S C 2 2' : {'ending':'ed','age':'B','frequency':'C'},  # G&L 101 N1
        'PRON 5 2 ACC S C 2 3' : {'ending':'et','age':'B','frequency':'B'},  # G&L 101 N1
        'PRON 5 2 ABL S C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 2 ABL S C 2 2' : {'ending':'ed','age':'X','frequency':'A'},
        'PRON 5 2 ABL S C 2 3' : {'ending':'et','age':'B','frequency':'B'},  # G&L 101 N1
        'PRON 5 3 NOM P C 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 5 3 VOC P C 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 5 3 GEN P C 2 2' : {'ending':'um','age':'X','frequency':'A'},
        'PRON 5 3 GEN P C 2 2' : {'ending':'om','age':'B','frequency':'C'},  # G&L 101 N3
        'PRON 5 3 GEN P C 2 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 5 3 GEN P M 2 4' : {'ending':'or','age':'B','frequency':'C'},  # G&L 101 N1
        'PRON 5 3 GEN P F 2 4' : {'ending':'ar','age':'B','frequency':'C'},  # G&L 101 N1
        'PRON 5 3 DAT P C 1 4' : {'ending':'ob','age':'X','frequency':'A'},
        'PRON 5 3 ACC P C 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 5 3 ABL P C 1 4' : {'ending':'ob','age':'X','frequency':'A'},
        'PRON 5 4 GEN X C 2 2' : {'ending':'ui','age':'X','frequency':'A'},
        'PRON 5 4 DAT X C 2 3' : {'ending':'ib','age':'X','frequency':'A'},
        'PRON 5 4 ACC X C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 4 ACC X C 2 3' : {'ending':'es','age':'X','frequency':'A'},
        'PRON 5 4 ABL X C 2 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 5 4 ABL X C 2 3' : {'ending':'es','age':'X','frequency':'A'},
        'PRON 6 0 NOM S M 1 1' : {'ending':'e','age':'X','frequency':'A'},
        'PRON 6 0 GEN S X 1 3' : {'ending':'iu','age':'X','frequency':'A'},
        'PRON 6 0 DAT S X 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 6 0 ACC S M 1 2' : {'ending':'um','age':'X','frequency':'A'},
        'PRON 6 0 ABL S M 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 6 0 NOM P M 1 1' : {'ending':'i','age':'X','frequency':'A'},
        'PRON 6 0 GEN P M 1 4' : {'ending':'or','age':'X','frequency':'A'},
        'PRON 6 0 DAT P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 6 0 ACC P M 1 2' : {'ending':'os','age':'X','frequency':'A'},
        'PRON 6 0 ABL P X 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 6 0 NOM S F 1 1' : {'ending':'a','age':'X','frequency':'A'},
        #PRON 6 0 GEN S F 1 3 ius                         X A
        #PRON 6 0 DAT S F 1 1 i                           X A
        'PRON 6 0 ACC S F 1 2' : {'ending':'am','age':'X','frequency':'A'},
        #PRON 6 0 ABL S F 1 1 a                           X A
        'PRON 6 0 NOM P F 1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'PRON 6 0 GEN P F 1 4' : {'ending':'ar','age':'X','frequency':'A'},
        #PRON 6 0 DAT P F 1 2 is                          X A
        'PRON 6 0 ACC P F 1 2' : {'ending':'as','age':'X','frequency':'A'},
        'PRON 6 0 ABL P F 1 2' : {'ending':'is','age':'X','frequency':'A'},
        'PRON 6 1 NOM S N 1 2' : {'ending':'ud','age':'X','frequency':'A'},
        #PRON 6 0 GEN S N 1 3 ius                         X A
        #PRON 6 0 DAT S N 1 1 i                           X A
        'PRON 6 1 ACC S N 1 2' : {'ending':'ud','age':'X','frequency':'A'},
        'PRON 6 0 ABL S N 1 1' : {'ending':'o','age':'X','frequency':'A'},
        'PRON 6 0 NOM P N 1 1' : {'ending':'a','age':'X','frequency':'A'},
        'PRON 6 0 GEN P N 1 4' : {'ending':'or','age':'X','frequency':'A'},
        #PRON 6 0 DAT P N 1 2 is                          X A
        'PRON 6 0 ACC P N 1 1' : {'ending':'a','age':'X','frequency':'A'},
        #PRON 6 0 ABL P N 1 2 is                          X A
        'PRON 6 2 NOM S M 1 2' : {'ending':'us','age':'B','frequency':'C'},   # OLD ipse
        'PRON 6 2 NOM S M 1 2' : {'ending':'os','age':'B','frequency':'E'},   # OLD ipse
        'PRON 6 2 NOM S N 1 2' : {'ending':'um','age':'X','frequency':'A'},
        'PRON 6 2 ACC S N 1 2' : {'ending':'um','age':'X','frequency':'A'},
        'PRON 6 2 NOM S N 1 2' : {'ending':'ud','age':'E','frequency':'E'},
        'PRON 6 2 ACC S N 1 2' : {'ending':'ud','age':'E','frequency':'E'} }

numeral_inflections = {
        'NUM 1 1 NOM S M CARD   1 2' : {'ending':'us','age':'X','frequency':'A'},
        'NUM 1 1 GEN S X CARD   1 3' : {'ending':'ius','age':'X','frequency':'A'},
        'NUM 1 1 DAT S X CARD   1 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 1 1 ACC S M CARD   1 2' : {'ending':'m','age':'X','frequency':'A'},
        'NUM 1 1 ABL S M CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 1 VOC S M CARD   1 1' : {'ending':'e','age':'X','frequency':'D'},
        'NUM 1 1 NOM S F CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 1 ACC S F CARD   1 2' : {'ending':'m','age':'X','frequency':'A'},
        'NUM 1 1 ABL S F CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 1 VOC S F CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 1 NOM S N CARD   1 2' : {'ending':'m','age':'X','frequency':'A'},
        'NUM 1 1 ACC S N CARD   1 2' : {'ending':'m','age':'X','frequency':'A'},
        'NUM 1 1 ABL S N CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 1 VOC S N CARD   1 2' : {'ending':'um','age':'X','frequency':'A'},
        'NUM 1 2 NOM P M CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 2 GEN P M CARD   1 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 1 2 GEN P M CARD   1 2' : {'ending':'um','age':'X','frequency':'B'},  # G&L 95 N2 
        'NUM 1 2 GEN P M CARD   1 2' : {'ending':'om','age':'B','frequency':'C'},  # G&L 95 N2 
        'NUM 1 2 DAT P M CARD   1 4' : {'ending':'obus','age':'X','frequency':'A'},
        'NUM 1 2 ACC P M CARD   1 2' : {'ending':'os','age':'X','frequency':'A'},
        'NUM 1 2 ACC P M CARD   1 1' : {'ending':'o','age':'B','frequency':'B'},  # G&L 95 N2 
        'NUM 1 2 ABL P M CARD   1 4' : {'ending':'obus','age':'X','frequency':'A'},
        'NUM 1 2 VOC P M CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 2 NOM P F CARD   1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 1 2 NOM P F CARD   1 1' : {'ending':'o','age':'X','frequency':'D'},  # G&L 95 N2 
        'NUM 1 2 NOM P F CARD   1 1' : {'ending':'a','age':'X','frequency':'E'},  # G&L 95 N2 
        'NUM 1 2 GEN P F CARD   1 4' : {'ending':'arum','age':'X','frequency':'A'},
        'NUM 1 2 DAT P F CARD   1 4' : {'ending':'abus','age':'X','frequency':'A'},
        'NUM 1 2 ACC P F CARD   1 2' : {'ending':'as','age':'X','frequency':'A'},
        'NUM 1 2 ABL P F CARD   1 4' : {'ending':'abus','age':'X','frequency':'A'},
        'NUM 1 2 VOC P F CARD   1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 1 2 NOM P N CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 2 GEN P N CARD   1 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 1 2 GEN P N CARD   1 2' : {'ending':'um','age':'X','frequency':'B'},  # G&L 95 N2 
        'NUM 1 2 GEN P N CARD   1 2' : {'ending':'om','age':'B','frequency':'C'},  # G&L 95 N2 
        'NUM 1 2 DAT P N CARD   1 4' : {'ending':'obus','age':'X','frequency':'A'},
        'NUM 1 2 ACC P N CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 2 ABL P N CARD   1 4' : {'ending':'obus','age':'X','frequency':'A'},
        'NUM 1 2 VOC P N CARD   1 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 1 3 NOM P C CARD   1 2' : {'ending':'es','age':'X','frequency':'A'},
        'NUM 1 3 GEN P X CARD   1 3' : {'ending':'ium','age':'X','frequency':'A'},
        'NUM 1 3 DAT P X CARD   1 4' : {'ending':'ibus','age':'X','frequency':'A'},
        'NUM 1 3 ACC P C CARD   1 2' : {'ending':'es','age':'X','frequency':'A'},
        'NUM 1 3 ACC P C CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},  # G&L 95, L  
        'NUM 1 3 ABL P X CARD   1 4' : {'ending':'ibus','age':'X','frequency':'A'},
        'NUM 1 3 VOC P C CARD   1 2' : {'ending':'es','age':'X','frequency':'A'},
        'NUM 1 3 NOM P N CARD   1 2' : {'ending':'ia','age':'X','frequency':'A'},
        'NUM 1 3 ACC P N CARD   1 2' : {'ending':'ia','age':'X','frequency':'A'},
        'NUM 1 3 VOC P N CARD   1 2' : {'ending':'ia','age':'X','frequency':'A'},
        'NUM 1 4 NOM P M CARD   1 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 1 4 GEN P M CARD   1 2' : {'ending':'um','age':'X','frequency':'A'},  # G&L 95 R  
        'NUM 1 4 GEN P M CARD   1 4' : {'ending':'orum','age':'X','frequency':'A'},  # C  
        'NUM 1 4 DAT P M CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 ACC P M CARD   1 2' : {'ending':'os','age':'X','frequency':'A'},
        'NUM 1 4 ABL P M CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 VOC P M CARD   1 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 1 4 NOM P F CARD   1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 1 4 GEN P F CARD   1 4' : {'ending':'arum','age':'X','frequency':'A'}, #G&L 95 R  
        'NUM 1 4 DAT P F CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 ACC P F CARD   1 2' : {'ending':'as','age':'X','frequency':'A'},
        'NUM 1 4 ABL P F CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 VOC P F CARD   1 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 1 4 NOM P N CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 4 GEN P N CARD   1 2' : {'ending':'um','age':'X','frequency':'A'}, #G&L 95 R  
        'NUM 1 4 DAT P N CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 ACC P N CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 4 ABL P N CARD   1 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 1 4 VOC P N CARD   1 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 2 0 X   X X CARD   1 0' : {'ending':'','age':'X','frequency':'A'},
        'NUM 0 0 NOM S M ORD    2 2' : {'ending':'us','age':'X','frequency':'A'},
        'NUM 0 0 GEN S M ORD    2 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 DAT S M ORD    2 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 0 0 ACC S M ORD    2 2' : {'ending':'um','age':'X','frequency':'A'},
        'NUM 0 0 ABL S M ORD    2 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 0 0 VOC S M ORD    2 1' : {'ending':'e','age':'X','frequency':'A'},
        'NUM 0 0 NOM P M ORD    2 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 GEN P M ORD    2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 0 0 DAT P M ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 ACC P M ORD    2 2' : {'ending':'os','age':'X','frequency':'A'},
        'NUM 0 0 ABL P M ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 VOC P M ORD    2 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 NOM S F ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 GEN S F ORD    2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 DAT S F ORD    2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 ACC S F ORD    2 2' : {'ending':'am','age':'X','frequency':'A'},
        'NUM 0 0 ABL S F ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 VOC S F ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 NOM P F ORD    2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 GEN P F ORD    2 4' : {'ending':'arum','age':'X','frequency':'A'},
        'NUM 0 0 DAT P F ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 ACC P F ORD    2 2' : {'ending':'as','age':'X','frequency':'A'},
        'NUM 0 0 ABL P F ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 VOC P F ORD    2 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 NOM S N ORD    2 2' : {'ending':'um','age':'X','frequency':'A'},
        'NUM 0 0 GEN S N ORD    2 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 DAT S N ORD    2 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 0 0 ACC S N ORD    2 2' : {'ending':'um','age':'X','frequency':'A'},
        'NUM 0 0 ABL S N ORD    2 1' : {'ending':'o','age':'X','frequency':'A'},
        'NUM 0 0 VOC S N ORD    2 2' : {'ending':'um','age':'X','frequency':'A'},
        'NUM 0 0 NOM P N ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 GEN P N ORD    2 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 0 0 DAT P N ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 ACC P N ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 ABL P N ORD    2 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 VOC P N ORD    2 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 NOM P M DIST   3 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 GEN P C DIST   3 2' : {'ending':'um','age':'X','frequency':'A'}, # G&L M/N but Caesar F  
        'NUM 0 0 GEN P M DIST   3 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 0 0 DAT P X DIST   3 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 ACC P M DIST   3 2' : {'ending':'os','age':'X','frequency':'A'},
        'NUM 0 0 ABL P X DIST   3 2' : {'ending':'is','age':'X','frequency':'A'},
        'NUM 0 0 VOC P M DIST   3 1' : {'ending':'i','age':'X','frequency':'A'},
        'NUM 0 0 NOM P F DIST   3 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 GEN P F DIST   3 4' : {'ending':'arum','age':'X','frequency':'A'},
        'NUM 0 0 ACC P F DIST   3 2' : {'ending':'as','age':'X','frequency':'A'},
        'NUM 0 0 VOC P F DIST   3 2' : {'ending':'ae','age':'X','frequency':'A'},
        'NUM 0 0 NOM P N DIST   3 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 GEN P N DIST   3 4' : {'ending':'orum','age':'X','frequency':'A'},
        'NUM 0 0 ACC P N DIST   3 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 0 0 VOC P N DIST   3 1' : {'ending':'a','age':'X','frequency':'A'},
        'NUM 1 1 X   X X ADVERB 4 0' : {'ending':'','age':'X','frequency':'A'},
        'NUM 1 2 X   X X ADVERB 4 0' : {'ending':'','age':'X','frequency':'A'},
        'NUM 1 3 X   X X ADVERB 4 0' : {'ending':'','age':'X','frequency':'A'},
        'NUM 1 4 X   X X ADVERB 4 3' : {'ending':'ies','age':'X','frequency':'A'},
        'NUM 1 4 X   X X ADVERB 4 4' : {'ending':'iens','age':'B','frequency':'A'},
        'NUM 2 0 X   X X ADVERB 4 3' : {'ending':'ies','age':'X','frequency':'A'},
        'NUM 2 0 X   X X ADVERB 4 4' : {'ending':'iens','age':'B','frequency':'A'} }

# End
