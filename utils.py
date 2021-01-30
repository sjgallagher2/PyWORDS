'''
Clean missing word lists and analyze stems
'''

import PYWORDS.lookup as lookup
import PYWORDS.definitions as definitions

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
# TODO
#  Go through matching stems, find possible inflections, cross check to find likely word declension/conjugation

            
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
    '''
    Write a text file `output_file_name` from a word list `words` containing
    filtering and analysis of the missed words.
    '''
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
                        var = infl.var
                        s = 'N '+decl+' '+var
                        if s in noun_inflections_count.keys():
                            noun_inflections_count[s] += 1
                    
                for inst_adj_infls in possible_adj_infls:
                    # Check each possible inflection of a given instance against the other inflections
                    for infl in inst_adj_infls:
                        decl = infl.decl
                        var = infl.var
                        s = 'ADJ '+decl+' '+var
                        if s in adj_inflections_count.keys():
                            adj_inflections_count[s] += 1
                for inst_v_infls in possible_v_infls:
                    # Check each possible inflection of a given instance against the other inflections
                    for infl in inst_v_infls:
                        conj = infl.conj
                        var = infl.var
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
