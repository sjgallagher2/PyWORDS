# Main methods for looking up words from the dictionary

import pywords.definitions as definitions
from pywords.matchfilter import MatchFilter
import os
import os.path
import bisect
import csv

dictline = []
dictline_ignoreuvij = []
stems1 = []
stems2 = []
stems3 = []
stems4 = []


def load_dictionary():
    """
    Load main dictionary database

    To handle the u/v and i/j problems, two almost identical copies are made
    (not ideal I know), one with dictionary spelling, one with all u's and i's 
    replaced with v's and j's (resp.). We perform searches using the latter,
    but return the former. It's a workaround.
    """
    global stems1,stems2,stems3,stems4
    global dictline
    global dictline_ignoreuvij

    dl_fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/DICTLINE.tsv')
    if not os.path.exists(dl_fname):
        print("FATAL ERROR: Could not find DICTLINE.tsv. This is the file that contains all words and definitions, which PyWORDS uses for word lookup. It should be included in the installation directory.")
        raise FileNotFoundError
    with open(dl_fname) as f:
        reader = csv.DictReader(f,delimiter='\t')
        dictline_rows = [row for row in reader]

    # First get column names and index them in case the order changes
    # Get dictline table
    # For every entry, populate global `dictline`
    for row in dictline_rows:
        stem1 = row['dl_stem1'] or ''
        stem2 = row['dl_stem2'] or ''
        stem3 = row['dl_stem3'] or ''
        stem4 = row['dl_stem4'] or ''
        entry = definitions.build_dictline_entry(row)

        dictline.append( {'stem1':stem1,
                          'stem2':stem2,
                          'stem3':stem3,
                          'stem4':stem4,
                          'entry':entry})
        dictline_ignoreuvij.append( {'stem1':stem1.replace('j','i').replace('u','v'),
                          'stem2':stem2.replace('j','i').replace('u','v'),
                          'stem3':stem3.replace('j','i').replace('u','v'),
                          'stem4':stem4.replace('j','i').replace('u','v'),
                          'entry':entry})

    # Get sorted stems with original indices
    # enumerate provides iterable with (idx,element) tuples
    # sorted key uses element (e[1]) as sort parameter
    # sorted returns a list of tuples (idx,element), and then all tuples are flipped
    # to give (element,idx)
    stems1 = sorted(enumerate([d['stem1'] for d in dictline_ignoreuvij],start=0),key=lambda e:e[1])
    stems1 = [(s[1],s[0]) for s in stems1] # Flip elements for comparison later
    stems2 = sorted(enumerate([d['stem2'] for d in dictline_ignoreuvij],start=0),key=lambda e:e[1])
    stems2 = [(s[1],s[0]) for s in stems2] # Flip elements for comparison later
    stems3 = sorted(enumerate([d['stem3'] for d in dictline_ignoreuvij],start=0),key=lambda e:e[1])
    stems3 = [(s[1],s[0]) for s in stems3] # Flip elements for comparison later
    stems4 = sorted(enumerate([d['stem4'] for d in dictline_ignoreuvij],start=0),key=lambda e:e[1])
    stems4 = [(s[1],s[0]) for s in stems4] # Flip elements for comparison later

    dictline_rows = None # Clean up


def find_endings(w,skip_zero=False):
    """ 
    Returns a list of 'splits', index where the split occurs, such that the stem is w[:split_idx]
    and the ending is w[split_idx:]
    If skip_zero==True, assume there is an ending and start with 1 letter instead of ending=''
    """
    endings = {}
    splits = []
    w = w.replace('u','v').replace('j','i')  # Verify the word is VI and not UVIJ
    if skip_zero:
        for i in range(len(w)-1,0,-1):
            wsub = w[i:]
            if wsub in definitions.endings_list_vi:
                endings[w[:i]] = wsub
                splits.append(i)
    else:
        for i in range(len(w),0,-1):
            wsub = w[i:]
            if wsub in definitions.endings_list_vi:
                endings[w[:i]] = wsub
                splits.append(i)
    return splits

