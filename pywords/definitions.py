# Python definitions useful for interpreting and working with dictionary entries, inflections, etc.

import os
import os.path
import csv
from pywords.matchfilter import MatchFilter

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
inflections = {'N': [], 'ADJ': [], 'V': [], 'VPAR': [], 'PRON': [], 'NUM': [], 'ADV': [], 'PREP': []}

# TODO Are these used? Is u/v causing problems?
irreg_sum = ['svm', 'es', 'est', 'svmvs', 'estis', 'svnt', 'eram', 'eras', 'erat', 'eramvs', 'eratis', 'erant',
             'ero', 'eris', 'erit', 'erimvs', 'eritis', 'ervnt', 'fvi', 'fvisti', 'fvit', 'fvimvs', 'fvistis',
             'fvervnt', 'fveram', 'fveras', 'fverat', 'fveramvs', 'fveratis', 'fverant', 'fvero', 'fveris', 'fverit',
             'fverimvs', 'fveritis', 'fvervnt', 'sis', 'sit', 'simvs', 'sitis', 'sint', 'essem', 'esses', 'esset',
             'essemvs', 'essetis', 'essent', 'fverim', 'fveris', 'fverit', 'fverimvs', 'fveritis', 'fverint',
             'fvissem', 'fvisses', 'fvisset', 'fvissemvs', 'fvissetis', 'fvissent']


#####################################
####### DICTIONARY ENTRIES ##########

class DictlineBaseEntry:
    '''
    dictline entry
    Base class for dictline entries, providing dictionary codes
    '''

    def __init__(self, pos, age, area, geog, freq, src, senses):
        self.pos = pos
        self.age = age
        self.area = area
        self.geog = geog
        self.freq = freq
        self.src = src
        self.senses = senses

    def get_part_of_speech(self):
        return parts_of_speech[self.pos]

    def get_age(self):
        return ages[self.age]

    def get_area(self):
        return areas[self.area]

    def get_geography(self):
        return geographies[self.geog]

    def get_frequency(self):
        return dict_frequencies[self.frequency]

    def get_source(self):
        return source_types[self.src]

    def get_senses(self):
        return self.senses


class DictlineNounEntry(DictlineBaseEntry):
    '''
    dictline noun entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, decl, variant, gender, noun_kind, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # declension variant (see INFLECTS.LAT)
        self.gender = gender
        self.noun_kind = noun_kind

    def get_declension(self):
        return noun_declensions[self.decl]

    def get_gender(self):
        return genders[self.gender]

    def get_noun_kind(self):
        return noun_kinds[self.noun_kind]

    def __repr__(self):
        return 'DictlineNounEntry(decl=' + self.decl + ', variant=' + self.variant + \
               ', gender=' + self.gender + ', noun_kind=' + self.noun_kind + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlineVerbEntry(DictlineBaseEntry):
    '''
    dictline verb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, conj, variant, verb_kind, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.conj = conj  # conjugation
        self.variant = variant  # conjugation variant (see INFLECTS.LAT)
        self.verb_kind = verb_kind

    def get_conjugation(self):
        return verb_conjugations[self.conj]

    def get_verb_kind(self):
        return verb_kinds[self.verb_kind]

    def __repr__(self):
        return 'DictlineVerbEntry(conj=' + self.conj + ', variant=' + self.variant + \
               ', verb_kind=' + self.verb_kind + ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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
    '''
    dictline adjective entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, decl, variant, comparison, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # adjective variant (see INFLECTS.LAT)
        self.comparison = comparison

    def get_declension(self):
        return adj_declensions[self.decl]

    def get_comparison(self):
        return comparisons[self.comparison]

    def __repr__(self):
        return 'DictlineAdjectiveEntry(decl=' + self.decl + ', variant=' + self.variant + \
               ', comparison=' + self.comparison + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlineAdverbEntry(DictlineBaseEntry):
    '''
    dictline adverb entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, comparison, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.comparison = comparison

    def get_comparison(self):
        return comparisons[self.comparison]

    def __repr__(self):
        return 'DictlineAdverbEntry(comparison=' + self.comparison + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlinePronounEntry(DictlineBaseEntry):
    '''
    dictline pronoun (and pack) entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, decl, variant, pronoun_kind, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension TODO
        self.variant = variant
        self.pronoun_kind = pronoun_kind

    def __repr__(self):
        return 'DictlinePronounEntry(decl=' + self.decl + ', variant=' + self.variant + \
               ', pronoun_kind=' + self.pronoun_kind + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlineConjunctionEntry(DictlineBaseEntry):
    '''
    dictline conjunction entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)

    def __repr__(self):
        return 'DictlineConjunctionEntry(pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlineInterjectionEntry(DictlineBaseEntry):
    '''
    dictline interjection entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)

    def __repr__(self):
        return 'DictlineInterjectionEntry(pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlinePrepositionEntry(DictlineBaseEntry):
    '''
    dictline preposition entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, case, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.case = case

    def get_case(self):
        return cases[self.case]

    def __repr__(self):
        return 'DictlinePrepositionEntry(case=' + self.case + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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


