# Python definitions useful for interpreting and working with dictionary entries, inflections, etc.

import os
import os.path
import csv
from dataclasses import dataclass
from pywords.matchfilter import MatchFilter


########################
####### GLOBALS ########

# MAIN INFLECTIONS DICTIONARY
inflections = {'N': [], 'ADJ': [], 'V': [], 'VPAR': [], 'SUPINE': [], 'PRON': [], 'NUM': [], 'ADV': [], 'PREP': []}
# Inflections cache, each has the decl/var as key (e.g. "1 1")
# This makes it faster to lookup possible endings, without handling all the default cases (e.g. "1 0", "0 0", which
# are only used internally, not in the DICTLINE file)
_noun_inflections_cached = {}
_adj_inflections_cached = {}
_verb_inflections_cached = {}
_num_inflections_cached = {}
_pron_inflections_cached = {}

# For convenience, here are dictionaries converting things
parts_of_speech = {
    'N': 'noun',
    'PRON': 'pronoun',
    'ADV': 'adverb',
    'ADJ': 'adjective',
    'NUM': 'number',
    'V': 'verb',
    'VPAR': 'verb participle',
    'INTERJ': 'interjection',
    'CONJ': 'conjunction',
    'SUPINE': 'supine',
    'PREP': 'preposition',
    'PACK': 'pack (internal use only)',
    'TACKON': 'tackon (internal use only)',
    'PREFIX': 'prefix (internal use only)',
    'SUFFIX': 'suffix (internal use only)',
    'X': ''}
cases = {
    'NOM': 'nominative',
    'VOC': 'vocative',
    'GEN': 'genitive',
    'DAT': 'dative',
    'ACC': 'accusative',
    'LOC': 'locative',
    'ABL': 'ablative',
    'X': ''}
genders = {
    'M': 'masculine',
    'F': 'feminine',
    'N': 'neuter',
    'C': 'masculine/feminine',  # (masc/fem depending on context)
    'X': ''}
persons = {
    '0': '',
    '1': 'first person',
    '2': 'second person',
    '3': 'third person'}
numbers = {
    'S': 'singular',
    'P': 'plural',
    'X': ''}
tenses = {
    'PRES': 'present',
    'IMPF': 'imperfect',
    'PERF': 'perfect',
    'FUT': 'future',
    'FUTP': 'future perfect',
    'PLUP': 'pluperfect',
    'INF': 'infinitive',
    'X': ''}
voices = {
    'ACTIVE': 'active',
    'PASSIVE': 'passive',
    'X': ''}
moods = {
    'IND': 'indicative',
    'SUB': 'subjunctive',
    'IMP': 'imperative',
    'INF': 'infinitive',
    'PPL': 'participle',
    'X': ''}
comparisons = {
    'POS': 'positive',
    'COMP': 'comparative',
    'SUPER': 'superlative',
    'X': ''}

noun_declensions = {
    '1': 'first declension',
    '2': 'second declension',
    '3': 'third declension',
    '4': 'fourth declension',
    '5': 'fifth declension',
    '9': 'indeclinable or undeclined'}

verb_conjugations = {
    '0': 'first conjugation',
    '1': 'first conjugation',
    '2': 'second conjugation',
    '3': 'third conjugation',
    '5': 'irregular',
    '6': 'irregular',
    '7': 'defective',
    '8': 'irregular',
    '9': 'indeclinable or undeclined'}

adj_declensions = {
    '0': 'first/second declension',
    '1': 'first/second declension',
    '2': 'Greek declension',
    '3': 'third declension',
    '9': 'indeclinable or undeclined'}

noun_kinds = {
    'S': 'singular only',
    'M': 'plural or multiple only',
    'A': 'abstract idea',
    'G': 'group/collective name',
    'N': 'proper name',
    'P': 'person',
    'T': 'thing',
    'L': 'locale',
    'W': 'where',
    'X': ''}
pronoun_kinds = {
    'PERS': 'personal',
    'REL': 'relative',
    'REFLEX': 'reflexive',
    'DEMONS': 'demonstrative',
    'INTERR': 'interrogative',
    'INDEF': 'indefinite',
    'ADJECT': 'adjectival',
    'X': ''}

verb_kinds = {
    'TO_BE': 'conjugated like sum, esse',
    'TO_BEING': 'conjugated like compound of sum, esse',
    'GEN': 'takes genitive',
    'DAT': 'takes dative',
    'ABL': 'takes ablative',
    'TRANS': 'transitive',
    'INTRANS': 'intransitive',
    'IMPERS': 'impersonal',
    'DEP': 'deponent',
    'SEMIDEP': 'semideponent',
    'PERFDEF': 'perfect definite',
    'X': ''}

number_kinds = {
    'X': '',
    'CARD': 'cardinal',
    'ORD': 'ordinal',
    'DIST': 'distributive',
    'ADVERB': 'numeral adverb'}

ages = {
    'A': 'archaic',  # Very early forms, obsolete by classical times
    'B': 'early',  # Early Latin, pre-classical, used for effect/poetry
    'C': 'classical',  # Limited to classical (~150 BC - 200 AD)
    'D': 'late',  # Late, post-classical (3rd-5th centuries)
    'E': 'later',  # Latin not in use in Classical times (6-10) Christian
    'F': 'medieval',  # Medieval (11th-15th centuries)
    'G': 'scholastic',  # Latin post 15th - Scholarly/Scientific   (16-18)
    'H': 'modern',  # Coined recently, words for new things (19-20)
    'X': 'common/unknown'}  # In use throughout the ages/unknown #the default
areas = {
    'A': 'Agriculture, Flora, Fauna, Land, Equipment, Rural',
    'B': 'Biological, Medical, Body Parts',
    'D': 'Drama, Music, Theater, Art, Painting, Sculpture',
    'E': 'Ecclesiastic, Biblical, Religious',
    'G': 'Grammar, Retoric, Logic, Literature, Schools',
    'L': 'Legal, Government, Tax, Financial, Political, Titles',
    'P': 'Poetic',
    'S': 'Science, Philosophy, Mathematics, Units/Measures',
    'T': 'Technical, Architecture, Topography, Surveying',
    'W': 'War, Military, Naval, Ships, Armor',
    'Y': 'Mythology',
    'X': ''}

geographies = {
    'A': 'Africa',
    'B': 'Britian',
    'C': 'China',
    'D': 'Scandinavia',
    'E': 'Egypt',
    'F': 'France, Gaul',
    'G': 'Germany',
    'H': 'Greece',
    'I': 'Italy, Rome',
    'J': 'India',
    'K': 'Balkans',
    'N': 'Netherlands',
    'P': 'Persia',
    'Q': 'Near East',
    'R': 'Russia',
    'S': 'Spain, Iberia',
    'U': 'Eastern Europe',
    'X': ''}

dict_frequencies = {
    'A': 'very frequent',  # Very frequent, in all Elementry Latin books, top 1000+ words
    'B': 'frequent',  # Frequent, next 2000+ words
    'C': 'common',  # For Dictionary, in top 10,000 words
    'D': 'less common',  # For Dictionary, in top 20,000 words
    'E': 'uncommon',  # 2 or 3 citations
    'F': 'very rare',  # Having only single citation in OLD or L+S
    'I': 'inscription',  # Only citation is inscription
    'M': 'graffiti',  # Presently not much used
    'N': 'Pliny',  # Things that appear only in Pliny Natural History
    'X': ''}

inflection_frequencies = {
    'A': 'most freq',  # Very frequent, the most common
    'B': 'sometimes',  # sometimes, a not unusual VARIANT
    'C': 'uncommon',  # occasionally seen
    'D': 'infrequent',  # recognizable variant, but unlikely
    'E': 'rare',  # for a few cases, very unlikely
    'F': 'very rare',  # singular examples,
    'I': '',  # Presently not used
    'M': '',  # Presently not used
    'N': '',  # Presently not used
    'X': 'unknown'}

source_types = {
    'X': 'General or unknown or too common to say',
    'A': '',
    'B': 'C.H.Beeson, A Primer of Medieval Latin, 1925 (Bee)',
    'C': 'Charles Beard, Cassell\'s Latin Dictionary 1892 (CAS)',
    'D': 'J.N.Adams, Latin Sexual Vocabulary, 1982 (Sex)',
    'E': 'L.F.Stelten, Dictionary of Eccles. Latin, 1995 (Ecc)',
    'F': 'Roy J. Deferrari, Dictionary of St. Thomas Aquinas, 1960 (DeF)',
    'G': 'Gildersleeve + Lodge, Latin Grammar 1895 (G+L)',
    'H': 'Collatinus Dictionary by Yves Ouvrard',
    'I': 'Leverett, F.P., Lexicon of the Latin Language, Boston 1845',
    'J': '',
    'K': 'Calepinus Novus, modern Latin, by Guy Licoppe (Cal)',
    'L': 'Lewis, C.S., Elementary Latin Dictionary 1891',
    'M': 'Latham, Revised Medieval Word List, 1980',
    'N': 'Lynn Nelson, Wordlist',
    'O': 'Oxford Latin Dictionary, 1982 (OLD)',
    'P': 'Souter, A Glossary of Later Latin to 600 A.D., Oxford 1949',
    'Q': 'Other, cited or unspecified dictionaries',
    'R': 'Plater & White, A Grammar of the Vulgate, Oxford 1926',
    'S': 'Lewis and Short, A Latin Dictionary, 1879 (L+S)',
    'T': 'Found in a translation - no dictionary reference',
    'U': 'Du Cange',
    'V': 'Vademecum in opus Saxonis - Franz Blatt (Saxo)',
    'W': 'Whitaker\'s personal guess',
    'Y': 'Temp special code',
    'Z': 'Sent by user - no dictionary reference'}