def _simple_match(w):
    """
    Core word match method. Tries all stem/ending combinations that are valid and searches
    for the stem in the dictionary. Finally, checks that ending is a valid ending given the
    dictline entry (declension, conjugation, variant, etc).

    Return a list of matched words in the format [stem, ending, dictline entry]
    """
    matches = []
    raw_w = w
    w = w.replace('j', 'i').replace('u', 'v')
    end_splits = find_endings(w)  # Get potential stem/ending pairs (ignores inflection)

    for split_idx in end_splits:
        stem = w[:split_idx]
        e = w[split_idx:]
        match_ids = []
        # STEM SEARCH
        # Search for stem in each stem column (1,2,3,4)
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
            # GET DICTLINE ENTRIES
            entries = [dictline[idx] for idx in match_ids]
            for entr in entries:
                # ONLY return the original word (with u, v, i, and j instead of just v and i)
                matches.append([raw_w[:split_idx],raw_w[split_idx:],entr])

    # VALIDATE STEM/ENDING PAIRS
    matches = [match for match in matches if is_possible_ending(match)]
    return matches


def _remove_enclitics(w):
    if w[-3:] == 'que':
        w = w[:len(w)-3] # Remove the 'que'
    elif w[-2:] == 'ne':
        w = w[:len(w)-2] # Remove the 'ne'
    elif w[-2:] == 've':
        w = w[:len(w)-2] # Remove the 've'
    return w


def match_word(w):
    """
    Try to match a word, with basic tricks. If use_tricks is used, more in depth matching
    methods are used (not implemented)
    """
    finished=False
    removed_encls = False

    while not finished:
        matches = _simple_match(w)
        if len(matches)>0:
            finished = True
        elif not removed_encls:
            w = _remove_enclitics(w)
            removed_encls = True
        else: # Search failed
            finished = True


    return matches

# TODO 
def print_noun_declensions(m):
    """
    Print the declensions of a noun
    m must be in the format [stem,ending,dictline] (same as a match)
    """
    dictline = m[2]
    entry = dictline['entry']
    stem1 = dictline['stem1']
    stem2 = dictline['stem2']