class DictlineNumberEntry(DictlineBaseEntry):
    '''
    dictline number entry
    Stores the dictline elements column-by-column as they appear, and can provide human-readable and
    machine-readable information.
    '''

    def __init__(self, pos, decl, variant, number_kind, number, age, area, geog, freq, src, senses):
        super().__init__(pos, age, area, geog, freq, src, senses)
        self.decl = decl  # declension
        self.variant = variant  # adjective variant (see INFLECTS.LAT)
        self.number_kind = number_kind
        self.number = number

    def get_declension(self):
        return adj_declensions[self.decl]

    def get_number_kind(self):
        return number_kinds[self.number_kind]

    def get_number(self):
        return self.number

    def __repr__(self):
        return 'DictlineNumberEntry(decl=' + self.decl + ', variant=' + self.variant + \
               ', number=' + self.number + ', number_kind=' + self.number_kind + \
               ', pos=' + self.pos + ', age=' + self.age + ', freq=' + self.freq + \
               ', area=' + self.area + ', geog=' + self.geog + ', src=' + self.src + \
               ', senses=' + self.senses + ')'

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
#


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


# NOTE: To match inflections, simply create a partially filled Infl object, and use a list
# comprehension to find matches, as in this example:
#   testnoun = NounInfl(decl='1',case='NOM',number='S')
#   noun_matches = [n for n in inflections['N'] if testnoun.matches(n)]
#
# Note the order of the matches() method: use the template inflection (testnoun)
# to check if the full inflections matches (inflections['N'])
class NounInfl:
    '''
    Structural version of noun inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', decl='', var='', case='', number='', gender='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.var = buildstr[8]
            self.case = buildstr[10:13].strip()
            self.number = buildstr[14]
            self.gender = buildstr[16]
            self.stem = buildstr[19]
            self.ending_uvij = buildstr[23:32].strip()
            self.ending_vi = buildstr[23:32].strip().replace('j', 'i').replace('u', 'v')
            self.age = buildstr[33]
            self.frequency = buildstr[35]
        else:
            self.decl = decl
            self.var = var
            self.case = case
            self.number = number
            self.gender = gender
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
        match = True
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' noun'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'NounInfl(decl=' + self.decl + ', var=' + self.var + ', case=' + self.case + \
               ', number=' + self.number + ', gender=' + self.gender + ', stem=' + self.stem + \
               ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi + ', age=' + self.age + \
               ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,NounInfl):
            return False
        return self.decl == other.decl and \
            self.var == other.var and \
            self.case == other.case and \
            self.number == other.number and \
            self.gender == other.gender and \
            self.stem == other.stem and \
            self.ending_uvij == other.ending_uvij and \
            self.ending_vi == other.ending_vi and \
            self.age == other.age and \
            self.frequency == other.frequency


class AdjectiveInfl:
    '''
    Structural version of adjective inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', decl='', var='', case='', number='', gender='', comparison='', stem='', ending=None,
                 age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.var = buildstr[8]
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
            self.var = var
            self.case = case
            self.number = number
            self.gender = gender
            self.comparison = comparison
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
        match = True
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' ' + genders[self.gender] + ' '
        if not less:
            inflstr += 'of ' + adj_declensions[self.decl] + ' '
            if self.comparison:
                inflstr += comparisons[self.comparison] + ' '
            inflstr += 'adjective'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'AdjectiveInfl(decl=' + self.decl + ', var=' + self.var + ', case=' + self.case + \
               ', number=' + self.number + ', gender=' + self.gender + ', comparison=' + self.comparison + \
               ', stem=' + self.stem + ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi + \
               ', age=' + self.age + ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,AdjectiveInfl):
            return False
        return self.decl == other.decl and \
               self.var == other.var and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.comparison == other.comparison and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency


class VerbInfl:
    '''
    Structural version of verb inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', conj='', var='', tense='', voice='', mood='', person='', number='', stem='',
                 ending=None, age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.conj = buildstr[6]
            self.var = buildstr[8]
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
            self.var = var
            self.tense = tense
            self.voice = voice
            self.mood = mood
            self.person = person
            self.number = number
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
        if self.conj:
            if infl.conj != self.conj:
                return False
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += persons[self.person] + ' ' + moods[self.mood] + ' ' + voices[self.voice] + ' '
        inflstr += tenses[self.tense] + ' tense '
        if not less:
            inflstr += 'of ' + verb_conjugations[self.conj] + ' verb'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'VerbInfl(conj=' + self.conj + ', var=' + self.var + ', tense=' + self.tense + \
               ', voice=' + self.voice + ', mood=' + self.mood + ', person=' + self.person + \
               ', number=' + self.number + ', stem=' + self.stem + \
               ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi + ', age=' + \
               self.age + ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,VerbInfl):
            return False
        return self.conj == other.conj and \
               self.var == other.var and \
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


class VerbParticipleInfl:
    '''
    Structural version of verb participle inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', conj='', var='', case='', number='', gender='', tense='', voice='', stem='',
                 ending=None, age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.conj = buildstr[5]
            self.var = buildstr[7]
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
            self.var = var
            self.case = case
            self.number = number
            self.gender = gender
            self.tense = tense
            self.voice = voice
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

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
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += verb_conjugations[self.conj] + ' ' + cases[self.case] + ' ' + numbers[self.number] + ' '
        inflstr += genders[self.gender] + ' ' + voices[self.voice] + ' ' + tenses[self.tense] + ' tense '
        inflstr += 'verb participle'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'VerbParticipleInfl(conj=' + self.conj + ', var=' + self.var + ', case=' + self.case + \
               ', number=' + self.number + ', gender=' + self.gender + ', tense=' + self.tense + \
               ', voice=' + self.voice + ', stem=' + self.stem + \
               ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi + ', age=' + self.age + \
               ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,VerbParticipleInfl):
            return False
        return self.conj == other.conj and \
               self.var == other.var and \
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


