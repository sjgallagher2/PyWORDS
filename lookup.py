# Main methods for looking up words from the dictionary

import PYWORDS.definitions as definitions
import re
import os

dictline = []

def load_dictionary():
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/DICTLINE.GEN'))
    orig_dictline = f.readlines()
    f.close()
    for l in orig_dictline:
        dictline.append( {'stem1':l[0:19].strip(),
                    'stem2':l[19:38].strip(),
                    'stem3':l[38:57].strip(),
                    'stem4':l[57:76].strip(),
                    'entry':definitions.build_dictline_entry(l[76:].strip())})
    orig_dictline = None # Clean up


class MatchFilter:
    '''Collection of flags used to filter word matches'''
    def __init__(self):
        self.substantives = True  # Show noun forms of adjectives
        self.ages = ['A','B','C','D','E','F','G','H','X'] # Coded time periods that are valid
        self.areas = ['A','B','D','E','G','L','P','S','T','W','Y','X']
        self.geographies=['A','B','C','D','E','F','G','H','I','J','K','N','P','Q','R','S','U','X']
        self.frequencies=['A','B','C','D','E','F','I','M','N','X']

        self.noun_declensions=['1','2','3','4','5','9']
        self.verb_conjugations=['0','1','2','3','4','5','6','7','8','9']
        self.adj_declensions=['0','1','2','3','9']
        self.noun_kinds=['S','M','A','G','N','P','T','L','W','X']
        self.verb_kinds=['TO_BE','TO_BEING','GEN','DAT','ABL','TRANS','INTRANS','IMPERS','DEP','SEMIDEPO','PERFEF','X']
        self.number_kinds=['CARD','ORD','DIST','ADVERB','X']
        self.pronoun_kinds=['PERS','REL','REFLEX','DEMONS','INTERR','INDEF','ADJECT','X']
        self.comparisons=['POS','COMP','SUPER','X']
        self.moods=['IND','SUB','IMP','INF','PPL','X']
        self.genders=['M','F','N','C','X']
        self.persons=['0','1','2','3']
        self.numbers=['S','P','X']
        self.tenses=['PRES','IMPF','PERF','FUT','FUTP','PLUP','INF','X']
        self.voices=['ACTIVE','PASSIVE','X']
    def check_dictline_word(self,w):
        # Return True if word is OK
        return True
    def check_inflection(self,infl):
        # Return True if word is OK
        return True
    def remove_substantives(self,matches):
        '''
        Return list of substantive adjectives from list of matches
        NOTE: This is aggressive. If an adjective is found, ALL nouns with matching stems will be removed. With a
        word like 'bonum' this is safe. Other words might not be. 
        '''
        filtmatches = matches
        adjs = set()
        # First make a list of adjectives
        for m in matches:
            e = m[2]['entry']
            if e.pos == 'ADJ':
                adjs.add(m[2]['stem2'])
        for stem in adjs:
            for m in filtmatches[:]:
                if m[2]['stem2'] == stem and m[2]['entry'].pos == 'N':
                    filtmatches.remove(m)
        return filtmatches

# Returns a dictionary of stem : ending pairs by starting with no ending and working backwards
def find_endings(w):
    endings = {}
    for i in range(len(w),0,-1):
        wsub = w[i:]
        if wsub in definitions.endings_list:
            endings[w[:i]] = wsub
    return endings

def match_word(w,filt=None):
    '''
    Return a list of matched words in the format [stem, ending, dictline entry]
    '''
    matches = []
    endings = find_endings(w)
    for stem,e in endings.items():
        for l in dictline:
            if stem == l['stem1']:
                matches.append([stem,e,l])
            elif stem == l['stem2']:
                matches.append([stem,e,l])
            elif stem == l['stem3']:
                matches.append([stem,e,l])
            elif stem == l['stem4']:
                matches.append([stem,e,l])
    return matches

def print_noun_declensions(m):
    '''Print the declensions of a noun
    m must be in the format [stem,ending,dictline] (same as a match)
    '''
    dictline = m[2]
    entry = dictline['entry']
    stem1 = dictline['stem1']
    stem2 = dictline['stem2']
    basecode_sg = definitions.NounCode(decl=entry.decl,var=entry.variant,number='S')
    basecode_pl = definitions.NounCode(decl=entry.decl,var=entry.variant,number='P')
    endings_sg = definitions.get_noun_case_endings(basecode_sg)
    endings_pl = definitions.get_noun_case_endings(basecode_pl)

    print('-------------------------------------')
    print(stem1+endings_sg['nominative'][0]['ending']+', '+stem2+endings_sg['genitive'][0]['ending'])
    print('-------------------------------------')
    print('Nom. | '+stem1+endings_sg['nominative'][0]['ending']+'\t'+stem2+endings_pl['nominative'][0]['ending'])
    print('Gen. | '+stem1+endings_sg['genitive'][0]['ending']+'\t'+stem2+endings_pl['genitive'][0]['ending'])
    print('Dat. | '+stem1+endings_sg['dative'][0]['ending']+'\t'+stem2+endings_pl['dative'][0]['ending'])
    print('Acc. | '+stem1+endings_sg['accusative'][0]['ending']+'\t'+stem2+endings_pl['accusative'][0]['ending'])
    print('Abl. | '+stem1+endings_sg['ablative'][0]['ending']+'\t'+stem2+endings_pl['ablative'][0]['ending'])