def get_dictionary_string(m, full_info=False, header_only=False, markdown_fmt=False):
    """
    Convert m into a string in dictionary style
    m must be in the format [stem, ending, dictline] (same as a match)
    If full_info is True, all available information is given. 
    If header_only, only the word header is given (no senses)
    If markdown_fmt, place headwords in bold (**ex**), part of speech in italics (*ex*)

    TODO This whole thing could be rewritten to be less hacky
    """
    dictstr = ''

    dictline = m[2]
    entry = dictline['entry']
    # For reference:
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
                    end1=ma.ending_uvij
                    stem1=ma.stem
                elif ma.case == 'GEN' and not stem2:
                    end2=ma.ending_uvij
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
                if markdown_fmt:
                    dictstr += '**'
                dictstr += nom_stem+end1+', '+gen_stem+end2
                if markdown_fmt:
                    dictstr += '** *'
                else:
                    dictstr += ' '
                dictstr += gender_s
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            else:
                if markdown_fmt:
                    dictstr += '**'
                dictstr += nom_stem+end1
                if markdown_fmt:
                    dictstr += '** *'
                else:
                    dictstr += ' '
                dictstr += gender_s
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '

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

        # TODO Fix semi-deponent, defective, and impersonal verbs

        if entry.verb_kind == 'DEP':
            vinfl = definitions.VerbInfl(conj=entry.conj,tense='PRES',voice='PASSIVE')
        elif entry.verb_kind == 'SEMIDEP':
            vinfl = definitions.VerbInfl(conj=entry.conj,tense='PRES',voice='ACTIVE')
        else:
            vinfl = definitions.VerbInfl(conj=entry.conj,tense='PRES',voice='ACTIVE')

        if entry.verb_kind == 'IMPERS':
            infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'],
                    persons=['0','3'],moods=['IND','INF'])
        else:
            infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'],
                    persons=['0','1'],moods=['IND','INF'])
        matches = [v for v in definitions.inflections[entry.pos] if vinfl.matches(v)]
        matches = [ma for ma in matches if infl_filt.check_inflection(ma,'V')]
        end1='' # sg ind pres active 1st person
        stem1=''
        end2='' # pres active infinitive
        stem2=''
        for ma in matches:
            if entry.verb_kind == 'IMPERS':
                if ma.person == '3' and ma.mood == 'IND' and not end1:
                    end1 = ma.ending_uvij
                    stem1=ma.stem
                elif ma.mood == 'INF' and not end2:
                    end2 = ma.ending_uvij
                    stem2 = ma.stem
            else:
                if ma.person == '1' and ma.mood == 'IND' and not end1:
                    end1 = ma.ending_uvij
                    stem1=ma.stem
                elif ma.mood == 'INF' and not end2:
                    end2 = ma.ending_uvij
                    stem2 = ma.stem

        if stem1 and stem2:
            if markdown_fmt:
                dictstr += '**'
            dictstr += dictline['stem'+stem1]+end1
            dictstr += ', '
            dictstr += dictline['stem'+stem2]+end2
            if dictline['stem3'] != 'zzz':
                dictstr += ', '
                if entry.verb_kind == 'IMPERS':
                    dictstr += dictline['stem3']+'it'
                else:
                    dictstr += dictline['stem3']+'i'
            if dictline['stem4'] != 'zzz':
                dictstr += ', '
                if entry.verb_kind == 'IMPERS':
                    dictstr += dictline['stem4']+'um est'
                else:
                    dictstr += dictline['stem4']+'us'
                if entry.verb_kind in ['DEP','SEMIDEP']:
                    dictstr += ' sum'
            if markdown_fmt:
                dictstr += '**'
            dictstr += ' '

        else:
            if markdown_fmt:
                dictstr += '**'
            dictstr += m[0]+m[1]
            if markdown_fmt:
                dictstr += '**'
            dictstr += ' '

        if not header_only:
            if entry.conj in ['1','2']:
                dictstr += '['+entry.conj+'] '
            elif entry.conj in ['3','8']:
                if entry.variant in ['0','1']:
                    dictstr += '[3] '
                elif entry.variant in ['2','3']:
                    dictstr += '[irreg] '
                elif entry.variant == '4':
                    dictstr += '[4] '
            elif entry.conj == '7':
                if entry.variant in ['1','3']:
                    dictstr += '[3] '
                else:
                    dictstr += '[irreg] '
            elif entry.conj in ['5','6']:
                dictstr += '[irreg] ' # Irregular
            # else      Abbreviations, indeclinable, etc can be skipped
            
            if entry.verb_kind == 'TRANS':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'vt'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'INTRANS':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'vi'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'SEMIDEP':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'v semidep'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'DEP':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'v dep'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'IMPERS':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'impers v'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'PERFDEF':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'perf def v'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'GEN':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += '(w/ gen)'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'DAT':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += '(w/ dat)'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            elif entry.verb_kind == 'ABL':
                if markdown_fmt:
                    dictstr += '*'
                dictstr += '(w/ abl)'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
            else:
                if markdown_fmt:
                    dictstr += '*'
                dictstr += 'vt'
                if markdown_fmt:
                    dictstr += '*'
                dictstr += ' '
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
    elif entry.pos == 'ADJ' or entry.pos == 'NUM':
        # Numeric declines like adjective

        # NOTE: Comparisons with adjectives are tricky, because there are two separate examples:
        # first, there are adjectives with 4 stems and a declension and variant like 1 1; then
        # e.g. the 4th stem is the superlative
        # second, there are adjectives with declension and variant like 0 0, for which only the
        # 1st stem is present, and therefore acts as the superlative (or comp.)
        # I've updated DICTLINE.GEN so that COMP and SUPER adjectives of declension 0 0 are
        # in the same stem slot
        ainfl = definitions.AdjectiveInfl(decl=entry.decl,
                number='S',case='NOM')
        if entry.pos == 'ADJ':
            if entry.comparison != 'POS':
                ainfl.comparison = entry.comparison
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
                end1 = ma.ending_uvij
                stem1 = ma.stem
            if ma.gender == 'F' or ma.gender == 'C' and not stem2:
                end2 = ma.ending_uvij
                stem2 = ma.stem
            elif ma.gender == 'N' and not stem3:
                end3 = ma.ending_uvij
                stem3 = ma.stem
        if stem1 and not stem2 and not stem3:
            stem2 = stem1
            end2 = end1
            stem3 = stem1
            end3 = end1

        # For adjectives it's common for stems to be matching 
        if stem1 and stem2 and stem3:
            stem1 = dictline['stem'+stem1]
            stem2 = dictline['stem'+stem2]
            stem3 = dictline['stem'+stem3]
            if stem1 == stem2 and stem1 == stem3:
                if markdown_fmt:
                    dictstr += '**'
                dictstr += stem1+end1+' -'+end2+' -'+end3
                if markdown_fmt:
                    dictstr += '**'
                dictstr += ' '
            elif stem1 == stem2:
                if markdown_fmt:
                    dictstr += '**'
                dictstr += stem1+end1+' -'+end3
                if markdown_fmt:
                    dictstr += '**'
                dictstr += ' '
            else:
                if markdown_fmt:
                    dictstr += '**'
                dictstr += stem1+end1+' '+stem2+end2+' '+stem3+end3
                if markdown_fmt:
                    dictstr += '**'
                dictstr += ' '
        else:
            if markdown_fmt:
                dictstr += '**'+m[0]+m[1]+'** '
            else:
                dictstr += m[0]+m[1]+' '
        if not header_only:
            if markdown_fmt:
                dictstr += '*'
            if entry.pos == 'ADJ':
                dictstr += 'adj'
            else:
                dictstr += 'num adj'
            if markdown_fmt:
                dictstr += '*'
            dictstr += ' '
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
                    end1=ma.ending_uvij
                    stem1=ma.stem
                elif ma.case == 'GEN' and not stem2:
                    end2=ma.ending_uvij
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
        if markdown_fmt:
            dictstr = '**'+dictline['stem1'] + '** *conj* '
        else:
            dictstr = dictline['stem1'] + ' conj '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADV':
        # TODO Add comparison
        if markdown_fmt:
            dictstr = '**'+dictline['stem1']+'** *adv* '
        else:
            dictstr = dictline['stem1'] + ' adv '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'NUM':
        # TODO Placeholder until I get the chance to properly format
        # Numbers share declension/variant codes with adjectives
        if markdown_fmt:
            dictstr = '**'+dictline['stem1']+'** *num* '
        else:
            dictstr = dictline['stem1'] + ' num '
        if not header_only:
            dictstr += ''.join(entry.senses)

    elif entry.pos in ['PREP','PACK']:
        # TODO Split these, add preposition information
        if markdown_fmt:
            dictstr = '**'+dictline['stem1'] + '** *prep* '
        else:
            dictstr = dictline['stem1'] + ' prep '
        if not header_only:
            dictstr += ''.join(entry.senses)
    return dictstr.replace('  ',' ').strip(' ')

