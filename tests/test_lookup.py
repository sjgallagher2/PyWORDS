import pywords.lookup as words
from pywords.matchfilter import MatchFilter

filt = MatchFilter(substantives=True)

# superlative adjective
words.lookup_word('maximum')
words.lookup_word('prior')
words.lookup_word('unus')
#words.lookup_word('vnvs')
words.lookup_word('paret')
words.lookup_word('imperat')  # TODO Returns noun, which is incorrect
words.lookup_word('sumit')
words.lookup_inflections('maximum')
words.lookup_inflections('prior')
words.lookup_inflections('unus')
print("Should be the same:")
words.lookup_inflections('vnvs')
print("Moving on..")
words.lookup_inflections('paret')
words.lookup_inflections('imperat')
words.lookup_inflections('sumit')

# Need to test a word from each declension-variant and conjugation-variant pair, and combinations
# of e.g. comparison, verb type, etc, for all parts of speech
# Need to test i/j and u/v interchanges

# Whitaker provides a number of examples, see `docs/notes.txt`