# TODO Are these used? Is u/v causing problems?
irreg_sum = ['svm', 'es', 'est', 'svmvs', 'estis', 'svnt', 'eram', 'eras', 'erat', 'eramvs', 'eratis', 'erant',
             'ero', 'eris', 'erit', 'erimvs', 'eritis', 'ervnt', 'fvi', 'fvisti', 'fvit', 'fvimvs', 'fvistis',
             'fvervnt', 'fveram', 'fveras', 'fverat', 'fveramvs', 'fveratis', 'fverant', 'fvero', 'fveris', 'fverit',
             'fverimvs', 'fveritis', 'fvervnt', 'sis', 'sit', 'simvs', 'sitis', 'sint', 'essem', 'esses', 'esset',
             'essemvs', 'essetis', 'essent', 'fverim', 'fveris', 'fverit', 'fverimvs', 'fveritis', 'fverint',
             'fvissem', 'fvisses', 'fvisset', 'fvissemvs', 'fvissetis', 'fvissent']

# @global
# OR'd List of Endings
endings_list_uvij = [
    '', 'a', 'abam', 'abamini', 'abamur', 'abamus', 'abant', 'abantur', 'abar',
    'abare', 'abaris', 'abas', 'abat', 'abatis', 'abatur', 'abere', 'aberis',
    'abimini', 'abimur', 'abimus', 'abis', 'abit', 'abitis', 'abitur', 'abo',
    'abor', 'abunt', 'abuntur', 'abus', 'ac', 'ad', 'ae', 'aec', 'ai', 'am',
    'amini', 'amur', 'amus', 'an', 'anc', 'anda', 'andae', 'andam', 'andarum',
    'andas', 'ande', 'andi', 'andis', 'ando', 'andorum', 'andos', 'andum', 'andus',
    'ans', 'ant', 'ante', 'antem', 'antes', 'anti', 'antia', 'antibus', 'antis',
    'antium', 'anto', 'antor', 'antum', 'antur', 'ar', 'are', 'arem', 'aremini',
    'aremur', 'aremus', 'arent', 'arentur', 'arer', 'arere', 'areris', 'ares',
    'aret', 'aretis', 'aretur', 'ari', 'arier', 'aris', 'arum', 'arun', 'as', 'at',
    'ate', 'atis', 'ato', 'ator', 'atote', 'atur', 'bam', 'bamini', 'bamur',
    'bamus', 'bant', 'bantur', 'bar', 'bare', 'baris', 'bas', 'bat', 'batis',
    'batur', 'bere', 'beris', 'berit', 'bimini', 'bimur', 'bimus', 'bis', 'bit',
    'bitis', 'bitur', 'bo', 'bor', 'bunt', 'buntur', 'd', 'e', 'eam', 'eamini',
    'eamur', 'eamus', 'eant', 'eantur', 'ear', 'eare', 'earis', 'eas', 'eat',
    'eatis', 'eatur', 'ebam', 'ebamini', 'ebamur', 'ebamus', 'ebant', 'ebantur',
    'ebar', 'ebare', 'ebaris', 'ebas', 'ebat', 'ebatis', 'ebatur', 'ebere',
    'eberis', 'ebimini', 'ebimur', 'ebimus', 'ebis', 'ebit', 'ebitis', 'ebitur',
    'ebo', 'ebor', 'ebunt', 'ebuntur', 'ebus', 'ed', 'ei', 'eis', 'em', 'eme',
    'emini', 'emur', 'emus', 'en', 'enda', 'endae', 'endam', 'endarum', 'endas',
    'ende', 'endi', 'endis', 'endo', 'endorum', 'endos', 'endum', 'endus', 'ens',
    'ent', 'ente', 'entem', 'entes', 'enti', 'entia', 'entibus', 'entis', 'entium',
    'ento', 'entor', 'entum', 'entur', 'enus', 'eo', 'eor', 'er', 'eram', 'eramus',
    'erant', 'eras', 'erat', 'eratis', 'ere', 'erem', 'eremini', 'eremur', 'eremus',
    'erent', 'erentur', 'erer', 'erere', 'ereris', 'eres', 'eret', 'eretis',
    'eretur', 'eri', 'erier', 'erim', 'erimus', 'erint', 'eris', 'erit', 'eritis',
    'ero', 'erum', 'erunt', 'es', 'ese', 'esse', 'essem', 'essemus', 'essent',
    'esses', 'esset', 'essetis', 'est', 'este', 'estis', 'esto', 'estote', 'et',
    'ete', 'etis', 'eto', 'etor', 'etote', 'etur', 'eu', 'fore', 'forem', 'foremus',
    'forent', 'fores', 'foret', 'foretis', 'i', 'ia', 'iant', 'ias', 'iat', 'ibam',
    'ibamus', 'ibant', 'ibas', 'ibat', 'ibatis', 'ibe', 'ibei', 'ibi', 'ibus', 'ic',
    'id', 'iens', 'ier', 'iere', 'ieri', 'ies', 'ihi', 'ii', 'iis', 'im', 'imini',
    'imur', 'imus', 'in', 'int', 'ire', 'irem', 'iremini', 'iremur', 'iremus',
    'irent', 'irentur', 'irer', 'irere', 'ireris', 'ires', 'iret', 'iretis',
    'iretur', 'iri', 'irier', 'iris', 'is', 'isse', 'issem', 'issemus', 'issent',
    'isses', 'isset', 'issetis', 'isti', 'istis', 'it', 'ite', 'itis', 'ito',
    'itor', 'itote', 'itur', 'ium', 'ius', 'jus', 'le', 'lem', 'lemus', 'lent',
    'les', 'let', 'letis', 'ma', 'mae', 'mam', 'marum', 'mas', 'me', 'mi', 'mini',
    'mis', 'mo', 'morum', 'mos', 'mum', 'mur', 'mus', 'o', 'obis', 'obus', 'oc',
    'od', 'oe', 'om', 'on', 'or', 'ora', 'ore', 'orem', 'ores', 'ori', 'oribus',
    'oris', 'orum', 'orun', 'os', 're', 'rem', 'remini', 'remur', 'remus', 'rent',
    'rentur', 'rer', 'rere', 'reris', 'res', 'ret', 'retis', 'retur', 'ri', 'rier',
    'ris', 's', 'se', 'sem', 'semus', 'sent', 'ses', 'set', 'setis', 'setur', 't',
    'te', 'tis', 'to', 'tor', 'tote', 'tur', 'u', 'ua', 'ubus', 'uc', 'ud', 'ui',
    'um', 'um', 'umus', 'un', 'unc', 'unda', 'undae', 'undam', 'undarum', 'undas',
    'unde', 'undi', 'undis', 'undo', 'undorum', 'undos', 'undum', 'undus', 'unt',
    'unte', 'untem', 'untes', 'unti', 'untia', 'untibus', 'untis', 'untium', 'unto',
    'untor', 'untur', 'ura', 'urae', 'uram', 'urarum', 'uras', 'ure', 'uri', 'uris',
    'uro', 'urorum', 'uros', 'urum', 'urus', 'us', 'ut', 'uum', 'uus', 'yn', 'yos'
]
endings_list_vi = [e.replace('j', 'i').replace('u', 'v') for e in endings_list_uvij]

####### /GLOBALS #######
########################


#####################################
####### DICTIONARY ENTRIES ##########

class DictlineBaseEntry:
    """
    dictline entry
    Base class for dictline entries, providing dictionary codes
    """

    def __init__(self, pos: str, age: str, area: str, geog: str, freq: str, src: str, senses: str):
        # These are required by every entry, cannot be empty string
        if pos in parts_of_speech.keys():
            self.pos = pos
        else:
            raise ValueError("Unexpected dictline entry part of speech '{0}'".format(pos))
        if age in ages.keys():
            self.age = age
        else:
            raise ValueError("Unexpected dictline entry age '{0}'".format(age))
        if area in areas.keys():
            self.area = area
        else:
            raise ValueError("Unexpected dictline entry subject area '{0}'".format(area))
        if geog in geographies.keys():
            self.geog = geog
        else:
            raise ValueError("Unexpected dictline entry geography '{0}'".format(geog))
        if freq in dict_frequencies.keys():
            self.freq = freq
        else:
            raise ValueError("Unexpected dictline entry frequency '{0}'".format(freq))
        if src in source_types.keys():
            self.src = src
        else:
            raise ValueError("Unexpected dictline entry source '{0}'".format(src))
        if senses:  # If not None or ''
            self.senses = senses
        else:
            raise ValueError("Dictline entry with empty sense.")

    def get_part_of_speech(self):
        if self.pos is not None:
            return parts_of_speech[self.pos]
        return None

    def get_age(self):
        if self.age is not None:
            return ages[self.age]
        return None

    def get_area(self):
        if self.area is not None:
            return areas[self.area]
        return None

    def get_geography(self):
        if self.geog is not None:
            return geographies[self.geog]
        return None

    def get_frequency(self):
        if self.freq is not None:
            return dict_frequencies[self.freq]
        return None

    def get_source(self):
        if self.src is not None:
            return source_types[self.src]
        return None

    def get_senses(self):
        if self.senses is not None:
            return self.senses
        return None


