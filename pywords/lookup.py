# Main methods for looking up words from the dictionary
from dataclasses import dataclass
import pywords.definitions as definitions
from pywords.matchfilter import MatchFilter
import os
import os.path
import bisect  # Search
import csv
import copy  # For deep copies
from typing import List  # For type hints with lists of objects

###############
# GLOBAL DATA #
dictline = []
dictline_ignoreuvij = []
stems1 = []
stems2 = []
stems3 = []
stems4 = []
tackons = []
tackon_suffix_set = set()
###############


@dataclass
class WordMatch:
    """
    WordMatch objects represent a single word lookup match result

    @params
        match_stem  Stem string that was matched
        match_ending    Ending string that was matched
        dl_stem1    Dictline stem 1
        dl_stem2    Dictline stem 2
        dl_stem3    Dictline stem 3
        dl_stem4    Dictline stem 4
        dl_entry    Dictline entry (DictlineBaseEntry subclass)
    """
    match_stem: str
    match_ending: str
    dl_stem1: str
    dl_stem2: str
    dl_stem3: str
    dl_stem4: str
    dl_entry: definitions.DictlineBaseEntry

    def get_stem_ids(self):
        """
        Return a list of IDs as strings representing the dictline stems that match the `match_stem`
        For example, if stem1 and stem4 matched, this method returns ['1','4']
        """
        match_stem = self.match_stem.replace('j','i').replace('u','v')
        stems = [self.dl_stem1.replace('j','i').replace('u','v'),
                 self.dl_stem2.replace('j','i').replace('u','v'),
                 self.dl_stem3.replace('j','i').replace('u','v'),
                 self.dl_stem4.replace('j','i').replace('u','v')]
        stem_ids = [str(s+1) for s,x in enumerate(stems) if x == match_stem]
        return stem_ids

    def get_stem(self,id):
        """
        Return stem<id> for ID string `id`
        """
        if id == '1':
            return self.dl_stem1
        elif id == '2':
            return self.dl_stem2
        elif id == '3':
            return self.dl_stem3
        elif id == '4':
            return self.dl_stem4
        else:
            raise ValueError("get_stem() failed with invalid stem ID string {0}. This method accepts a string number in ['1','2','3','4']".format(id))


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


def load_tackons():
    global tackons,tackon_suffix_set

    # First get column names and index them in case the order changes
    # Get inflects table
    tackon_fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/TACKONS.tsv')
    if not os.path.exists(tackon_fname):
        print("ERROR: Could not find TACKONS.tsv. This is the file that contains word endings like -libet, -cumque, and others. It should have been included in your installation under data/.")
        raise FileNotFoundError
    with open(tackon_fname) as f:
        reader = csv.DictReader(f,delimiter='\t')
        tackon_rows = [row for row in reader]  # tackon_rows is now a list of dictionaries, each dict represents a row
    for tackon in tackon_rows:
        tackons.append(definitions.Tackon(tackon['tackon_suffix'],
                                          tackon['tackon_senses'],
                                          tackon['tackon_wordpos'],
                                          tackon['tackon_worddecl'],
                                          tackon['tackon_wordvariant'],
                                          tackon['tackon_wordgender'],
                                          tackon['tackon_wordplurality'],
                                          tackon['tackon_wordcase'],
                                          tackon['tackon_wordkind']
                                          ))
        tackon_suffix_set.add(tackon['tackon_suffix'])


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
                matches.append(WordMatch(match_stem=raw_w[:split_idx],
                                         match_ending=raw_w[split_idx:],
                                         dl_stem1=entr['stem1'],
                                         dl_stem2=entr['stem2'],
                                         dl_stem3=entr['stem3'],
                                         dl_stem4=entr['stem4'],
                                         dl_entry=entr['entry']
                                         ))

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


