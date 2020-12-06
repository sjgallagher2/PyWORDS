# PYWORDS

### A Python Toolkit for Latin, Based on Whitaker's WORDS Program

As a student of new Latin who is learning from classical Latin books like Wheelock's, I have been dreaming of a way to automatically process documents, lookup obscure words, collect specific words (mathematical, scientific), and generate vocab lists from arbitrarily large uploaded texts. 

Fortunately, William Whitaker developed a fairly extensive dictionary written in a somewhat human-readable raw text format, and he provided an accompanying program written in Ada with very strong functionality. Several projects have aimed to bring WORDS to the Python language, but to date their attempts have been limited to word lookup alone. And so, I've decided to part with the existing work, and to develop *yet another* Python port of the WORDS program, to my own needs. 

## Current Functionality

The dictionary builder is functional, and it works much faster than previous versions. Running the complete text of Euler's *Institutionum Calculi Integralis Vol. 1* through without filtering takes about 30 seconds. With filtering, the time is reduced, sometimes to as little as <1 second. 

To get started:

```python
import PYWORDS.lookup as lookup
from PYWORDS.matchfilter import MatchFilter
```

There's a lot of functionality available, but the most direct methods are:

* `lookup.match_word(w)`
  * Returns a list of matched words in the format `[stem,ending,DictlineEntry]`
  * Used for finding any entries that match a plaintext latin word
* `lookup.get_dictionary_string(m, full_info=False)`
  * Converts a match (from match_word) into a string, dictionary style. E.g. `series, seriei fem row, series, secession, chain, train, sequence, order (gen lacking, no pl.);`
  * If full_info is True, all known information (out of: relative frequency, subject area, time period, geography) is additionally printed
  * Used for converting matches into user-friendly text
* `lookup.get_vocab_list(text, filt=MatchFilter())`
  * Take an arbitrary string (newlines allowed), eliminate unlikely words and punctuation, match each word, and return the dictionary entry
  * MatchFilter is a simple class of lists representing the declension, variant, frequency, conjugation, case, etc. By using the MatchFilter.check_dictline_word(DictlineEntry) method, filled in items will be matched exactly. This is a very powerful feature, and is very simple to use.
  * Used for converting large amounts of (preferably preprocessed) text into a dictionary, and a list of missed words.
* `lookup.get_word_inflections(match,less=False)`
  * Use a match (from `match_word`) to look up the possible inflections of a word. Returned as list of plain text.
  * By default, inflections are printed in a form similar to `vocative singular neuter of third declension positive adjective cognominis -is -e`
  * If `less`is True, the verb/noun/adj/etc information is not shown, as with `vocative singular neuter of cognominis -is -e`
  * There may be some formatting issues, that's just me being lazy
* find_example_sentences(text,word,word_filt,infl_filt)
  * Search `text` for uses of the word `word` by breaking sentences up at periods
  * This is one of my favorite methods, and with the filtering, it is a very powerful learning tool
  * With some forms a Latin student may not be familiar with the grammar, e.g subjunctive or supine forms; the get_word_inflections() method can help here. 
  * This method is also an example of a quick and easy application of the infrastructure; many more possibilities are out there!

There are all sorts of methods in `definitions.py`, and much infrastructure, which make the raw dictionary elements highly accessible. Implementing a function to e.g. write out noun declensions or verb conjugations would be straightforward, and running statistics and reviewing the dictionary and inflection entries is greatly simplified. 

Some examples:

#### Looking up a word

```python
word = 'aliqua'
matches = lookup.match_word(word)
for match in matches:
    print(lookup.get_dictionary_string(match,full_info=True))
```

Returns:

```
aliqua adv somehow, in some way or another, by some means or other; to some extent;
aliqu, alicujus (very frequent, common/unknown). Source: Oxford Latin Dictionary, 1982 (OLD). anyone/anybody/anything; someone; some/few; some (particular) thing;
aliqu, alicujus (very frequent, common/unknown). Source: Oxford Latin Dictionary, 1982 (OLD). some; any;
a few; a particular/certain ~; some other; about/like (NUM);                          
aliqui, zzzjus (very frequent, common/unknown). Source: Oxford Latin Dictionary, 1982 (OLD). some; any; a few; a particular/certain ~; some other; about/like (NUM);
...
```

#### Building a dictionary with a filter

```python
filt = MatchFilter(ages=['F','G']) # Only medieval and scholastic (11th-18th centuries)
s = '''
Hoc cogmine appellare liceat illam maxime memorabilem seriem, qua vir acutissimi ingenii Lambertus radices aequationum trinomialium primus exprimere docuit in 
'''
lookup.get_vocab_list(s,filt)
```

This returns a list of filtered dictionary entries compiled from the words present in the string `s`. Using a MatchFilter, only words which were coined or most prominent in the 11th-18th centuries are included. 

For a complete listing of available filter options, see `PYWORDS/matchfilter.py`  and `PYWORDS/definitions.py`. 

### Status

So far, words with enclitics (-que, -ne, etc) and prefixes (ad-, ab-, etc) are often missed because the match doesn't try removing them. Whitaker's original program had a large number of 'tricks' which would be great to add, and not too difficult. Mostly it's a matter of checking if the start and/or end of the word contains prefixes or suffixes or enclitics, then removing them, and trying the search again. 

It is often useful when looking up adjectives to remove substantive forms (noun forms of adjectives) which can add 2-3 entries. For this, the MatchFilter class implements a method `remove_substantives()` which will (rather aggressively) seek out any nouns with identical stems to adjectives, and remove them from the matched words list. Use with care.

Some parts of speech (numeral, preposition, PACK, TACKON, the latter two being used only internally by Whitaker's original WORDS program) are not completely implemented in some places, because they are less significant. When checking for valid endings for verbs, the verb participle endings have not yet been included. The original program's UNIQUES is not used. The English-to-Latin translation facility is unlikely to be implemented.

Note that this program manages the process of parsing Whitaker's dictionary, not building new entries for it. It's fairly simple, once you get familiar with it, to add entries, but this program (as it stands) won't help you. 

