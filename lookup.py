# Main methods for looking up words from the dictionary

import PYWORDS.definitions as definitions
from PYWORDS.matchfilter import MatchFilter
import re
import os
import bisect

dictline = []
stems1 = []
stems2 = []
stems3 = []
stems4 = []

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

    # Get sorted stems with original indices
    # enumerate provides iterable with (idx,element) tuples
    # sorted key uses element (e[1]) as sort parameter
    # sorted returns a list of tuples (idx,element), and then all tuples are flipped
    # to give (element,idx)
    global stems1,stems2,stems3,stems4
    stems1 = sorted(enumerate([d['stem1'] for d in dictline],start=0),key=lambda e:e[1])
    stems1 = [(s[1],s[0]) for s in stems1] # Flip elements for comparison later
    stems2 = sorted(enumerate([d['stem2'] for d in dictline],start=0),key=lambda e:e[1])
    stems2 = [(s[1],s[0]) for s in stems2] # Flip elements for comparison later
    stems3 = sorted(enumerate([d['stem3'] for d in dictline],start=0),key=lambda e:e[1])
    stems3 = [(s[1],s[0]) for s in stems3] # Flip elements for comparison later
    stems4 = sorted(enumerate([d['stem4'] for d in dictline],start=0),key=lambda e:e[1])
    stems4 = [(s[1],s[0]) for s in stems4] # Flip elements for comparison later

    orig_dictline = None # Clean up


# Returns a dictionary of stem : ending pairs by starting with no ending and working backwards
def find_endings(w):
    endings = {}
    for i in range(len(w),0,-1):
        wsub = w[i:]
        if wsub in definitions.endings_list:
            endings[w[:i]] = wsub
    return endings


def match_word(w):
    '''
    Return a list of matched words in the format [stem, ending, dictline entry]
    Method: Given word, find possible endings, then check with bisect search for
    each list of stems (stems1, stems2, stems3, stems4)
    During bisect search, find all matching stems, efficiently
    This method is much, much, much faster than brute force
    '''
    matches = []
    endings = find_endings(w)
    for stem,e in endings.items():
        match_ids = []
        idx1_s = bisect.bisect(stems1,(stem,0)) # First entry match
        if idx1_s != len(stems1) and stems1[idx1_s][0] == stem: # if actual match
            idx1_e = idx1_s  # find end index, last element that is a true match
            while stems1[idx1_e][0] == stem and idx1_e+1 < len(stems1):
                idx1_e += 1
            # stems1[idx1_e-1] is now the last matching stem entry
            for i in range(idx1_s,idx1_e):
                if stems1[i][1] not in match_ids:
                    match_ids.append(stems1[i][1]) # append original indices
        idx2_s = bisect.bisect(stems2,(stem,0)) # First entry match
        if idx2_s != len(stems2) and stems2[idx2_s][0] == stem: # if actual match
            idx2_e = idx2_s  # find end index, last element that is a true match
            while stems2[idx2_e][0] == stem and idx2_e+1 < len(stems1):
                idx2_e += 1
            # stems2[idx2_e-1] is now the last matching stem entry
            for i in range(idx2_s,idx2_e):
                if stems2[i][1] not in match_ids:
                    match_ids.append(stems2[i][1]) # append original indices
        idx3_s = bisect.bisect(stems3,(stem,0)) # First entry match
        if idx3_s != len(stems3) and stems3[idx3_s][0] == stem: # if actual match
            idx3_e = idx3_s  # find end index, last element that is a true match
            while stems3[idx3_e][0] == stem and idx3_e+1 < len(stems1):
                idx3_e += 1
            # stems3[idx3_e-1] is now the last matching stem entry
            for i in range(idx3_s,idx3_e):
                if stems3[i][1] not in match_ids:
                    match_ids.append(stems3[i][1]) # append original indices
        idx4_s = bisect.bisect(stems4,(stem,0)) # First entry match
        if idx4_s != len(stems4) and stems4[idx4_s][0] == stem: # if actual match
            idx4_e = idx4_s  # find end index, last element that is a true match
            while stems4[idx4_e][0] == stem and idx4_e+1 < len(stems1):
                idx4_e += 1
            # stems1[idx4_e-1] is now the last matching stem entry
            for i in range(idx4_s,idx4_e):
                if stems4[i][1] not in match_ids:
                    match_ids.append(stems4[i][1]) # append original indices
        if match_ids:
            entries = [dictline[idx] for idx in match_ids]
            for entr in entries:
                matches.append([stem,e,entr])
    matches = [match for match in matches if is_possible_ending(match)]
    return matches