class DictlineNounEntry(DictlineBaseEntry):
    """
    dictline noun entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos: str, decl: str, variant: str, gender: str, noun_kind: str, age: str, area: str, geog: str,
                 freq: str, src: str, senses: str):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # declension variant (see INFLECTS.LAT)
        if gender in genders.keys():
            self.gender = gender
        else:
            raise ValueError( "Attempting to initialize gender as '{0}' but this is not a valid gender.".format(gender))

        if noun_kind in noun_kinds.keys():
            self.noun_kind = noun_kind

    def get_declension(self):
        return noun_declensions[self.decl]

    def get_gender(self):
        return genders[self.gender]

    def get_noun_kind(self):
        return noun_kinds[self.noun_kind]

    def __repr__(self):
        return "DictlineNounEntry(decl='" + self.decl + "', variant='" + self.variant + \
               "', gender='" + self.gender + "', noun_kind='" + self.noun_kind + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineNounEntry):
            return False
        return self.pos == other.pos and \
               self.decl == other.decl and \
               self.variant == other.variant and \
               self.gender == other.gender and \
               self.noun_kind == other.noun_kind and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlineVerbEntry(DictlineBaseEntry):
    """
    dictline verb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos: str, conj: str, variant: str, verb_kind: str, age: str, area: str, geog: str, freq: str,
                 src: str, senses: str):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.conj = conj  # conjugation
        self.variant = variant  # conjugation variant (see INFLECTS.LAT)
        if verb_kind == '' or verb_kind in verb_kinds.keys():
            self.verb_kind = verb_kind
        else:
            raise ValueError("Attempting to initialize verb kind as '{0}' but this is not a valid verb kind.".format(verb_kind))

    def get_conjugation(self):
        return verb_conjugations[self.conj]

    def get_verb_kind(self):
        return verb_kinds[self.verb_kind]

    def __repr__(self):
        return "DictlineVerbEntry(conj='" + self.conj + "', variant='" + self.variant + \
               "', verb_kind='" + self.verb_kind + "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineVerbEntry):
            return False
        return self.pos == other.pos and \
               self.conj == other.conj and \
               self.variant == other.variant and \
               self.verb_kind == other.verb_kind and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses


class DictlineAdjectiveEntry(DictlineBaseEntry):
    """
    dictline adjective entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, decl, variant, comparison, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # adjective variant (see INFLECTS.LAT)
        if comparison in comparisons.keys():
            self.comparison = comparison
        else:
            raise ValueError("Attempting to initialize adjective with unrecognized comparison '{0}'".format(comparison))

    def get_declension(self):
        return adj_declensions[self.decl]

    def get_comparison(self):
        return comparisons[self.comparison]

    def __repr__(self):
        return "DictlineAdjectiveEntry(decl='" + self.decl + "', variant='" + self.variant + \
               "', comparison='" + self.comparison + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineAdjectiveEntry):
            return False
        return self.pos == other.pos and \
               self.decl == other.decl and \
               self.variant == other.variant and \
               self.comparison == other.comparison and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlineAdverbEntry(DictlineBaseEntry):
    """
    dictline adverb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, comparison, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        if comparison in comparisons.keys():
            self.comparison = comparison
        else:
            raise ValueError("Attempting to initialize adjective with unrecognized comparison '{0}'".format(comparison))

    def get_comparison(self):
        return comparisons[self.comparison]

    def __repr__(self):
        return "DictlineAdverbEntry(comparison='" + self.comparison + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineAdverbEntry):
            return False
        return self.pos == other.pos and \
               self.comparison == other.comparison and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlinePronounEntry(DictlineBaseEntry):
    """
    dictline pronoun (and pack) entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.

    NOTE: 'pos' can be PRON or PACK
    """

    def __init__(self, pos, decl, variant, pronoun_kind, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension TODO
        self.variant = variant
        if pos != 'PACK':
            if pronoun_kind in pronoun_kinds.keys():
                self.pronoun_kind = pronoun_kind
            else:
                raise ValueError("Attempting to initialize pronoun kind with unrecognized kind '{0}'".format(pronoun_kind))
        else:
            self.pronoun_kind = None

    def __repr__(self):
        return "DictlinePronounEntry(decl='" + self.decl + "', variant='" + self.variant + \
               "', pronoun_kind='" + self.pronoun_kind + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlinePronounEntry):
            return False
        return self.pos == other.pos and \
               self.decl == other.decl and \
               self.variant == other.variant and \
               self.pronoun_kind == other.pronoun_kind and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlineConjunctionEntry(DictlineBaseEntry):
    """
    dictline conjunction entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)

    def __repr__(self):
        return "DictlineConjunctionEntry(pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineConjunctionEntry):
            return False
        return self.pos == other.pos and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlineInterjectionEntry(DictlineBaseEntry):
    """
    dictline interjection entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)

    def __repr__(self):
        return "DictlineInterjectionEntry(pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineInterjectionEntry):
            return False
        return self.pos == other.pos and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlinePrepositionEntry(DictlineBaseEntry):
    """
    dictline preposition entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, case, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        if case in ['ACC','ABL','GEN']:
            self.case = case
        else:
            raise ValueError("Unexpected preposition auxiliary case '{0}', valid options are ACC, ABL, and GEN".format(case))

    def get_case(self):
        return cases[self.case]

    def __repr__(self):
        return "DictlinePrepositionEntry(case='" + self.case + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlinePrepositionEntry):
            return False
        return self.pos == other.pos and \
              self.case == other.case and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


class DictlineNumberEntry(DictlineBaseEntry):
    """
    dictline number entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    """

    def __init__(self, pos, decl, variant, number_kind, number, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # adjective variant (see INFLECTS.LAT)
        self.number_kind = number_kind
        if number_kind in number_kinds.keys():
            self.number_kind = number_kind
        else:
            raise ValueError("Attempting to initialize number kind with unrecognized kind '{0}'".format(number_kind))
        self.number = number

    def get_declension(self):
        return adj_declensions[self.decl]

    def get_number_kind(self):
        return number_kinds[self.number_kind]

    def get_number(self):
        return self.number

    def __repr__(self):
        return "DictlineNumberEntry(decl='" + self.decl + "', variant='" + self.variant + \
               "', number='" + self.number + "', number_kind='" + self.number_kind + \
               "', pos='" + self.pos + "', age='" + self.age + "', freq='" + self.freq + \
               "', area='" + self.area + "', geog='" + self.geog + "', src='" + self.src + \
               "', senses='" + self.senses + "')"

    def __eq__(self,other):
        if not isinstance(other,DictlineNumberEntry):
            return False
        return self.pos == other.pos and \
               self.decl == other.decl and \
               self.variant == other.variant and \
               self.number_kind == other.number_kind and \
               self.age == other.age and \
               self.area == other.area and \
               self.geog == other.geog and \
               self.freq == other.freq and \
               self.src == other.src and \
               self.senses == other.senses

    def __hash__(self):
        return hash(repr(self))


def build_dictline_entry(dictline_row):
    """
    Accepts a dictline row and dictionary of columns and returns a DictlineEntry subclass object
    """
    pos = dictline_row['dl_pos']
    senses = dictline_row['dl_senses']
    age = dictline_row['dl_age']
    area = dictline_row['dl_area']
    geography = dictline_row['dl_geography']
    frequency = dictline_row['dl_frequency']
    source = dictline_row['dl_source']

    if pos == 'N':
        return DictlineNounEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                 decl=dictline_row['dl_type'],
                                 variant=dictline_row['dl_variant'],
                                 gender=dictline_row['dl_gender'],
                                 noun_kind=dictline_row['dl_kind']
                                 )
    if pos == 'ADJ':
        return DictlineAdjectiveEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                      decl=dictline_row['dl_type'],
                                      variant=dictline_row['dl_variant'],
                                      comparison=dictline_row['dl_comparison']
                                      )
    if pos == 'V':
        return DictlineVerbEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                 conj=dictline_row['dl_type'],
                                 variant=dictline_row['dl_variant'],
                                 verb_kind=dictline_row['dl_kind']
                                 )
    if pos == 'ADV':
        return DictlineAdverbEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                   comparison=dictline_row['dl_comparison']
                                   )
    if pos == 'CONJ':
        return DictlineConjunctionEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses
                                        )
    if pos in ['PRON', 'PACK']:
        return DictlinePronounEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                    decl=dictline_row['dl_type'],
                                    variant=dictline_row['dl_variant'],
                                    pronoun_kind=dictline_row['dl_kind']
                                    )
    if pos == 'NUM':
        return DictlineNumberEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                   decl=dictline_row['dl_type'],
                                   variant=dictline_row['dl_variant'],
                                   number_kind=dictline_row['dl_kind'],
                                   number=None  # In case we want to include numerical data later
                                   )
    if pos == 'PREP':
        return DictlinePrepositionEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses,
                                        case=dictline_row['dl_aux_case']
                                        )
    if pos == 'INTERJ':
        return DictlineInterjectionEntry(pos=pos, age=age, area=area, geog=geography, freq=frequency, src=source, senses=senses
                                         )


#####################################
######### INFLECTIONS ###############

# NOTE: To match inflections, simply create a partially filled Infl object, and use a list
# comprehension to find matches, as in this example:
#   testnoun = NounInfl(decl='1',case='NOM',number='S')
#   noun_matches = [n for n in inflections['N'] if testnoun.matches(n)]
#
# Note the order of the matches() method: use the template inflection (testnoun)
# to check if the full inflections matches (inflections['N'])
class NounInfl:
    """
    Structural version of noun inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', decl='', variant='', case='', number='', gender='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.variant = buildstr[8]
            self.case = buildstr[10:13].strip()
            self.number = buildstr[14]
            self.gender = buildstr[16]
            self.stem = buildstr[19]
            self.ending_uvij = buildstr[23:32].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[33]
            self.frequency = buildstr[35]
        else:
            self.decl = decl
            self.variant = variant
            if case == '' or case in cases.keys():
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender in genders.keys():
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        match = True
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' noun'
        return inflstr.replace('  ', ' ')

    def overrides(self,other):
        """
        Return True if this inflection has higher priority than `other` inflection

        For NounInfl, priority goes to inflection with variant other than 0
        Inflections are comparable if declension, case, number, and gender are the same

        NOTE: Returning False does not mean other inflection has priority
        age and frequency are checked

        TODO: Are there cases when gender is overridden? e.g. inflection gender 'M' overrides 'C'
        """
        if not isinstance(other,NounInfl):
            return False
        # If these inflections are comparable, check if we have priority
        if self.decl == other.decl:
            if self.case == other.case and \
                    self.number == other.number and \
                    self.gender == other.gender and \
                    self.age == other.age and \
                    self.frequency == other.frequency:
                if other.variant == '0' and self.variant != '0':
                    return True
        return False

    def __repr__(self):
        return "NounInfl(decl='" + self.decl + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + self.age + \
               "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,NounInfl):
            return False
        return self.decl == other.decl and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class AdjectiveInfl:
    """
    Structural version of adjective inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', decl='', variant='', case='', number='', gender='', comparison='', stem='', ending=None,
                 age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.variant = buildstr[8]
            self.case = buildstr[10:13].strip()
            self.number = buildstr[14]
            self.gender = buildstr[16]
            self.comparison = buildstr[18:24].strip()
            self.stem = buildstr[24]
            self.ending_uvij = buildstr[28:38].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[38]
            self.frequency = buildstr[40]
        else:
            self.decl = decl
            self.variant = variant
            if case == '' or case in cases.keys():
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender in genders.keys():
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if comparison == '' or comparison in comparisons:
                self.comparison = comparison
            else:
                raise ValueError("Unexpected inflection ")
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        match = True
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.comparison:
            if infl.comparison != self.comparison:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' ' + genders[self.gender] + ' '
        if not less:
            inflstr += 'of ' + adj_declensions[self.decl] + ' '
            if self.comparison:
                inflstr += comparisons[self.comparison] + ' '
            inflstr += 'adjective'
        return inflstr.replace('  ', ' ')

    def overrides(self,other):
        """
        Return True if this inflection has higher priority than `other` inflection

        For AdjectiveInfl, priority goes to inflection with variant other than 0, unless decl=0
        Inflections are comparable if declension, case, number, gender, and comparison are the same

        NOTE: Returning False does not mean other inflection has priority
        NOTE: age and frequency are checked
        """
        if not isinstance(other,AdjectiveInfl):
            return False
        # If these inflections are comparable, check if we have priority
        if self.decl == other.decl or (self.decl != '0' and other.decl == '0'):
            if self.case == other.case and \
                    self.number == other.number and \
                    self.gender == other.gender and \
                    self.comparison == other.comparison and \
                    self.age == other.age and \
                    self.frequency == other.frequency:
                if other.variant == '0' and self.variant != '0':
                    return True
        return False

    def __repr__(self):
        return "AdjectiveInfl(decl='" + self.decl + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', comparison='" + self.comparison + \
               "', stem='" + self.stem + "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + \
               "', age='" + self.age + "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,AdjectiveInfl):
            return False
        return self.decl == other.decl and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.comparison == other.comparison and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class VerbInfl:
    """
    Structural version of verb inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', conj='', variant='', tense='', voice='', mood='', person='', number='', stem='',
                 ending=None, age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.conj = buildstr[6]
            self.variant = buildstr[8]
            self.tense = buildstr[10:16].strip()
            self.voice = buildstr[16:24].strip()
            self.mood = buildstr[24:29].strip()
            self.person = buildstr[29]
            self.number = buildstr[31]
            self.stem = buildstr[34]
            self.ending_uvij = buildstr[38:52].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[52]
            self.frequency = buildstr[54]
        else:
            self.conj = conj
            self.variant = variant
            if tense == '' or tense in tenses:
                self.tense = tense
            else:
                raise ValueError("Unexpected inflection tense '{0}' during initialization.".format(tense))
            if voice == '' or voice in voices:
                self.voice = voice
            else:
                raise ValueError("Unexpected inflection voice '{0}' during initialization.".format(voice))
            if mood == '' or mood in moods:
                self.mood = mood
            else:
                raise ValueError("Unexpected inflection mood '{0}' during initialization.".format(mood))
            if person == '' or person in persons.keys():
                self.person = person
            else:
                raise ValueError("Unexpected inflection person '{0}' during initialization.".format(person))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.conj:
            if infl.conj != self.conj:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.tense:
            if infl.tense != self.tense:
                return False
        if self.voice:
            if infl.voice != self.voice:
                return False
        if self.mood:
            if infl.mood != self.mood:
                return False
        if self.person:
            if infl.person != self.person:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += persons[self.person] + ' ' + moods[self.mood] + ' ' + voices[self.voice] + ' '
        inflstr += tenses[self.tense] + ' tense '
        if not less:
            inflstr += 'of ' + verb_conjugations[self.conj] + ' verb'
        return inflstr.replace('  ', ' ')

    def overrides(self,other):
        """
        Return True if this inflection has higher priority than `other` inflection

        For VerbInflection, priority goes to inflection with variant other than 0
        Inflections are comparable if

        NOTE: Returning False does not mean other inflection has priority
        NOTE: age and frequency are checked
        """
        if not isinstance(other,VerbInfl):
            return False
        # If these inflections are comparable, check if we have priority
        if self.conj == other.conj or (self.conj != '0' and other.conj == '0'):
            if self.tense == other.tense and \
                    self.number == other.number and \
                    self.person == other.person and \
                    self.voice == other.voice and \
                    self.mood == other.mood and \
                    self.age == other.age and \
                    self.frequency == other.frequency:
                if other.variant == '0' and self.variant != '0':
                    return True
        return False

    def __repr__(self):
        return "VerbInfl(conj='" + self.conj + "', variant='" + self.variant + "', tense='" + self.tense + \
               "', voice='" + self.voice + "', mood='" + self.mood + "', person='" + self.person + \
               "', number='" + self.number + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + \
               self.age + "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,VerbInfl):
            return False
        return self.conj == other.conj and \
               self.variant == other.variant and \
               self.tense == other.tense and \
               self.mood == other.voice and \
               self.voice == other.mood and \
               self.person == other.person and \
               self.number == other.number and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class VerbParticipleInfl:
    """
    Structural version of verb participle inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', conj='', variant='', case='', number='', gender='', tense='', voice='', stem='',
                 ending=None, age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.conj = buildstr[5]
            self.variant = buildstr[7]
            self.case = buildstr[9:13].strip()
            self.number = buildstr[13]
            self.gender = buildstr[15]
            self.tense = buildstr[17:22].strip()
            self.voice = buildstr[22:30].strip()
            self.stem = buildstr[34]
            self.ending_uvij = buildstr[38:51].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[51]
            self.frequency = buildstr[53]
        else:
            self.conj = conj
            self.variant = variant
            if case == '' or case in cases.keys():
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender in genders.keys():
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if tense == '' or tense in tenses:
                self.tense = tense
            else:
                raise ValueError("Unexpected inflection tense '{0}' during initialization.".format(tense))
            if voice == '' or voice in voices:
                self.voice = voice
            else:
                raise ValueError("Unexpected inflection voice '{0}' during initialization.".format(voice))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.conj:
            if infl.conj != self.conj:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.tense:
            if infl.tense != self.tense:
                return False
        if self.voice:
            if infl.voice != self.voice:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += verb_conjugations[self.conj] + ' ' + cases[self.case] + ' ' + numbers[self.number] + ' '
        inflstr += genders[self.gender] + ' ' + voices[self.voice] + ' ' + tenses[self.tense] + ' tense '
        inflstr += 'verb participle'
        return inflstr.replace('  ', ' ')

    def overrides(self,other):
        """
        Return True if this inflection has higher priority than `other` inflection

        For VerbParticipleInflection, priority goes to inflection with variant other than 0
        Inflections are comparable if case, tense, plurality, gender, and voice match

        NOTE: Returning False does not mean other inflection has priority
        NOTE: age and frequency are checked
        """
        if not isinstance(other,VerbParticipleInfl):
            return False
        # If these inflections are comparable, check if we have priority
        if self.conj == other.conj or (self.conj != '0' and other.conj == '0'):
            if self.tense == other.tense and \
                    self.case == other.case and \
                    self.gender == other.gender and \
                    self.number == other.number and \
                    self.voice == other.voice and \
                    self.age == other.age and \
                    self.frequency == other.frequency:
                if other.variant == '0' and self.variant != '0':
                    return True
        return False

    def __repr__(self):
        return "VerbParticipleInfl(conj='" + self.conj + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', tense='" + self.tense + \
               "', voice='" + self.voice + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + self.age + \
               "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,VerbParticipleInfl):
            return False
        return self.conj == other.conj and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.voice == other.voice and \
               self.tense == other.tense and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class SupineInfl:
    """
    Structural version of supine inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from original INFLECTS.LAT)
    If buildstr is given, all other args are ignored

    NOTE: buildstr is mostly legacy, INFLECTS.LAT is not even included in the distribution anymore, but the code
    can be useful e.g. for tests
    """

    def __init__(self, buildstr='', decl='', variant='', case='', number='', gender='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            raise DeprecationWarning("""buildstr is no longer supported because the data file is no longer part of the distribution. 
            Previous versions of PyWORDS used INFLECTS.LAT with spacing made more consistent, so the original WORDS version also
            won't work here. It's no longer recommended to use strings to initialize. 
            """)
        else:
            self.decl = decl
            self.variant = variant
            if case in ['','ACC','ABL']:
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number == 'S':
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender == 'N':
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if stem == '' or stem == '4':
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + genders[self.gender] + ' '
            inflstr += 'supine'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return "SupineInfl(decl='" + self.decl + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + self.age + \
               "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,PronounInfl):
            return False
        return self.decl == other.decl and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class PronounInfl:
    """
    Structural version of pronoun inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', decl='', variant='', case='', number='', gender='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.variant = buildstr[8]
            self.case = buildstr[10:14].strip()
            self.number = buildstr[14]
            self.gender = buildstr[16]
            self.stem = buildstr[20]
            self.ending_uvij = buildstr[24:52].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[52]
            self.frequency = buildstr[54]
        else:
            self.decl = decl
            self.variant = variant
            if case == '' or case in cases.keys():
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender in genders.keys():
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' '
            inflstr += 'pronoun'
        return inflstr.replace('  ', ' ')

    def overrides(self,other):
        """
        Return True if this inflection has higher priority than `other` inflection

        For PronounInflection, priority goes to inflection with variant other than 0
        Inflections are comparable if TODO

        NOTE: Returning False does not mean other inflection has priority
        NOTE: age and frequency are checked
        """
        if not isinstance(other,PronounInfl):
            return False
        # If these inflections are comparable, check if we have priority
        if self.decl == other.decl:
            if self.case == other.case and \
                    self.gender == other.gender and \
                    self.number == other.number and \
                    self.age == other.age and \
                    self.frequency == other.frequency:
                if other.variant == '0' and self.variant != '0':
                    return True
        return False

    def __repr__(self):
        return "PronounInfl(decl='" + self.decl + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + self.age + \
               "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,PronounInfl):
            return False
        return self.decl == other.decl and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class NumberInfl:
    """
    Structural version of number inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', decl='', variant='', case='', number='', gender='', kind='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[7]
            self.variant = buildstr[9]
            self.case = buildstr[11:15].strip()
            self.number = buildstr[15]
            self.gender = buildstr[17]
            self.kind = buildstr[20:29].strip()
            self.stem = buildstr[29]
            self.ending_uvij = buildstr[33:52].strip()
            self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            self.age = buildstr[52]
            self.frequency = buildstr[54]
        else:
            self.decl = decl
            self.variant = variant
            if case == '' or case in cases.keys():
                self.case = case
            else:
                raise ValueError("Unexpected inflection case {0} during initialization.".format(case))
            if number == '' or number in numbers.keys():
                self.number = number
            else:
                raise ValueError("Unexpected inflection number {0} during initialization.".format(number))
            if gender == '' or gender in genders.keys():
                self.gender = gender
            else:
                raise ValueError("Unexpected inflection gender {0} during initialization.".format(gender))
            if kind == '' or kind in number_kinds:
                self.kind = kind
            else:
                raise ValueError("Unexpected inflection number kind {0} during initialization.".format(kind))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.variant:
            if infl.variant != self.variant:
                return False
        if self.case:
            if infl.case != self.case:
                return False
        if self.number:
            if infl.number != self.number:
                return False
        if self.gender:
            if infl.gender != self.gender:
                return False
        if self.kind:
            if infl.kind != self.kind:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if self.ending_vi is not None:
            if infl.ending_vi != self.ending_vi:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' '
            if self.kind:
                inflstr += number_kinds[self.kind] + ' '
            inflstr += 'numeral'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return "NumberInfl(decl='" + self.decl + "', variant='" + self.variant + "', case='" + self.case + \
               "', number='" + self.number + "', gender='" + self.gender + "', kind='" + self.kind + "', stem='" + self.stem + \
               "', ending_uvij='" + self.ending_uvij + "', ending_vi='" + self.ending_vi + "', age='" + self.age + \
               "', frequency='" + self.frequency + "')"

    def __eq__(self,other):
        if not isinstance(other,NumberInfl):
            return False
        return self.decl == other.decl and \
               self.variant == other.variant and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.kind == other.kind and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class AdverbInfl:
    """
    Structural version of adverb inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', comparison='', stem='', age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.comparison = buildstr[5]
            self.stem = buildstr[11]
            self.age = buildstr[19]
            self.frequency = buildstr[21]
        else:
            if comparison == '' or comparison in comparisons.keys():
                self.comparison = comparison
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.comparison:
            if infl.comparison != self.comparison:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        if self.comparison:
            inflstr += comparisons[self.comparison]
        inflstr += ' adverb'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return "AdverbInfl(comparison='{0}', stem='{1}', self.age='{2}', self.frequency='{3}')".format(
            self.comparison, self.stem, self.age, self.frequency)

    def __eq__(self,other):
        if not isinstance(other,AdverbInfl):
            return False
        return self.comparison == other.comparison and \
               self.stem == other.stem and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


