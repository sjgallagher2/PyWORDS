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

# Returns a dictionary of stem : ending pairs by starting with no ending and working backwards
def find_endings(w):
    endings = {}
    for i in range(len(w),0,-1):
        wsub = w[i:]
        if wsub in definitions.endings_list:
            endings[w[:i]] = wsub
    return endings
            
def match_word(w):
    matches = []
    endings = find_endings(w)
    for stem,e in endings.items():
        for l in dictline:
            if stem == l['stem1']:
                matches.append(l)
            if stem == l['stem2']:
                matches.append(l)
            if stem == l['stem3']:
                matches.append(l)
            if stem == l['stem4']:
                matches.append(l)

    return matches
 

if __name__ == '__main__':
    load_dictionary()
    words = ['hoc', 'cognomine', 'appellare', 'liceat', 'illam', 'maxime', 'memorabilem', 'seriem', 'qua']
    for w in words:
        ms = match_word(w)
        for m in ms:
            print(m,end=' => ')
            print(m['entry'])