# TODO 
def print_noun_declensions(m):
    '''Print the declensions of a noun
    m must be in the format [stem,ending,dictline] (same as a match)
    '''
    dictline = m[2]
    entry = dictline['entry']
    stem1 = dictline['stem1']
    stem2 = dictline['stem2']


def get_dictionary_string(m, full_info=False, header_only=False):
    '''
    Convert m into a string in dictionary style
    m must be in the format [stem, ending, dictline] (same as a match)
    If full_info is True, all available information is given. 
    If header_only, only the word header is given (no senses)
    '''
    dictstr = ''

    dictline = m[2]
    entry = dictline['entry']
    #stem1 = dictline['stem1']
    #stem2 = dictline['stem2']
    #stem3 = dictline['stem2']
    #stem4 = dictline['stem2']
    if entry.pos == 'N':
        infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'])
        ninfl = definitions.NounInfl(decl=entry.decl,number='S')
        matches = [n for n in definitions.inflections[entry.pos] if ninfl.matches(n)]
        matches = [ma for ma in matches if infl_filt.check_inflection(ma,'N')]
        gender_s = ''
        if matches:
            end1='' # sg nom 
            stem1=''
            end2='' # sg gen
            stem2=''
            for ma in matches:
                if ma.case == 'NOM' and not stem1:
                    end1=ma.ending
                    stem1=ma.stem
                elif ma.case == 'GEN' and not stem2:
                    end2=ma.ending
                    stem2=ma.stem
            if not stem1 and not stem2:
                for ma in matches:
                    if ma.case == 'X':
                        end1 = ''
                        stem1 = '1'
            # Set gender string
            if not header_only:
                if entry.gender == 'C':
                    gender_s = 'masc/fem'
                elif entry.gender == 'N':
                    gender_s = 'neut'
                elif entry.gender == 'M':
                    gender_s = 'masc'
                elif entry.gender == 'F':
                    gender_s = 'fem'

            nom_stem = dictline['stem'+stem1]
            if stem2:
                gen_stem = dictline['stem'+stem2]
                dictstr = nom_stem+end1+', '+gen_stem+end2+' '+gender_s+' '
            else:
                dictstr = nom_stem+end1+' '+gender_s+' '
            if full_info:
                # add age, area, geography, frequency
                dictstr += '('+definitions.dict_frequencies[entry.freq]+', '+\
                        definitions.ages[entry.age]+'. '
                if entry.area != 'X':
                    dictstr += definitions.areas[entry.area]+'. '
                if entry.geog != 'X':
                    dictstr += definitions.geographies[entry.geog]+'). '
                else:
                    dictstr = dictstr.strip(' .')+'). ' # Avoid awkward spaces
                dictstr += 'Source: '+definitions.source_types[entry.src]+'. '
            if not header_only:
                dictstr += ''.join(entry.senses)

    if entry.pos == 'V':
        # ex. singular indicative present active 1st person
        #V     1 1 PRES  ACTIVE  IND  1 S  1 1 o             X A
        # ex. infinitive
        #V     1 1 PRES  ACTIVE  INF  0 X  2 3 are           X A

        vinfl = definitions.VerbInfl(conj=entry.conj,tense='PRES',voice='ACTIVE')

        infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'],
                persons=['0','1'],moods=['IND','INF'])
        matches = [v for v in definitions.inflections[entry.pos] if vinfl.matches(v)]
        matches = [ma for ma in matches if infl_filt.check_inflection(ma,'V')]
        end1='' # sg ind pres active 1st person
        stem1=''
        end2='' # pres active infinitive
        stem2=''
        for ma in matches:
            if ma.person == '1' and ma.mood == 'IND' and not end1:
                end1 = ma.ending
                stem1=ma.stem
            elif ma.mood == 'INF' and not end2:
                end2 = ma.ending
                stem2=ma.stem

        if stem1 and stem2:
            dictstr += dictline['stem'+stem1]+end1+', '
            dictstr += dictline['stem'+stem2]+end2+' '
        else:
            dictstr += m[0]+m[1]+' '

        if not header_only:
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
                dictstr += 'vt '
        if full_info:
            # add age, area, geography, frequency
            dictstr += '('+definitions.dict_frequencies[entry.freq]+', '+\
                    definitions.ages[entry.age]+'. '
            if entry.area != 'X':
                dictstr += definitions.areas[entry.area]+'. '
            if entry.geog != 'X':
                dictstr += definitions.geographies[entry.geog]+'). '
            else:
                dictstr = dictstr.strip(' .')+'). ' # Avoid awkward spaces
            dictstr += 'Source: '+definitions.source_types[entry.src]+'. '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADJ':
        ainfl = definitions.AdjectiveInfl(decl=entry.decl,
                number='S',case='NOM')
        infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'])
        matches = [a for a in definitions.inflections[entry.pos] if ainfl.matches(a)]
        matches = [ma for ma in matches if infl_filt.check_inflection(ma,'ADJ')]
        end1='' # sg nom masc
        stem1=''
        end2='' # sg nom fem
        stem2=''
        end3='' # sg nom neut
        stem3=''
        for ma in matches:
            if ma.gender == 'M' or ma.gender == 'X' or ma.gender == 'C' and not stem1:
                end1 = ma.ending
                stem1 = ma.stem
            if ma.gender == 'F' or ma.gender == 'C' and not stem2:
                end2 = ma.ending
                stem2 = ma.stem
            elif ma.gender == 'N' and not stem3:
                end3 = ma.ending
                stem3 = ma.stem

        # For adjectives it's common for stems to be matching 
        if stem1 and stem2 and stem3:
            stem1 = dictline['stem'+stem1]
            stem2 = dictline['stem'+stem2]
            stem3 = dictline['stem'+stem3]
            if stem1 == stem2 and stem1 == stem3:
                dictstr += stem1+end1+' -'+end2+' -'+end3+' '
            elif stem1 == stem2:
                dictstr += stem1+end1+' -'+end3+' '
            else:
                dictstr += stem1+end1+' '+stem2+end2+' '+stem3+end3+' '
        else:
            dictstr += m[0]+m[1]+' '
        if not header_only:
            dictstr += 'adj '
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'PRON':
        infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'])
        pinfl = definitions.PronounInfl(decl=entry.decl,number='S')
        matches = [p for p in definitions.inflections[entry.pos] if pinfl.matches(p)]
        matches = [ma for ma in matches if infl_filt.check_inflection(ma,'PRON')]
        if matches:
            end1='' # sg nom 
            stem1=''
            end2='' # sg gen
            stem2=''
            for ma in matches:
                if ma.case == 'NOM' and not stem1:
                    end1=ma.ending
                    stem1=ma.stem
                elif ma.case == 'GEN' and not stem2:
                    end2=ma.ending
                    stem2=ma.stem
            if not stem1 and not stem2:
                for ma in matches:
                    if ma.case == 'X':
                        end1 = ''
                        stem1 = '1'
            if not stem1:
                stem1='1'

            nom_stem = dictline['stem'+stem1]
            if stem2:
                gen_stem = dictline['stem'+stem2]
                dictstr = nom_stem+end1+', '+gen_stem+end2+' '
            else:
                dictstr = nom_stem+end1+' '

            if full_info:
                # add age, area, geography, frequency
                dictstr += '('+definitions.dict_frequencies[entry.freq]+', '+\
                        definitions.ages[entry.age]+'. '
                if entry.area != 'X':
                    dictstr += definitions.areas[entry.area]+'. '
                if entry.geog != 'X':
                    dictstr += definitions.geographies[entry.geog]+'). '
                else:
                    dictstr = dictstr.strip(' .')+'). ' # Avoid awkward spaces
                dictstr += 'Source: '+definitions.source_types[entry.src]+'. '
            if not header_only:
                dictstr += ''.join(entry.senses)
        
    elif entry.pos == 'CONJ':
        dictstr = dictline['stem1'] + ' conj '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADV':
        dictstr = dictline['stem1'] + ' adv '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos in ['PREP','PACK']:
        dictstr = dictline['stem1'] + ' prep '
        if not header_only:
            dictstr += ''.join(entry.senses)
    return dictstr.replace('  ',' ').strip(' ')