def _match_tackon(w,tackon: definitions.Tackon):
    """
    Given a plaintext word `w` and a TACKON object `tackon`, determine if this is a match

    Return list of WordMatch objects that work with this TACKON
    """
    wbase = w[:-len(tackon.suffix)]  # Exclude last <len_suffix> characters
    wmatches = _simple_match(wbase)
    matches_out = []
    if len(wmatches)==0:
        return wmatches
    for wm in wmatches:
        if tackon.matches_dictline_entry(wm.dl_entry):
            wm_infls = definitions.get_possible_inflections(wm.dl_entry,infl_ages=['X'],infl_frequencies=['A'])
            for wmi in wm_infls:
                if tackon.matches_inflection(wmi):
                    matches_out.append(wm)
                    break  # Break inner loop only, we only need to verify at least one inflection works
    return matches_out


def _check_tackons(w):
    """
    Check if the word `w` (with uvij spelling) has a valid TACKON ending
    """
    global tackons,tackon_suffix_set
    # First check for tackon endings
    possible_tackons = set()
    matches = []
    for tack in tackon_suffix_set:
        if w.endswith(tack):
            possible_tackons.add(tack)
    if len(possible_tackons)>0:
        # Get tackon objects
        tack_objs = []
        for tack in possible_tackons:
            for tack_obj in tackons:  # remember that tackons is global
                if tack_obj.suffix == tack:
                    matches += _match_tackon(w, tack_obj)

    return matches


def _prune_pronouns(matches: List[WordMatch]):
    """
    Remove pronoun matches that include "(w/-<tackon>)", e.g. (w/-cumque),
    because these are handled by the tackon methods.
    """
    matches_out = []
    for m in matches:
        if m.dl_entry.pos in ['PRON','PACK']:
            if not m.dl_entry.senses.startswith('(w/-'):
                matches_out.append(m)
        else:
            matches_out.append(m)

    return matches_out


def match_word(w, use_tricks=False):
    """
    Try to match a word, with basic tricks. If use_tricks is used, more in depth matching
    methods are used (not implemented)
    """
    finished=False
    removed_encls = False
    tried_tackons = False
    matches = []

    while not finished:
        matches = _simple_match(w)
        matches = _prune_pronouns(matches)
        if len(matches)>0:
            finished = True
        elif not tried_tackons:
            tackon_matches = _check_tackons(w)
            if len(tackon_matches)>0:
                matches = tackon_matches
                finished=True
            tried_tackons = True  # Pass through for now
        elif not removed_encls:
            w = _remove_enclitics(w)
            removed_encls = True
        else: # Search failed
            finished = True

    return matches


# TODO 
def print_noun_declensions(m: WordMatch):
    """
    Print the declensions of a noun
    m must be in the format [stem,ending,dictline] (same as a match)
    """
    dictline = m.dl_entry