def is_possible_ending(match):
    """
    Check whether a match [stem,ending,dictline entry] is possible
    match should be returned from e.g. _simple_match and should be in uvij format
    """
    entry = match[2]['entry']
    # Find which stem we're working with
    match_stem = match[0].replace('j','i').replace('u','v')
    stems = [match[2]['stem1'].replace('j','i').replace('u','v'),
             match[2]['stem2'].replace('j','i').replace('u','v'),
             match[2]['stem3'].replace('j','i').replace('u','v'),
             match[2]['stem4'].replace('j','i').replace('u','v')]
    stem_ids = [str(s+1) for s,x in enumerate(stems) if x == match_stem]

    # Get part of speech, handle internal-only parts for now
    pos = entry.pos
    if pos in ['PACK','TACKON','SUFFIX','PREFIX','X']:
        return True # TODO?
    infl = None
    possible_endings = []
    for stem_id in stem_ids:
        if pos == 'V':
            # TODO Check for verb type and limit options based on that
            infl1 = definitions.build_inflection(part_of_speech=entry.pos,conj=entry.conj,stem=stem_id,var=entry.variant)  # Ignoring variant to account for var 0
            infl2 = definitions.build_inflection(part_of_speech=entry.pos,conj=entry.conj,stem=stem_id,var='0')  # Ignoring variant to account for var 0
        elif pos in ['N','ADJ','PRON','NUM']:
            infl1 = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl,stem=stem_id,var=entry.variant)
            infl2 = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl,stem=stem_id,var='0')
        elif pos in ['ADV','PREP','CONJ','INTERJ']:
            if match[1] != '':
                return False
            else:
                return True
        possible_endings += definitions.get_possible_endings(infl1,entry.pos)  # With specified variant
        # TODO Does generic variant only apply to some of the other variants?
        possible_endings += definitions.get_possible_endings(infl2, entry.pos)  # With generic variant
    if match[1].replace('u','v').replace('j','i') in possible_endings:
        return True
    else:
        # Check for COMP and SUPER adjectives
        if pos == 'ADJ':
            for stem_id in stem_ids:
                infl = definitions.build_inflection(part_of_speech=entry.pos,decl='0',var='0',stem=stem_id)
                possible_endings += definitions.get_possible_endings(infl, entry.pos)
            if match[1].replace('u', 'v').replace('j', 'i') in possible_endings:
                return True
        return False