class PrepositionInfl:
    """
    Structural version of preposition inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    """

    def __init__(self, buildstr='', aux_case='', stem='', age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.aux_case = buildstr[5]
            self.stem = buildstr[11]
            self.age = buildstr[19]
            self.frequency = buildstr[21]
        else:
            if aux_case in ['','GEN','ACC','ABL']:
                self.aux_case = aux_case
            else:
                raise ValueError("Unexpected inflection auxiliary case {0} during initialization.".format(aux_case))
            if stem == '' or stem in ['1','2','3','4']:
                self.stem = stem
            else:
                raise ValueError("Unexpected inflection stem id {0} during initialization.".format(stem))
            if age == '' or age in ages.keys():
                self.age = age
            else:
                raise ValueError("Unexpected inflection age {0} during initialization.".format(age))
            if frequency == '' or frequency in inflection_frequencies.keys():
                self.frequency = frequency
            else:
                raise ValueError("Unexpected inflection frequency {0} during initialization.".format(frequency))

    def matches(self, infl, match_age=False, match_frequency=False):
        """
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        """
        if self.aux_case:
            if infl.aux_case != self.aux_case:
                return False
        if self.stem:
            if infl.stem != self.stem:
                return False
        if match_age:
            if self.age:
                if infl.age != self.age:
                    return False
        if match_frequency:
            if self.frequency:
                if infl.frequency != self.frequency:
                    return False
        return True

    def get_inflection_string(self, less=False):
        """Convert the inflection information into a plaintext, user-friendly form."""
        inflstr = ''
        inflstr += 'preposition'
        if cases[self.aux_case]:
            inflstr += ' with ' + cases[self.aux_case]
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return "PrepositionInfl(aux_case={0}, stem='{1}', age='{2}', frequency='{3}')".format(
            self.aux_case, self.stem, self.age, self.frequency)

    def __eq__(self,other):
        if not isinstance(other,PrepositionInfl):
            return False
        return self.aux_case == other.aux_case and \
               self.stem == other.stem and \
               self.age == other.age and \
               self.frequency == other.frequency

    def __hash__(self):
        return hash(repr(self))


@dataclass
class Tackon:
    """
    Tackon and Packon objects, representing possible tackons
    See notes.txt for details. Tackons can be applied to pronouns, nouns, or adjectives,
    of specific declension, variant, kind, and even case.

    @params
        suffix          Actual tackon that gets added (e.g. -libet)
        senses          Senses of tackon in general
        word_pos        Part of speech of valid targets
        word_decl       Declension of valid targets
        word_variant    Variant of valid targets
        word_gender     (for nouns)
        word_plurality  (for nouns)
        word_case       (optional) case of inflection that this tackon applies to (e.g. ABL with -cum)
        word_kind       Kind for valid targets
    """
    suffix: str
    senses: str
    word_pos: str = ''
    word_decl: str = ''
    word_variant: str = ''
    word_gender: str = ''
    word_plurality: str = ''
    word_case: str = ''
    word_kind: str = ''

    def matches_dictline_entry(self,entry : DictlineBaseEntry):
        """
        Check if this tackon can apply to `entry`

        Note: Pronoun entry part of speech can be either PRON or PACK, so
        no special handling is required to distinguish
        """
        if isinstance(entry, (DictlineAdjectiveEntry,DictlinePronounEntry,DictlineNounEntry) ):
            if entry.pos != self.word_pos:
                return False
            if entry.decl != self.word_decl:
                return False
            if self.word_variant != '0' and entry.variant != self.word_variant:
                return False
            if isinstance(entry,DictlinePronounEntry):
                if entry.pronoun_kind != self.word_kind:
                    return False
            elif isinstance(entry,DictlineAdjectiveEntry):
                if entry.comparison != self.word_kind:
                    return False
            elif isinstance(entry,DictlineNounEntry):
                if entry.gender != self.word_gender:
                    return False
            return True
        else:
            return False

    def matches_inflection(self,infl):
        """
        Check if the plurality and case are valid for this tackon
        """
        if isinstance(infl, (NounInfl,AdjectiveInfl,PronounInfl)):
            if self.word_case != '':
                if infl.case != self.word_case:
                    return False
            if self.word_plurality != '':
                if infl.number != self.word_plurality:
                    return False
            return True
        else:
            return False


def build_inflection(buildstr='', part_of_speech='', stem='', ending=None, age='', frequency='', decl='', conj='', variant='',
                     case='', number='', gender='', person='', comparison='', tense='', voice='', mood='', kind=''):
    """
    Automatically build and return an Infl object of correct type
    If buildstr is provided, only it is used
    If not, part_of_speech MUST be given
    """
    if buildstr:
        pos = buildstr[0:5].strip()
        infl_out = None
        if pos == 'N':
            infl_out = NounInfl(buildstr=buildstr)
        elif pos == 'ADJ':
            infl_out = AdjectiveInfl(buildstr=buildstr)
        elif pos == 'V':
            infl_out = VerbInfl(buildstr=buildstr)
        elif pos == 'VPAR':
            infl_out = VerbParticipleInfl(buildstr=buildstr)
        elif pos == 'PRON':
            infl_out = PronounInfl(buildstr=buildstr)
        elif pos == 'NUM':
            infl_out = NumberInfl(buildstr=buildstr)
        elif pos == 'SUPINE':
            infl_out = SupineInfl(buildstr=buildstr)
        elif pos == 'ADV':
            infl_out = AdverbInfl(buildstr=buildstr)
        elif pos in ['PREP', 'CONJ', 'INTERJ']:
            infl_out = None
        return infl_out
    else:
        # Note: it's fine if entries are empty
        pos = part_of_speech
        if pos == 'N':
            infl_out = NounInfl(decl=decl, variant=variant, case=case, number=number, gender=gender,
                                stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'ADJ':
            infl_out = AdjectiveInfl(decl=decl, variant=variant, case=case, number=number, gender=gender,
                                     comparison=comparison, stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'V':
            infl_out = VerbInfl(conj=conj, variant=variant, tense=tense, voice=voice, mood=mood, number=number,
                                stem=stem, person=person, ending=ending, age=age, frequency=frequency)
        elif pos == 'VPAR':
            infl_out = VerbParticipleInfl(conj=conj, variant=variant, case=case, number=number, gender=gender,
                                          stem=stem, tense=tense, voice=voice, ending=ending, age=age,
                                          frequency=frequency)
        elif pos == 'SUPINE':
            infl_out = SupineInfl(decl=decl, variant=variant, case=case, number=number, gender=gender,
                                  stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'PRON':
            infl_out = PronounInfl(decl=decl, variant=variant, case=case, number=number, gender=gender,
                                   stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'NUM':
            infl_out = NumberInfl(decl=decl, variant=variant, case=case, number=number, gender=gender, kind=kind,
                                  stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'SUPINE':  # Note: because of indexing the 'E' at the end is cut off
            infl_out = None
        elif pos == 'ADV':
            infl_out = AdverbInfl(comparison=comparison, stem=stem, age=age, frequency=frequency)
        elif pos in ['PREP', 'CONJ', 'INTERJ', 'PACK', 'TACKON', 'SUFFIX', 'PREFIX']:
            infl_out = None
        else:
            print("WARNING: Unknown inflection part of speech: {0}\nReturning None".format(pos))
            infl_out = None
        return infl_out


def load_inflections():
    # orig_inflections = f.readlines()
    # f.close()
    global inflections

    # First get column names and index them in case the order changes
    # Get inflects table
    infl_fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/INFLECTS.tsv')
    if not os.path.exists(infl_fname):
        print("FATAL ERROR: Could not find INFLECTS.tsv. This is the file that contains all possible inflections of words. It should have been included in your installation under data/.")
        raise FileNotFoundError
    with open(infl_fname) as f:
        reader = csv.DictReader(f,delimiter='\t')
        inflect_rows = [row for row in reader]

    # Build inflections
    for row in inflect_rows:
        pos = row['infl_pos']
        infl_out = build_inflection(
            part_of_speech=row['infl_pos'] or '',
            stem=row['infl_stem_id'] or '',
            ending=row['infl_ending'] or '',
            age=row['infl_age'] or '',
            frequency=row['infl_frequency'] or '',
            decl=row['infl_type'] or '',
            conj=row['infl_type'] or '',
            variant=row['infl_variant'] or '',
            case=row['infl_case'] or '',
            number=row['infl_plurality'] or '',
            gender=row['infl_gender'] or '',
            person=row['infl_person'] or '',
            comparison=row['infl_comparison'] or '',
            tense=row['infl_tense'] or '',
            voice=row['infl_voice'] or '',
            mood=row['infl_mood'] or '',
            kind=row['infl_numtype'] or '')
        if infl_out:
            inflections[pos].append(infl_out)  # Add to appropriate inflection list


def _cache_noun_inflections(key : str):
    """
    Generate a cached inflection for N <key>
    `key` must be a string in the format "<decl> <var>", e.g. "1 1"
    Neither decl nor var can be 0
    """
    global inflections
    global _noun_inflections_cached

    if len(key) != 3:
        raise ValueError("Trying to build noun inflection but key provided '{0}' is not in the format '<decl> <var>'. Length is not 3.".format(key))
    if key[1] != ' ':
        raise ValueError("Trying to build noun inflection but key provided '{0}' is not in the format '<decl> <var>'. Space must be in key.".format(key))
    try:
        decl_int = int(key[0])
        var_int = int(key[2])
    except ValueError:
        raise ValueError("Trying to build noun inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension or variant is not recognzied as a number.".format(key))
    if key[0] == '0' or key[2] == '0':
        raise ValueError("Trying to build noun inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension and variant cannot be '0'.".format(key))

    # Don't recache
    if key in _noun_inflections_cached.keys():
        return

    # Get inflections, noting priority and keeping age and frequency
    # first priority
    test_infl = build_inflection(part_of_speech='N', decl=key[0], variant=key[2])
    Ninfls1 = [n for n in inflections['N'] if test_infl.matches(n)]
    # second priority
    test_infl = build_inflection(part_of_speech='N', decl=key[0], variant='0')
    Ninfls2 = [n for n in inflections['N'] if test_infl.matches(n)]

    infls_out = Ninfls1  # Start with top priority, which must be included
    # Now check for gaps
    for lopri_infl in Ninfls2:
        overridden=False
        for hipri_infl in Ninfls1:
            if hipri_infl.overrides(lopri_infl):
                overridden=True
                break
        if not overridden:
            infls_out.append(lopri_infl)

    _noun_inflections_cached[key] = infls_out


def _cache_adj_inflections(key : str):
    """
    Generate a cached inflection for ADJ <key>
    `key` must be a string in the format "<decl> <var>", e.g. "1 1"
    If decl is not '0', variant cannot be '0', but '0 0' is valid
    """
    global inflections
    global _adj_inflections_cached

    if len(key) != 3:
        raise ValueError("Trying to build adjective inflection but key provided '{0}' is not in the format '<decl> <var>'. Length is not 3.".format(key))
    if key[1] != ' ':
        raise ValueError("Trying to build adjective inflection but key provided '{0}' is not in the format '<decl> <var>'. Space must be in key.".format(key))
    try:
        decl_int = int(key[0])
        var_int = int(key[2])
    except ValueError:
        raise ValueError("Trying to build adjective inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension or variant is not recognzied as a number.".format(key))
    if key[0] == '0' or key[2] == '0':
        if key[0] != '0' or key[2] != '0':
            raise ValueError("Trying to build adjective inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension and variant cannot be '0' unless both are '0'.".format(key))

    # Don't recache
    if key in _adj_inflections_cached.keys():
        return

    # Get inflections, noting priority and keeping age and frequency
    # first priority
    test_infl = build_inflection(part_of_speech='ADJ', decl=key[0], variant=key[2])
    ADJinfls1 = [n for n in inflections['ADJ'] if test_infl.matches(n)]
    # second priority
    test_infl = build_inflection(part_of_speech='ADJ', decl=key[0], variant='0')
    ADJinfls2 = [n for n in inflections['ADJ'] if test_infl.matches(n)]
    # third priority
    test_infl = build_inflection(part_of_speech='ADJ', decl='0', variant='0')
    ADJinfls3 = [n for n in inflections['ADJ'] if test_infl.matches(n)]

    infls_out = ADJinfls1  # Start with top priority, which must be included
    # Now check for gaps
    for midpri_infl in ADJinfls2:
        overridden = False
        for hipri_infl in ADJinfls1:
            if hipri_infl.overrides(midpri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(midpri_infl)

    infls_out_partial = infls_out  # Capture state before we start adding again
    for lopri_infl in ADJinfls3:
        overridden = False
        for hipri_infl in infls_out_partial:
            if hipri_infl.overrides(lopri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(lopri_infl)

    _adj_inflections_cached[key] = infls_out


def _cache_verb_inflections(key : str):
    """
    Generate a cached inflection for V <key>
    `key` must be a string in the format "<conj> <var>", e.g. "1 1"
    Neither decl nor var can be 0

    This also adds VPAR and SUPINE inflections
    """
    global inflections
    global _verb_inflections_cached

    if len(key) != 3:
        raise ValueError("Trying to build verb inflection but key provided '{0}' is not in the format '<conj> <var>'. Length is not 3.".format(key))
    if key[1] != ' ':
        raise ValueError("Trying to build verb inflection but key provided '{0}' is not in the format '<conj> <var>'. Space must be in key.".format(key))
    try:
        conj_int = int(key[0])
        var_int = int(key[2])
    except ValueError:
        raise ValueError("Trying to build verb inflection but key provided '{0}' is not in the format '<conj> <var>'. Conjugation or variant is not recognzied as a number.".format(key))
    if key[0] == '0' or key[2] == '0':
        raise ValueError("Trying to build verb inflection but key provided '{0}' is not in the format '<conj> <var>'. Conjugation and variant cannot be '0'.".format(key))

    # Don't recache
    if key in _verb_inflections_cached.keys():
        return

    # BASE INFLECTIONS (V x y)
    # Get inflections, noting priority and keeping age and frequency
    # first priority (V x y)
    test_infl = build_inflection(part_of_speech='V', conj=key[0], variant=key[2])
    Vinfls1 = [n for n in inflections['V'] if test_infl.matches(n)]
    # second priority (V x 0)
    test_infl = build_inflection(part_of_speech='V', conj=key[0], variant='0')
    Vinfls2 = [n for n in inflections['V'] if test_infl.matches(n)]
    # third priority (V 0 0)
    test_infl = build_inflection(part_of_speech='V', conj='0', variant='0')
    Vinfls3 = [n for n in inflections['V'] if test_infl.matches(n)]

    infls_out = Vinfls1  # Start with top priority, which must be included
    # Now check for gaps
    for midpri_infl in Vinfls2:
        overridden = False
        for hipri_infl in Vinfls1:
            if hipri_infl.overrides(midpri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(midpri_infl)

    infls_out_partial = infls_out  # Partial list before we start adding again
    for lopri_infl in Vinfls3:
        overridden = False
        for hipri_infl in infls_out_partial:
            if hipri_infl.overrides(lopri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(lopri_infl)

    # VPAR INFLECTIONS (VPAR x y)
    test_infl = build_inflection(part_of_speech='VPAR', conj=key[0], variant=key[2])
    Vinfls1 = [n for n in inflections['VPAR'] if test_infl.matches(n)]
    # second priority (V x 0)
    test_infl = build_inflection(part_of_speech='V', conj=key[0], variant='0')
    Vinfls2 = [n for n in inflections['VPAR'] if test_infl.matches(n)]
    # third priority (V 0 0)
    test_infl = build_inflection(part_of_speech='V', conj='0', variant='0')
    Vinfls3 = [n for n in inflections['VPAR'] if test_infl.matches(n)]

    vpar_infls_out = Vinfls1  # Start with top priority, which must be included
    # Now check for gaps
    for midpri_infl in Vinfls2:
        overridden = False
        for hipri_infl in Vinfls1:
            if hipri_infl.overrides(midpri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(midpri_infl)

    vpar_infls_out_partial = vpar_infls_out  # Partial list before we start adding again
    for lopri_infl in Vinfls3:
        overridden = False
        for hipri_infl in vpar_infls_out_partial:
            if hipri_infl.overrides(lopri_infl):
                overridden = True
                break
        if not overridden:
            vpar_infls_out.append(lopri_infl)
    infls_out += vpar_infls_out  # Concatenate

    # SUPINE INFLECTIONS (SUPINE 0 0)
    infls_out += inflections['SUPINE']

    # Set cached verb inflection list
    _verb_inflections_cached[key] = infls_out


def _cache_num_inflections(key : str):
    """
    Generate a cached inflection for NUM <key>
    `key` must be a string in the format "<decl> <var>", e.g. "1 1"
    Neither decl nor var can be 0
    """
    global inflections
    global _num_inflections_cached

    if len(key) != 3:
        raise ValueError("Trying to build numeral inflection but key provided '{0}' is not in the format '<decl> <var>'. Length is not 3.".format(key))
    if key[1] != ' ':
        raise ValueError("Trying to build numeral inflection but key provided '{0}' is not in the format '<decl> <var>'. Space must be in key.".format(key))
    try:
        decl_int = int(key[0])
        var_int = int(key[2])
    except ValueError:
        raise ValueError("Trying to build numeral inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension or variant is not recognzied as a number.".format(key))
    if key[0] == '0' or key[2] == '0':
        raise ValueError("Trying to build numeral inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension and variant cannot be '0'.".format(key))

    # Don't recache
    if key in _num_inflections_cached.keys():
        return

    # first priority
    test_infl = build_inflection(part_of_speech='NUM', decl=key[0], variant=key[2])
    NUMinfls1 = [n for n in inflections['NUM'] if test_infl.matches(n)]
    # second priority
    test_infl = build_inflection(part_of_speech='NUM', decl=key[0], variant='0')
    NUMinfls2 = [n for n in inflections['NUM'] if test_infl.matches(n)]
    # third priority
    test_infl = build_inflection(part_of_speech='NUM', decl='0', variant='0')
    NUMinfls3 = [n for n in inflections['NUM'] if test_infl.matches(n)]

    infls_out = NUMinfls1  # Start with top priority, which must be included
    # Now check for gaps
    for midpri_infl in NUMinfls2:
        overridden = False
        for hipri_infl in NUMinfls1:
            if hipri_infl.overrides(midpri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(midpri_infl)

    infls_out_partial = infls_out  # Capture state before we start adding again
    for lopri_infl in NUMinfls3:
        overridden = False
        for hipri_infl in infls_out_partial:
            if hipri_infl.overrides(lopri_infl):
                overridden = True
                break
        if not overridden:
            infls_out.append(lopri_infl)

    _num_inflections_cached[key] = infls_out


def _cache_pronoun_inflections(key : str):
    """
    Generate a cached inflection for NUM <key>
    `key` must be a string in the format "<decl> <var>", e.g. "1 1"
    Neither decl cannot be 0, var can
    """
    global inflections
    global _pron_inflections_cached

    if len(key) != 3:
        raise ValueError("Trying to build pronoun inflection but key provided '{0}' is not in the format '<decl> <var>'. Length is not 3.".format(key))
    if key[1] != ' ':
        raise ValueError("Trying to build pronoun inflection but key provided '{0}' is not in the format '<decl> <var>'. Space must be in key.".format(key))
    try:
        decl_int = int(key[0])
        var_int = int(key[2])
    except ValueError:
        raise ValueError("Trying to build pronoun inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension or variant is not recognzied as a number.".format(key))
    if key[0] == '0':
        raise ValueError("Trying to build pronoun inflection but key provided '{0}' is not in the format '<decl> <var>'. Declension cannot be '0'.".format(key))

    # Don't recache
    if key in _pron_inflections_cached.keys():
        return

    # Get inflections, noting priority and keeping age and frequency
    # first priority
    test_infl = build_inflection(part_of_speech='PRON', decl=key[0], variant=key[2])
    Pinfls1 = [n for n in inflections['PRON'] if test_infl.matches(n)]
    # second priority
    test_infl = build_inflection(part_of_speech='PRON', decl=key[0], variant='0')
    Pinfls2 = [n for n in inflections['PRON'] if test_infl.matches(n)]

    infls_out = Pinfls1  # Start with top priority, which must be included
    # Now check for gaps
    for lopri_infl in Pinfls2:
        overridden=False
        for hipri_infl in Pinfls1:
            if hipri_infl.overrides(lopri_infl):
                overridden=True
                break
        if not overridden:
            infls_out.append(lopri_infl)

    _pron_inflections_cached[key] = infls_out


def _get_possible_noun_inflections(dl_entry):
    # Nouns have gender, which might require including common (C) or specific
    # (M/F) genders in addition
    # If noun kind is S (singular only) or M (multiple/plural only), assign number
    global inflections
    global _noun_inflections_cached

    infls_matched = set()  # Temporary variable before age/frequency
    key = '{0} {1}'.format(dl_entry.decl, dl_entry.variant)
    _cache_noun_inflections(key)  # Make sure we cache this inflection key
    infls_all = _noun_inflections_cached[key]

    for infl in infls_all:
        matched = True
        # Check gender
        if dl_entry.gender in ['M', 'F', 'C']:
            # Check for M, F, and C genders
            if infl.gender == 'N':
                matched = False
                continue
        elif dl_entry.gender == 'N':
            if infl.gender not in ['N','X']:
                matched = False
                continue
        # Check noun kind
        if dl_entry.noun_kind == 'S':
            if infl.number == 'P':
                matched = False
                continue
        elif dl_entry.noun_kind == 'M':
            if infl.number == 'S':
                matched = False
                continue

        if matched:
            infls_matched.add(infl)
    return infls_matched


def _get_possible_adj_inflections(dl_entry):
    # Adjectives are narrowed by comparison SOMETIMES
    # If comparison is 'X', all are valid
    # If comparison is 'POS', 'COMP', or 'SUPER', only that comparison is a match
    global inflections
    global _adj_inflections_cached

    infls_matched = set()  # Temporary variable before age/frequency
    key = '{0} {1}'.format(dl_entry.decl,dl_entry.variant)
    _cache_adj_inflections(key)
    infls_all = _adj_inflections_cached[key]

    for infl in infls_all:
        matched = True
        # Check comparison
        if dl_entry.comparison in ['POS','COMP','SUPER']:
            if infl.comparison != dl_entry.comparison:
                matched = False
        if matched:
            infls_matched.add(infl)
    return infls_matched


def _get_possible_verb_inflections(dl_entry):
    # Verbs have kinds (DEP, SEMIDEP, PERFDEF, IMPERS, TO_BE, TO_BEING) that we need to check
    global inflections
    global _verb_inflections_cached

    infls_matched = set()  # Temporary variable before age/frequency
    key = '{0} {1}'.format(dl_entry.conj, dl_entry.variant)
    _cache_verb_inflections(key)  # Make sure this inflection key is cached
    infls_all = _verb_inflections_cached[key]

    for infl in infls_all:
        matched = True
        # Check verb types
        if dl_entry.verb_kind == 'DEP':
            # Deponent, passive voice only (active meaning), still has present and fut active ppls, fut act. infinitive
            # No perfect stem, occasionally has no supine
            # Examples:
            #   tueor, tueri, tuitis sum
            if isinstance(infl,VerbInfl):
                if infl.voice == 'ACTIVE':
                    matched = False
            elif isinstance(infl,VerbParticipleInfl):
                if infl.voice == 'PASSIVE':
                    # TODO gerundive exists in transitive verbs, and intransitive impersonal verbs
                    # Whitaker has only one verb kind column, so there's not enough information to exclude gerundive
                    # He notes that the verb kinds are not mutually exclusive; would probably be worth it to refactor
                    if infl.tense == 'PRES' or infl.tense == 'PERF':
                        matched = False

        elif dl_entry.verb_kind == 'SEMIDEP':
            # Passive voice for perfect system, otherwise normal
            # Usually, but not always, has no perfect stem in dictline entry
            # Examples:
            #   defio, defieri
            #   audeo, audere (optionally semidep., has perfect stem)
            if isinstance(infl,VerbInfl):
                if infl.voice == 'ACTIVE':
                    if infl.stem == '3':
                        matched = False
            elif isinstance(infl,VerbParticipleInfl):
                if infl.stem == '3':
                    matched = False
                if infl.voice == 'PASSIVE':
                    matched = False
        elif dl_entry.verb_kind == 'PERFDEF':
            # Perfect stem only, or sometimes supine stem
            # Examples:
            #   commemini, commeminisse, - (no supine)
            #   novi, novisse, notus sum
            if infl.stem not in ['3','4']:
                matched = False
        elif dl_entry.verb_kind == 'IMPERS':
            # 3rd person singular only, or infinitive or gerund (inflect stem = 0)
            # Examples:
            if isinstance(infl,VerbInfl):
                if infl.person not in ['3','0']:
                    matched = False
                elif infl.number not in ['S','X']:
                    matched = False
            elif isinstance(infl,VerbParticipleInfl):
                # Only gerund i.e. singular future passive participle in oblique cases
                if infl.case not in ['ABL','ACC','DAT','GEN']:
                    matched = False
                if infl.tense != 'FUT':
                    matched = False
                if infl.number == 'P':
                    matched = False
                if infl.voice == 'ACTIVE':
                    matched = False

        elif dl_entry.verb_kind == 'TO_BE':
            # esse, not used because it's handled as a unique
            pass
        elif dl_entry.verb_kind == 'TO_BEING':
            # like esse, need to revisit this and figure out how to use it... TODO
            pass
        if matched:
            infls_matched.add(infl)
    return infls_matched


def _get_possible_num_inflections(dl_entry):
    # This method is basically a pass-through for now, but if it changes, things can be added
    global inflections
    global _num_inflections_cached
    infls_matched = set()  # Temporary variable before age/frequency
    key = '{0} {1}'.format(dl_entry.decl, dl_entry.variant)
    _cache_num_inflections(key)  # Make sure this inflection key is cached
    infls_all = _num_inflections_cached[key]

    for infl in infls_all:
        matched = True
        if matched:
            infls_matched.add(infl)
    return infls_matched


def _get_possible_pron_inflections(dl_entry):
    # This is basically a pass-through unless any special cases crop up
    global inflections
    global _num_inflections_cached
    infls_matched = set()  # Temporary variable before age/frequency
    key = '{0} {1}'.format(dl_entry.decl, dl_entry.variant)
    _cache_pronoun_inflections(key)  # Make sure this inflection key is cached
    infls_all = _pron_inflections_cached[key]

    for infl in infls_all:
        matched = True
        if matched:
            infls_matched.add(infl)
    return infls_matched


def get_possible_inflections(dl_entry,infl_age='',infl_frequency=''):
    """
    Given a dictline entry, return a list of all possible inflections

    Some notable special cases:
    -Nouns-
        N kind=S    Singular only
        N kind=M    Plural/multiple only
    -Verbs-
        V 0 0 is shared for all decl/var combinations, except when overridden
        V x 0 is shared for all variants of declension `x`, except when overridden
        V 3 1       Unique handling depending on whether stem ends in -c
        V 7 x       Defective verbs
        V 8 0       Irregular verbs, overrides FUTP IND and PERF/PLUP SUB
        V DEP       Passive voice only, and PRES/FUT ACTIVE VPAR, FUT ACTIVE INF
        V SEMIDEP   Passive voice for stem 3 (perfect stem), otherwise active or passive
        V IMPERS    3rd person singular, infinitive, and gerund
        V PERFDEF   Perfect stem only
        V mood=PPL  Not used
        V TO_BE     Not used
        V TO_BEING  Verbs like esse
    """
    global inflections

    pos = dl_entry.pos
    infls = set()
    infls_matched = set()  # Temporary variable before age/frequency
    if pos in ['PREP','INTERJ','CONJ','ADV']:
        infls_matched = inflections[pos]
    elif pos == 'ADJ':
        infls_matched = _get_possible_adj_inflections(dl_entry)
    elif pos == 'NUM':
        infls_matched = _get_possible_num_inflections(dl_entry)
    elif pos == 'PRON':
        infls_matched = _get_possible_pron_inflections(dl_entry)
    elif pos == 'N':
        infls_matched = _get_possible_noun_inflections(dl_entry)
    elif pos == 'V':
        infls_matched = _get_possible_verb_inflections(dl_entry)

    # Remove based on age and frequency
    for infl in infls_matched:
        infl_ok = True
        if infl_age != '':
            if infl.age != infl_age:
                infl_ok = False
        if infl_frequency != '':
            if infl.frequency != infl_frequency:
                infl_ok = False

        if infl_ok:
            infls.add(infl)
    return infls


def reverse_ending_lookup(e):
    # Return a list of possible forms that use the ending given by `e`
    e = e.strip('-')  # remove any dashes
    infls = set()
    for pos in ['N', 'ADJ', 'V']:
        inflection = build_inflection(part_of_speech=pos, ending=e)
        matches = [inf for inf in inflections[pos] if inflection.matches(inf)]
        for m in matches:
            infls.add(m)
        if pos == 'V':
            vpar_matches = [inf for inf in inflections['VPAR'] if inflection.matches(inf)]
            for m in vpar_matches:
                infls.add(m)
            supine_matches = [inf for inf in inflections['SUPINE'] if inflection.matches(inf)]
            for m in supine_matches:
                infls.add(m)
    return infls