def get_dictionary_string(m, full_info=False):
    '''
    Convert m into a string in dictionary style
    m must be in the format [stem, ending, dictline] (same as a match)
    if full_info is True, all available information is given. 
    '''
    dictstr = ''

    dictline = m[2]
    entry = dictline['entry']
    stem1 = dictline['stem1']
    stem2 = dictline['stem2']
    if entry.pos == 'N':
        basecode_sg = definitions.NounCode(decl=entry.decl,var=entry.variant,number='S')
        endings_sg = definitions.get_noun_case_endings(basecode_sg)
        if endings_sg['nominative'] and endings_sg['genitive']:
            dictstr = stem1+endings_sg['nominative'][0]['ending']+', '+stem2+endings_sg['genitive'][0]['ending']+' '
            if entry.gender == 'C':
                dictstr += 'masc/fem '
            elif entry.gender in ['M','F']:
                dictstr += entry.gender.lower()+' '
            elif entry.gender == 'N':
                dictstr += 'neut '
            dictstr += ''.join(entry.senses)
    if entry.pos == 'V':
        ending = definitions.get_verb_sg_firstperson_ending(entry.conj)
        if ending:
            dictstr = stem1+ending+', '
            dictstr += stem2+definitions.get_verb_infinitive_ending(entry.conj)+' '
            if entry.verb_kind == 'TRANS':
                dictstr += 'vt '
            elif entry.verb_kind == 'INTRANS':
                dictstr += 'vi '
            elif entry.verb_kind == 'SEMIDEP':
                dictstr += 'v semidep '
            elif entry.verb_kind == 'DEP':
                dictstr += 'v dep '
            elif entry.verb_kind == 'IMPERS':
                dictstr += 'impers v '
            elif entry.verb_kind == 'PERFDEF':
                dictstr += 'perf def v '
            elif entry.verb_kind == 'GEN':
                dictstr += '(w/ gen) '
            elif entry.verb_kind == 'DAT':
                dictstr += '(w/ dat) '
            elif entry.verb_kind == 'ABL':
                dictstr += '(w/ abl) '
            else:
                dictstr += 'v '
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADJ':
        endings = definitions.get_adj_sg_nom_endings(entry.decl,entry.variant)
        dictstr = stem1+endings['masc']+' -'+endings['fem']+' -'+endings['neut']+' adj '
        dictstr += ''.join(entry.senses)
    elif entry.pos == 'PRON':
        endings = definitions.get_pronoun_sg_nom_endings(entry.decl,entry.variant)
        if endings['masc'] or endings['fem'] or endings['neut']:
            dictstr = stem1+endings['masc']+' -'+endings['fem']+' -'+endings['neut']+' pron '
        elif 'common' in endings.keys():
            dictstr = stem1+endings['common']+' pron '
        else:
            endings = definitions.get_pronoun_pl_nom_endings(entry.decl,entry.variant)
            if endings['masc'] or endings['fem'] or endings['neut']:
                dictstr = stem1+endings['masc']+' -'+endings['fem']+' -'+endings['neut']+' pron '
            elif 'common' in endings.keys():
                dictstr = stem1+endings['common']+' pron '
        dictstr += ''.join(entry.senses)
    elif entry.pos == 'CONJ':
        dictstr = stem1 + ' conj '
        dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADV':
        dictstr = stem1 + ' adv '
        dictstr += ''.join(entry.senses)
    elif entry.pos in ['PREP','PACK']:
        dictstr = stem1 + ' prep '
        dictstr += ''.join(entry.senses)

        
    return dictstr

# TODO 
def find_match_inflections(m):
    '''
    Return a list of possible inflections codes given the match information
    '''
    stem = m[0]
    ending = m[1]
    dictline = m[2]
    entry = dictline['entry']

    part_of_speech = entry.get_part_of_speech()

    inflections = [] # return variable

    if part_of_speech == 'noun':
        return
    elif part_of_speech == 'adjective':
        return
    elif part_of_speech == 'verb':
        return
    elif part_of_speech == 'preposition':
        return
    elif part_of_speech == 'pronoun':
        return
    elif part_of_speech == 'number':
        return
    elif part_of_speech == 'adverb': # No endings, list is always the same
        return ['ADV X 1 0 X A',
                'ADV X 2 0 X A',
                'ADV X 3 0 X A',
                'ADV POS 1 0 X A',
                'ADV COMP 1 0 X A',
                'ADV SUPER 1 0 X A']
    elif part_of_speech == 'preposition': # No endings, list is always the same
        return ['PREP GEN 1 0 X A',
                'PREP ACC 1 0 X A',
                'PREP ABL 1 0 X A' ]
    elif part_of_speech == 'conjunction': # No endings, list is always the same
        return 'CONJ 1 0 X A'
    elif part_of_speech == 'interjection': # No endings, list is always the same
        return 'INTERJ 1 0 X A'

    return

def print_vocab_list(text):
    # text should be a string with any number of words, and this will print a vocab list
    filt = MatchFilter()

    tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]',text)
    tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]
    
    defns = set([])
    for w in tlist:
        ms = match_word(w)
        filt.remove_substantives(ms)
        wdefns = []
        for m in ms:
            wdefns.append(get_dictionary_string(m))
        for wdefn in wdefns:
            if wdefn != '':
                defns.add(wdefn)

    defns_sort = sorted(defns)
    return defns_sort
 


load_dictionary()

if __name__ == '__main__':
    words = ['hoc', 'cognomine', 'appellare', 'liceat', 'illam', 'maxime', 'memorabilem', 'seriem','bonum','nos']
    filt = MatchFilter()

    for w in words:
        ms = match_word(w)
        filt.remove_substantives(ms)
        for m in ms:
            print(get_dictionary_string(m))