class PronounInfl:
    '''
    Structural version of pronoun inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', decl='', var='', case='', number='', gender='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[6]
            self.var = buildstr[8]
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
            self.var = var
            self.case = case
            self.number = number
            self.gender = gender
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' '
            inflstr += 'pronoun'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'PronounInfl(decl=' + self.decl + ', var=' + self.var + ', case=' + self.case + \
               ', number=' + self.number + ', gender=' + self.gender + ', stem=' + self.stem + \
               ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi +', age=' + self.age + \
               ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,PronounInfl):
            return False
        return self.decl == other.decl and \
               self.var == other.var and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency


class NumberInfl:
    '''
    Structural version of number inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', decl='', var='', case='', number='', gender='', kind='', stem='', ending=None, age='',
                 frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.decl = buildstr[7]
            self.var = buildstr[9]
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
            self.var = var
            self.case = case
            self.number = number
            self.gender = gender
            self.kind = kind
            self.stem = stem
            self.ending_uvij = ending
            if ending is not None:
                self.ending_vi = self.ending_uvij.replace('j', 'i').replace('u', 'v')
            else:
                self.ending_vi = ending
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
        if self.decl:
            if infl.decl != self.decl:
                return False
        if self.var:
            if infl.var != self.var:
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
        '''Convert the inflection information into a plaintext, user-friendly form.'''
        inflstr = ''
        inflstr += cases[self.case] + ' ' + numbers[self.number] + ' '
        if not less:
            inflstr += 'of ' + noun_declensions[self.decl] + ' ' + genders[self.gender] + ' '
            if self.kind:
                inflstr += number_kinds[self.kind] + ' '
            inflstr += 'numeral'
        return inflstr.replace('  ', ' ')

    def __repr__(self):
        return 'NumberInfl={decl=' + self.decl + ', var=' + self.var + ', case=' + self.case + \
               ', number=' + self.number + ', gender=' + self.gender + ', kind=' + self.kind + ', stem=' + self.stem + \
               ', ending_uvij=' + self.ending_uvij + ', ending_vi=' + self.ending_vi + ', age=' + self.age + \
               ', frequency=' + self.frequency + ')'

    def __eq__(self,other):
        if not isinstance(other,NumberInfl):
            return False
        return self.decl == other.decl and \
               self.var == other.var and \
               self.case == other.case and \
               self.number == other.number and \
               self.gender == other.gender and \
               self.kind == other.kind and \
               self.stem == other.stem and \
               self.ending_uvij == other.ending_uvij and \
               self.ending_vi == other.ending_vi and \
               self.age == other.age and \
               self.frequency == other.frequency