def get_word_inflections(match,less=False):
    """
    Use a match (from match_word) to look up the possible inflections of a word. Returned as list of plain text
    strings.
    If less is False, information about the word is printed along with the inflection. If
    less is True, only the inflection information and the word header are printed.
    """
    entry = match[2]['entry']
    infl_strings = []
    head = get_dictionary_string(match,header_only=True)
    pos = entry.pos
    if pos in ['PREP','PACK','TACKON','SUFFIX','PREFIX','X']:
        return []
    infl = None
    if pos == 'V':
        infl = definitions.build_inflection(part_of_speech=entry.pos,conj=entry.conj,var=entry.variant,ending=match[1])
    elif pos == 'N':
        infl = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl,var=entry.variant,ending=match[1],gender=entry.gender)
    elif pos in ['ADJ','PRON','NUM']:
        infl = definitions.build_inflection(part_of_speech=entry.pos,decl=entry.decl,var=entry.variant,ending=match[1])
    elif pos in ['ADV','PREP','CONJ','INTERJ']:
        return []
    possible_infls = definitions.get_possible_inflections(infl,pos)
    for minfl in possible_infls:
        if less:
            infl_strings.append(minfl.get_inflection_string(less=less)+'of '+head)
        else:
            infl_strings.append(minfl.get_inflection_string(less=less)+' '+head)
    return infl_strings



def lookup_word(w,full_info=False,match_filter=MatchFilter()):
    """
    Print-only method for user to look up a word
    """
    matches = match_word(w)
    if match_filter.substantives is False:
        matches = match_filter.remove_substantives(matches)
    for match in matches:
        if match_filter.check_dictline_word(match[2]['entry']):
            print(get_dictionary_string(match, full_info))


def lookup_inflections(w,match_filter=MatchFilter()):
    """
    Print-only method for user to look up a word's possible inflections
    """
    matches = match_word(w)
    if match_filter.substantives is False:
        matches = match_filter.remove_substantives(matches)
    infl_strs = set()
    for match in matches:
        if match_filter.check_dictline_word(match[2]['entry']):
            for infl in get_word_inflections(match):
                infl_strs.add(infl)
    for s in infl_strs:
        print(s)

load_dictionary()
definitions.load_inflections()