def _get_noun_dictionary_string(m: WordMatch,full_info=False,header_only=False,markdown_fmt=False):
    """
    Generate a dictionary string for a noun
    Includes:
        - principle parts
        - gender
        - kinds and modifiers (singular only, plural only)
        - senses
        - meta data (age, area, geography, frequency, and source)
    """
    # 1. Start with principle parts, same for all variants except undeclined
    princ_parts = ['','']

    if not isinstance(m.dl_entry,definitions.DictlineNounEntry):
        raise ValueError("Match passed to _get_noun_dictionary_string() is not a DictlineNounEntry match.")
    if m.dl_entry.decl == '9':
        princ_parts[0] += m.match_stem
    else:
        # Get nom. and gen. singular stem
        infls = definitions.get_possible_inflections(m.dl_entry,infl_ages=['X'],infl_frequencies=['A'])
        nom_infl = [infl for infl in infls if infl.case=='NOM' and infl.number=='S'][0]
        nom_stem = m.get_stem(nom_infl.stem)
        nom_stem = '' if nom_stem == '-' else nom_stem
        gen_infl = [infl for infl in infls if infl.case=='GEN' and infl.number=='S'][0]
        gen_stem = m.get_stem(gen_infl.stem)
        gen_stem = '' if gen_stem == '-' else gen_stem

        princ_parts[0] = nom_stem + nom_infl.ending_uvij if nom_stem else ''
        princ_parts[1] = gen_stem + gen_infl.ending_uvij if gen_stem else ''

    # 2. Get gender
    # You can use genders or genders_short here
    gender = definitions.genders[m.dl_entry.gender]  # e.g. 'masc.', 'fem.'
    #gender = definitions.genders_short[m.dl_entry.gender]  # e.g. 'm', 'f'

    # 3. Get kind or modifier
    # These include noun_kind='S','M' (singular only, multiple only)
    kind = ''
    variant = ''
    if m.dl_entry.noun_kind == 'S':  # Included here, but not actually used in DICTLINE
        kind = 'sing.'
    elif m.dl_entry.noun_kind == 'M':
        kind = 'pl.'
    # Check if this variant has a string associated with it (e.g. 'Greek')
    varstr = definitions.noun_variants[m.dl_entry.decl][m.dl_entry.variant]
    if varstr != '':
        variant = varstr

    # 4. frequency, age, geography, subject area, source
    frequency = m.dl_entry.get_frequency()
    if m.dl_entry.age != 'X':
        age = m.dl_entry.get_age()
    else:
        age = ''
    if m.dl_entry.geog != 'X':
        geography = m.dl_entry.get_geography()
    else:
        geography = ''
    subject_area = m.dl_entry.get_area()
    source = m.dl_entry.get_source()
    #source = m.dl_entry.get_source_short()  # Abbreviations like 'OLD' and 'L+S', or just author's name

    # 5. senses
    senses = m.dl_entry.senses

    # *************************
    # Put it all together
    # Note: each dictionary element adds a space after itself to prepare for the next element.
    outstr = ''
    if princ_parts[0] and princ_parts[1]:
        outstr += '**'+princ_parts[0]+'**, **'+princ_parts[1]+'** ' if markdown_fmt else princ_parts[0]+', '+princ_parts[1]+' '
    elif princ_parts[0]:  # Indeclinable usually
        outstr += '**'+princ_parts[0]+'** ' if markdown_fmt else princ_parts[0]+' '
    elif princ_parts[1]:  # Indeclinable sometimes only has second stem
        outstr += '**'+princ_parts[1]+'** ' if markdown_fmt else princ_parts[1]+' '

    else:
        raise ValueError("Error when printing noun. No principle parts were found, or only second principle part. Entry: {0}".format(m.dl_entry))
    if header_only:
        return outstr[:-1]  # Return output, leave out extra space

    outstr += '*'+gender if markdown_fmt else gender+' '
    if kind:
        outstr += ' '+kind+'* ' if markdown_fmt else kind+' '
    else:
        outstr += '* ' if markdown_fmt else ''

    # Variant (e.g. 'Greek'), and meta data (e.g. 'Medieval', 'most common')
    if variant or (full_info and (age or geography or frequency or subject_area)):
        # Add relevant geography, age, frequency, and subject area
        outstr += '('
        first = True  # Whether we've included some info already
        if variant:
            outstr += variant
            first = False
        if full_info:
            if frequency:
                outstr += frequency if first else ', '+frequency
                first = False  # This is the first one, next one (if any) needs to add ', '
            if age:
                outstr += age if first else ', '+age
                first = False  # Regardless of whether we were first, this should be False now
            if subject_area:
                outstr += subject_area if first else ', '+subject_area
                first = False  # See previous comment
            if geography:
                outstr += geography if first else ', '+geography
                # `first` is no longer relevant
        outstr += ') '
        # We'll return to `source` after the senses
    outstr += senses
    outstr = outstr.strip()  # Just make sure we're clean. We're breaking with the spacing slightly
    # to avoid adding a double period after the senses.
    if full_info:
        outstr += '. Source: '+source if outstr[-1] != '.' else ' Source: '+source
    return outstr