class AdverbInfl:
    '''
    Structural version of adverb inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', comparison='', stem='', age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.comparison = buildstr[5]
            self.stem = buildstr[11]
            self.age = buildstr[19]
            self.frequency = buildstr[21]
        else:
            self.comparison = comparison
            self.stem = stem
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
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
        return 'AdverbInfl={self.comparison={0}, self.stem={1}, self.age={2}, self.frequency={3})'.format(
            self.comparison, self.stem, self.age, self.frequency)

    def __eq__(self,other):
        if not isinstance(other,AdverbInfl):
            return False
        return self.comparison == other.comparison and \
               self.stem == other.stem and \
               self.age == other.age and \
               self.frequency == other.frequency


class PrepositionInfl:
    '''
    Structural version of preposition inflection codes, for easier searching
    either specify some of the parameters, or use a raw build string (from INFLECTS.LAT)
    If buildstr is given, all other args are ignored
    '''

    def __init__(self, buildstr='', aux_case='', stem='', age='', frequency=''):
        if buildstr:
            # Build from INFLECTS.LAT string
            self.aux_case = buildstr[5]
            self.stem = buildstr[11]
            self.age = buildstr[19]
            self.frequency = buildstr[21]
        else:
            self.aux_case = aux_case
            self.stem = stem
            self.age = age
            self.frequency = frequency

    def matches(self, infl, match_age=False, match_frequency=False):
        '''
        Return True if all nonempty parameters of THIS inflection match the same parameters
        in the GIVEN inflection.
        Note that this will still return True if the given infl has parameters where
        this inflection is empty
        age and frequency are not matched by default
        '''
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
        return 'PrepositionInfl={self.aux_case={0}, self.stem={1}, self.age={2}, self.frequency={3})'.format(
            self.aux_case, self.stem, self.age, self.frequency)

    def __eq__(self,other):
        if not isinstance(other,PrepositionInfl):
            return False
        return self.aux_case == other.aux_case and \
               self.stem == other.stem and \
               self.age == other.age and \
               self.frequency == other.frequency


def build_inflection(buildstr='', part_of_speech='', stem='', ending=None, age='', frequency='', decl='', conj='', var='',
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
        elif pos == 'SUPIN':  # Note: because of indexing the 'E' at the end is cut off
            infl_out = None
        elif pos == 'ADV':
            infl_out = AdverbInfl(buildstr=buildstr)
        elif pos in ['PREP', 'CONJ', 'INTERJ']:
            infl_out = None
        return infl_out
    else:
        # Note: it's fine if entries are empty
        pos = part_of_speech
        if pos == 'N':
            infl_out = NounInfl(decl=decl, var=var, case=case, number=number, gender=gender,
                                stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'ADJ':
            infl_out = AdjectiveInfl(decl=decl, var=var, case=case, number=number, gender=gender,
                                     comparison=comparison, stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'V':
            infl_out = VerbInfl(conj=conj, var=var, tense=tense, voice=voice, mood=mood, number=number,
                                stem=stem, person=person, ending=ending, age=age, frequency=frequency)
        elif pos == 'VPAR':
            infl_out = VerbParticipleInfl(conj=conj, var=var, case=case, number=number, gender=gender,
                                          stem=stem, tense=tense, voice=voice, ending=ending, age=age,
                                          frequency=frequency)
        elif pos == 'PRON':
            infl_out = PronounInfl(decl=decl, var=var, case=case, number=number, gender=gender,
                                   stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'NUM':
            infl_out = NumberInfl(decl=decl, var=var, case=case, number=number, gender=gender, kind=kind,
                                  stem=stem, ending=ending, age=age, frequency=frequency)
        elif pos == 'SUPIN' or pos == 'SUPINE':  # Note: because of indexing the 'E' at the end is cut off
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
        print("FATAL ERROR: Could not find DICTLINE.tsv. This is the file that contains all words and definitions, which PyWORDS uses for word lookup. It should be included in the installation directory.")
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
            var=row['infl_variant'] or '',
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


def get_possible_endings(inflection, part_of_speech, filt=MatchFilter()):
    """
    Return a sorted list of possible endings as strings
    """
    endings = set()
    pos = part_of_speech
    matches = [inf for inf in inflections[pos] if inflection.matches(inf, match_age=True, match_frequency=True)]
    for m in matches:
        if filt.check_inflection(m, pos):
            endings.add(m.ending_vi)
    if pos == 'V':
        # Add supine and vpar endings
        endings.add('vm')
        endings.add('v')
        inflection.var = ''  # Remove variation id
        vpar_matches = [inf for inf in inflections['VPAR'] if
                        inflection.matches(inf, match_age=True, match_frequency=True)]
        for m in vpar_matches:
            if filt.check_inflection(m, 'VPAR'):
                endings.add(m.ending_vi)
        inflection.conj = '0'  # Check common case
        vpar_matches = [inf for inf in inflections['VPAR'] if
                        inflection.matches(inf, match_age=True, match_frequency=True)]
        for m in vpar_matches:
            if filt.check_inflection(m, 'VPAR'):
                endings.add(m.ending_vi)

    return sorted(endings)


def get_possible_inflections(inflection, part_of_speech, filt=MatchFilter()):
    """Return a list of possible inflections as Infl objects"""
    infls = set()
    pos = part_of_speech
    matches = [inf for inf in inflections[pos] if inflection.matches(inf, match_age=True, match_frequency=True)]
    for m in matches:
        if filt.check_inflection(m, pos):
            infls.add(m)
    if pos == 'V':
        inflection.var = ''  # Don't match inflection
        vpar_matches = [inf for inf in inflections['VPAR'] if
                        inflection.matches(inf, match_age=True, match_frequency=True)]
        for m in vpar_matches:
            if filt.check_inflection(m, 'VPAR'):
                infls.add(m)
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
            vpar_matches = [inf for inf in inflections['VPAR'] if
                            inflection.matches(inf)]
            for m in vpar_matches:
                infls.add(m)
    return infls