def is_possible_ending(match):
    entry = match[2]['entry']
    pos = entry.pos
    if pos in ['PREP','PACK','TACKON','SUFFIX','PREFIX','X']:
        return True # TODO
    infl = None
    if pos == 'V':
        infl = definitions.build_inflection(part_of_speech=entry.pos,conj=entry.conj)
    elif pos in ['N','ADJ','PRON','NUM']:
        infl = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl)
    elif pos in ['ADV','PREP','CONJ','INTERJ']:
        if match[1] != '':
            return False
        else:
            return True
    possible_endings = definitions.get_possible_endings(infl,entry.pos)
    if match[1] in possible_endings:
        return True
    else:
        return False

def get_word_inflections(match,less=False):
    '''
    Use a match (from match_word) to look up the possible inflections of a word. Returned as list of plain text
    strings.
    If less is False, information about the word is printed along with the inflection. If
    less is True, only the inflection information and the word header are printed.
    '''
    entry = match[2]['entry']
    infl_strings = []
    head = get_dictionary_string(match,header_only=True)
    pos = entry.pos
    if pos in ['PREP','PACK','TACKON','SUFFIX','PREFIX','X']:
        return []
    infl = None
    if pos == 'V':
        infl = definitions.build_inflection(part_of_speech=entry.pos,conj=entry.conj,ending=match[1])
    elif pos in ['N','ADJ','PRON','NUM']:
        infl = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl,ending=match[1])
    elif pos in ['ADV','PREP','CONJ','INTERJ']:
        return []
    possible_infls = definitions.get_possible_inflections(infl,pos)
    for minfl in possible_infls:
        if less:
            infl_strings.append(minfl.get_inflection_string(less=less)+'of '+head)
        else:
            infl_strings.append(minfl.get_inflection_string(less=less)+' '+head)
    return infl_strings

