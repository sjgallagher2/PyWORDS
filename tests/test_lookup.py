import pywords.lookup as lookup
import pywords.utils as pwutils
from pywords.matchfilter import MatchFilter

filt = MatchFilter(substantives=True)

# superlative adjective
lookup.lookup_word('maximum')
lookup.lookup_word('prior')
lookup.lookup_word('unus')
#lookup.lookup_word('vnvs')
lookup.lookup_word('paret')
lookup.lookup_word('imperat')
lookup.lookup_word('sumit')
lookup.lookup_inflections('maximum')
lookup.lookup_inflections('prior')
lookup.lookup_inflections('unus')
print("Should be the same:")
lookup.lookup_inflections('vnvs')
print("Moving on..")
lookup.lookup_inflections('paret')
lookup.lookup_inflections('imperat')
lookup.lookup_inflections('sumit')

# Need to test a word from each declension-variant and conjugation-variant pair, and combinations
# of e.g. comparison, verb type, etc, for all parts of speech
# Need to test i/j and u/v interchanges

# Whitaker provides a number of examples, see `docs/notes.txt`


defns,missed = pwutils.get_vocab_list('sumit summat',vocab_list='llpsi')
print(defns)

