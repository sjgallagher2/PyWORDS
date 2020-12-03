# Main methods for looking up words from the dictionary

import definitions
import bisect

dictline = []

def load_dictionary():
    f = open('data/DICTLINE.GEN')
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
        # inflection is:
        # pos decl var [case number] gender {x x} ending {age frequency}
        # Where the square brackets indicate we need to find these values, 
        # curly brackets indicate this value is unique to a given [case,number] 
        # pair
        pos=entry.pos
        decl=entry.decl
        var=entry.variant
        gender=[entry.gender]
        if gender[0] in ['M','F']:
            gender.append('X')


        code_start = pos+' '+decl+' '+var # Beginning of code
        
        code_matches=[]
        infl_matches=[]
        for code,infl in definitions.noun_inflections.items():
            if code.startswith(code_start):
                code_matches.append(code)
                infl_matches.append(infl)
        match_idx = []
        for i in range(len(code_matches)):
            if code_matches[i][12] in gender and infl_matches[i]['ending']==ending:
                match_idx.append(i)
        code_matches = [code_matches[i] for i in match_idx]
        infl_matches = [infl_matches[i] for i in match_idx] 

        return (code_matches,infl_matches)
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
        return [ 'PREP GEN 1 0 X A',
                'PREP ACC 1 0 X A',
                'PREP ABL 1 0 X A' ]
    elif part_of_speech == 'conjunction': # No endings, list is always the same
        return 'CONJ 1 0 X A'
    elif part_of_speech == 'interjection': # No endings, list is always the same
        return 'INTERJ 1 0 X A'

    return

 

if __name__ == '__main__':
    load_dictionary()
    words = ['hoc', 'cognomine', 'appellare', 'liceat', 'illam', 'maxime', 'memorabilem', 'seriem','bonum']
    filt = MatchFilter()

    for w in words:
#        print("Word: "+w)
        ms = match_word(w)
        ms = filt.remove_substantives(ms)
#        print("Matches: ")
#        for m in ms:
#            print(m,end=' => ')
#            print(m[2]['entry'])
#        print()
        m = ms[0]