def get_dictionary_string(m: WordMatch, full_info=False, header_only=False, markdown_fmt=False):
    """
    Convert m into a string in dictionary style
    m must be a WordMatch object (usually returned by match_word())
    If full_info is True, all available information is given. 
    If header_only, only the word header is given (no senses)
    If markdown_fmt, place headwords in bold (**ex**), part of speech in italics (*ex*)

    TODO This whole thing could be rewritten to be less hacky
    """
    dictstr = ''

    entry = m.dl_entry
    # For reference:
    #stem1 = dictline['stem1']
    #stem2 = dictline['stem2']
    #stem3 = dictline['stem2']
    #stem4 = dictline['stem2']
    if entry.pos == 'N':
        dictstr = _get_noun_dictionary_string(m,full_info,header_only,markdown_fmt)

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
            dictstr += m.get_stem(stem1)+end1
            dictstr += ', '
            dictstr += m.get_stem(stem2)+end2
            if m.dl_stem3 != '-':
                dictstr += ', '
                if entry.verb_kind == 'IMPERS':
                    dictstr += m.dl_stem3+'it'
                else:
                    dictstr += m.dl_stem3+'i'
            if m.dl_stem4 != '-':
                dictstr += ', '
                if entry.verb_kind == 'IMPERS':
                    dictstr += m.dl_stem4+'um est'
                else:
                    dictstr += m.dl_stem4+'us'
                if entry.verb_kind in ['DEP','SEMIDEP']:
                    dictstr += ' sum'
            if markdown_fmt:
                dictstr += '**'
            dictstr += ' '

        else:
            if markdown_fmt:
                dictstr += '**'
            dictstr += m.match_stem+m.match_ending
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
        # 4th stem is present, and therefore acts as the superlative (or comp.)
        # I've updated DICTLINE.GEN so that COMP and SUPER adjectives of declension 0 0 are
        # in the same stem slot
        #ainfl = definitions.AdjectiveInfl(decl=entry.decl,
        #        number='S',case='NOM')
        #if entry.pos == 'ADJ':
        #    if entry.comparison != 'POS':
        #        ainfl.comparison = entry.comparison
        #infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'])
        #matches = [a for a in definitions.inflections[entry.pos] if ainfl.matches(a)]
        #matches = [ma for ma in matches if infl_filt.check_inflection(ma,'ADJ')]
        matches = definitions.get_possible_inflections(entry,infl_ages=['X'],infl_frequencies=['A'])
        matches = [m for m in matches if m.number=='S' and m.case=='NOM']
        if entry.pos == 'ADJ':
            matches = [m for m in matches if m.comparison == 'POS']
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
            stem1 = m.dl_stem1
            stem2 = m.dl_stem2
            stem3 = m.dl_stem3
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
                dictstr += '**'+m.match_stem+m.match_ending+'** '
            else:
                dictstr += m.match_stem+m.match_ending+' '
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
    elif entry.pos in ['PRON','PACK']:
        infl_filt = MatchFilter(ages=['X'],frequencies=['X','A'],variants=[entry.variant,'0'])
        pinfl = definitions.PronounInfl(decl=entry.decl,number='S')
        matches = [p for p in definitions.inflections['PRON'] if pinfl.matches(p)]
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

            nom_stem = m.get_stem(stem1)
            if stem2:
                gen_stem = m.get_stem(stem2)
                dictstr = nom_stem+end1+', '+gen_stem+end2+' '
            else:
                dictstr = nom_stem+end1+' '

            if full_info:
                # add age, area, geography, frequency
                dictstr += '('+definitions.dict_frequencies[entry.freq]+', ' + \
                        definitions.ages[entry.age]+'. '
                if entry.area != 'X':
                    dictstr += definitions.areas[entry.area]+'. '
                if entry.geog != 'X':
                    dictstr += definitions.geographies[entry.geog]+'). '
                else:
                    dictstr = dictstr.strip(' .')+'). '  # Avoid awkward spaces
            if not header_only:
                dictstr += ''.join(entry.senses)
            if full_info:
                dictstr += 'Source: '+definitions.source_types[entry.src]+'. '

    elif entry.pos == 'CONJ':
        if markdown_fmt:
            dictstr = '**'+m.dl_stem1 + '** *conj* '
        else:
            dictstr = m.dl_stem1 + ' conj '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'ADV':
        # TODO Add comparison
        if markdown_fmt:
            dictstr = '**'+m.dl_stem1+'** *adv* '
        else:
            dictstr = m.dl_stem1 + ' adv '
        if not header_only:
            dictstr += ''.join(entry.senses)
    elif entry.pos == 'NUM':
        # TODO Placeholder until I get the chance to properly format
        # Numbers share declension/variant codes with adjectives
        if markdown_fmt:
            dictstr = '**'+m.dl_stem1+'** *num* '
        else:
            dictstr = m.dl_stem1 + ' num '
        if not header_only:
            dictstr += ''.join(entry.senses)

    elif entry.pos == 'PREP':
        # TODO Placeholder until I get the chance to properly format
        if markdown_fmt:
            dictstr = '**'+m.dl_stem1 + '** *prep* '
        else:
            dictstr = m.dl_stem1 + ' prep '
        if not header_only:
            dictstr += ''.join(entry.senses)
    return dictstr.replace('  ',' ').strip(' ')