def get_vocab_list(text,filt=MatchFilter()):
    '''
    Take an arbitrarily long string (newlines and all) and process each word,
    then compile dictionary entries.
    '''
    tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]',text)
    tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]
    
    defns = set()
    missed = set()
    for w in tlist:
        ms = match_word(w)
        if len(ms) == 0:
            missed.add(w)
        #filt.remove_substantives(ms)
        wdefns = []
        for m in ms:
            if filt.check_dictline_word(m[2]['entry']):
                wdefns.append(get_dictionary_string(m))
        for wdefn in wdefns:
            if wdefn != '':
                defns.add(wdefn)

    defns_sort = sorted(defns)
    missed_sort = sorted(missed)
    return (defns_sort,missed_sort)
 
def find_example_sentences(text,word,word_filt=MatchFilter(),infl_filt=MatchFilter()):
    word_matches = match_word(word)

    if not word_matches:
        print("Word "+word+" doesn't seem to be in the dictionary. Check your spelling and try again.")
        return None
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    word_matches = [match for match in word_matches if word_filt.check_dictline_word(match[2]['entry'])]
    if len(word_matches) > 1:
        print("Which word did you mean? ")
        for i,match in enumerate(word_matches):
            print(alphabet[i]+") "+get_dictionary_string(match))
        chosen=False
        while not chosen:
            choice = input('WORD: ')
            if choice in alphabet[:len(word_matches)]:
                word_match = word_matches[alphabet.index(choice)]
                chosen=True
    else:
        word_match = word_matches[0]
    print("\nFinding example sentences of word: ",end='')
    print(get_dictionary_string(word_match))

    sentences = text.replace('\n',' ').split('.') # Try to roughly split into sentences
    matched_sentences = []
    for sentence in sentences:
        tlist = re.split('[, \n!.\-:;?=+/\'\"^\\]\\[]',sentence)
        tlist = [t.lower() for t in tlist if t and t.isalpha() and len(t) > 1]
        
        for w in tlist:
            ms = match_word(w)
            for m in ms:
                if m[2]['entry'] == word_match[2]['entry'] and sentence.strip()+'.' not in matched_sentences:
                    matched_sentences.append(sentence.strip()+'.')
                    

    print("Found %d sentences." % (len(matched_sentences)))
    return matched_sentences


load_dictionary()
definitions.load_inflections()

if __name__ == '__main__':
    words = ['hoc', 'cognomine', 'appellare', 'liceat', 'illam', 'maxime', 'memorabilem', 'seriem','bonum','nos']
    filt = MatchFilter()

    

#    for w in words:
#        ms = match_word(w)
#        filt.remove_substantives(ms)
#        for m in ms:
#            print(get_dictionary_string(m))