def is_possible_ending(m: WordMatch):
    """
    Check whether a match is possible
    match should be returned from e.g. _simple_match and should be in uvij format

    This is one of the key functions in the lookup process, narrowing the list of
    stem matches to those that are actually possible. It needs to account for different
    kinds (verb kinds like deponent, impersonal; noun kinds like singular or plural
    only) but doesn't need to manage SUPINE and VPAR inflections (handled by
    definitions.get_possible_endings(infl,part_of_speech)

    Note: These should be cached
    """
    match_stem = m.match_stem.replace('j', 'i').replace('u', 'v')
    stem_ids = m.get_stem_ids()
    possible_endings = set()
    entry = m.dl_entry
    # Get part of speech, handle internal-only parts for now
    pos = entry.pos
    if pos in ['ADV','PREP','CONJ','INTERJ']:
        if m.match_ending == '':
            return True
        else:
            return False
    elif pos == 'X':  # Not used in DICTLINE, but just in case
        return True
    elif pos == 'PACK':  # Treated like PRON
        pron_entry = copy.deepcopy(entry)
        pron_entry.pos = 'PRON'
        infls = definitions.get_possible_inflections(pron_entry,infl_ages=['X'],infl_frequencies=['A'])
    else:
        infls = definitions.get_possible_inflections(entry, infl_ages=['X'], infl_frequencies=['A'])
    for infl in infls:
        # Make list of endings
        ###### SPECIAL CASE ######
        # V 3 1 with -c stem can have empty ending but otherwise cannot

        # Details: There's an inflection for V 3 1 imperative which only applies to stems
        # which end in 'c' (inflects id 744). Can this be a new V 3 x variant? Otherwise
        # we need to process this manually which is ugly
        # Original WORDS might have organized stems by endings but I don't understand that
        # codebase so I'm not sure how this gets handled
        if entry.pos == 'V':
            if entry.conj == '3' and entry.variant == '1':
                if infl.stem == '2' and m.match_ending == '':
                    if m.dl_stem3[-1] != 'c':
                        continue  # Don't bother with this inflection, go to next
        ##########################
        # An ending is valid if our stem (all stems in `stem_ids`) is the stem id of an inflection
        if infl.stem in stem_ids:
            possible_endings.add(infl.ending_vi)

    if m.match_ending.replace('u', 'v').replace('j', 'i') in possible_endings:
        return True
    return False


def get_word_inflections(m: WordMatch, less=False):
    """
    Use a match (from match_word) to look up the possible inflections of a word. Returned as list of plain text
    strings.
    If less is False, information about the word is printed along with the inflection. If
    less is True, only the inflection information and the word header are printed.
    """
    entry = m.dl_entry
    infl_strings = []
    head = get_dictionary_string(m, header_only=True)
    pos = entry.pos
    if pos in ['SUFFIX','PREFIX','X']:
        return []  #TODO ?
    possible_infls = definitions.get_possible_inflections(entry,infl_ages=['X'],infl_frequencies=['A'])
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
        if match_filter.check_dictline_word(match.dl_entry):
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
        if match_filter.check_dictline_word(match.dl_entry):
            for infl in get_word_inflections(match):
                infl_strs.add(infl)
    for s in infl_strs:
        print(s)


# TODO Should this go somewhere else?
load_dictionary()
definitions.load_inflections()
load_tackons()

