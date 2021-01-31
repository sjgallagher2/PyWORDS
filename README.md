# PYWORDS

### A Python Toolkit for Latin, Based on Whitaker's WORDS Program

As a student of new Latin who is learning from classical Latin books like Wheelock's, I have been dreaming of a way to automatically process documents, lookup obscure words, collect specific words (mathematical, scientific), and generate vocab lists from arbitrarily large uploaded texts. 

Fortunately, William Whitaker developed a fairly extensive dictionary written in a somewhat human-readable raw text format, and he provided an accompanying program written in Ada with very strong functionality. Several projects have aimed to bring WORDS to the Python language, but to date their attempts have been limited to word lookup alone. And so, I've decided to part with the existing work, and to develop *yet another* Python port of the WORDS program, to my own needs. 

The original Whitaker's WORDS program is available online in several places, including University of Notre Dame ([here](http://archives.nd.edu/words.html)), and mk270's Github repository ([repo](https://github.com/mk270/whitakers-words), [website](https://mk270.github.io/whitakers-words/)). This program also borrows (minimally) from other Python ports of WORDS, such as this ArchimedesDigital [open_words program](https://github.com/ArchimedesDigital/open_words), and this repository called [whitakers_words](https://github.com/blagae/whitakers_words) from blagae. 

To learn more about the original WORDS program, I highly recommend reading Whitaker's own original description, available in this repository under `archive/`, which is reproduced from last version of the WORDS website stored in the WaybackMachine. 



## Current Functionality

The dictionary builder is functional, and it works much faster than previous versions. Running the complete text of Euler's *Institutionum Calculi Integralis Vol. 1* through without filtering takes about 10 seconds. With filtering, the time is reduced, sometimes to as little as <1 second. 

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
* `lookup.find_example_sentences(text,word,word_filt,infl_filt)`
  * Search `text` for uses of the word `word` by breaking sentences up at periods
  * This is one of my favorite methods, and with the filtering, it is a very powerful learning tool
  * With some forms a Latin student may not be familiar with the grammar, e.g subjunctive or supine forms; the get_word_inflections() method can help here. 
  * This method is also an example of a quick and easy application of the infrastructure; many more possibilities are out there!

There are all sorts of methods in `definitions.py`, and much infrastructure, which make the raw dictionary elements highly accessible. Implementing a function to e.g. write out noun declensions or verb conjugations would be straightforward, and running statistics and reviewing the dictionary and inflection entries is greatly simplified. 

### Examples

#### Looking up a word

```python
word = 'aliqua'
matches = lookup.match_word(word)
for match in matches:
    print(lookup.get_dictionary_string(match,full_info=True))
```

Output:

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
(vocab,missed_words) = lookup.get_vocab_list(s,filt)
```

This returns a list of filtered dictionary entries compiled from the words present in the string `s`, as well as a list of missed words. Using a MatchFilter, only words which were coined or most prominent in the 11th-18th centuries are included. 

For a complete listing of available filter options, see `PYWORDS/matchfilter.py`  and `PYWORDS/definitions.py`. 

#### Find verbs used in a text

```python
from example_text import text
from PYWORDS.matchfilter import MatchFilter
# Match only verbs by filtering
(vocab,missed) = lookup.get_vocab_list(s,MatchFilter(parts_of_speech=['V'])) 
for v in vocab:
    print(v)
```

Output:

```
abeo, abire vi depart, go away; go off, go forth; pass away, die, disappear; be changed;
accipio, accipere vt take, grasp, receive, accept, undertake; admit, let in, hear, learn; obey;
adeo, adire vt approach; attack; visit, address; undertake; take possession (inheritance);
anteo, antire vt go before, go ahead, precede; surpass; anticipate; prevent; (anteeo drop e);
appello, appellare vt call (upon); address; dun; solicit; appeal (to); bring to court; accuse; name;
appello, appellere vt apply, to put in practice;
appello, appellere vt drive to, move up, bring along, force towards; put ashore at, land (ship);
assigno, assignare vt assign, distribute, allot; award, bestow (rank/honors); impute; affix seal;
...
```



#### Printing inflections of a word

```python
for match in lookup.match_word('casus'): # Match possible words
    print(lookup.get_dictionary_string(match))  # Start with the definition of the word
    for i in lookup.get_word_inflections(match,less=True):
        print(i) # Then print each inflection's meaning
```

Output:

```
casus, casus masc fall, overthrow; chance/fortune; accident, emergency, calamity, plight; fate;
vocative singular of casus, casus
vocative plural of casus, casus
nominative plural of casus, casus
genitive singular of casus, casus
nominative singular of casus, casus
nominative singular of casus, casus
accusative plural of casus, casus
genitive singular of casus, casus
casus, casus masc grammatical case; termination/ending (of words);
vocative singular of casus, casus
...
```



#### Finding example sentences from text

Assume we have a file `example_text.py` which defines a string `text` that contains a large amount of Latin text from a book or article or paper. To find example sentences of a word *series* we can use the `find_example_sentences()` method. This method is more of a demonstration of possible user friendly methods.

```python
from example_text import text # for example_text.py defines a string called 'text'
word = 'series'  # Desired word
for sentence in lookup.find_example_sentences(text,word):
    print(sentence)
```

Output:

```
Which word did you mean? 
a) seria, seriae fem large earthenware jar;
b) series, seriei fem row, series, secession, chain, train, sequence, order (gen lacking, no pl.);
WORD: 
```

This is the disambiguation prompt. Note that you can give `word` as any inflected form, and specify which definition makes the most sense. Entering 'b', the output is:

```
...
WORD: b

Finding example sentences of word: series, seriei fem row, series, secession, chain, train, sequence, order (gen lacking, no pl.);
Found 10 sentences.
Hoc cognomine appellare liceat illam maxime memorabilem seriem, qua vir acutissimi ingenii Lambertus  radices aequationum trinomialium primus exprimere docuit in.                                               
Haec autem series, si eius  elementa parumper immutentur, sequenti forma repraesentari potest: ubi cum illa aequatio plures habere possit radices, pro earum maximam vel minimam accipi oportet, prouti circumstantiae postulauerint.
...
```



### Utilities

The `PYWORDS.util`  module contains a few useful and somewhat powerful utilities for managing missed words. Current methods that have been implemented:

* `format_dictline_entry()`
  * Walks the user through the process of building a DICTLINE entry
  * The final output is a loosely formatted that needs spacing to match the other DICTLINE entries, and it doesn't take senses because they may need to be broken up over multiple lines and without exact spacing that's not available to the method.
  * Performs some simple checks, forces case (upper or lower) as necessary
* `get_missing_word_report(words, output_file_name)`
  * Takes a list of words not in the dictionary, `words`,  and processes them, saving the results (and overwriting) to `output_file_name`
  * Performs "winnowing" of words unlikely to be Latin:
    * Trashes words less than 4 letters long
    * Trashes words without vowels
    * Trashes words with only 'IVXLCDM' (numerals)
    * Trashes words that are not ASCII
    * Trashed words are put in the end of the file for review
  * Checks all words for valid Latin endings, puts such words first in the file ("good" words)
  * Keeps all good words and "tentative" (no Latin ending but not trash) words
  * Performs stem analysis:
    * Groups all words by stem
    * Uses all endings associated with a given stem, and checks possible inflections and the associated part of speech, conjugation/declension, and variant
    * Tallies up the number of possible inflections for each case and lists them to the user

The output of `get_missing_word_report()` looks like this:

```
Original number of words: 4146
Number of words after winnowing: 2242
Number of words with valid Latin endings: 1199
=====================================================
GOOD WORD LIST: 
---------------------
abierit
abierunt
[...]
zeteticis
zeteticorum
=====================================================
TENTATIVE WORD LIST (Superset): 
---------------------
aberrantem
abierit
[...]
zeteticis
zeteticorum
=====================================================
POSSIBLE WORDS WITH STEMS: 
---------------------
STEM: adiic
	  -> adiicere
	  -> adiici
	  -> adiicimus
DECLENSION ANALYSIS:
N 2 0		3
N 2 1		1
[...]
V 7 1		1
V 7 3		1
STEM: adiici
	  -> adiiciamus
	  -> adiiciendo
	  -> adiiciendum
	  -> adiicimus
DECLENSION ANALYSIS:
ADJ 0 0		1
V 1 1		1
V 3 0		9
V 6 1		2
[...]
=====================================================
TRASH BIN: 
---------------------
académie
adscitâ
aisément
alternè
année
asinφ
aαbβcγ
[...]
```

Using the stem **adiici** as an example, the output of the declension/stem analysis is:

```
STEM: adiici
	  -> adiiciamus
	  -> adiiciendo
	  -> adiiciendum
	  -> adiicimus
DECLENSION ANALYSIS:
ADJ 0 0		1
V 1 1		1
V 3 0		9
V 6 1		2
```

This shows:

* The stem (without any ending)
* All instances found with this stem and valid latin endings
* Total number of times an ending returned a valid inflection in the given part of speech's declensions/conjugations and variants
  * `ADJ 0 0     1`  means of the four instances combined, there was only one with possible inflections in the `ADJ 0 0`  part of speech/declension/variant
  * This provides a semi-quantitative view of the possible forms this stem would fit. Thus the score of 9 for `V 3 0` compared to the very low scores in all other forms strongly implies this is third conjugation verb



### Status

Whitaker's original program had a large number of 'tricks' which would be great to add, and not too difficult. Mostly it's a matter of checking of checking for letter swaps (i and j, u and v), trying suffixes and prefixes then removing or adding them, and so on. 

It is often useful when looking up adjectives to remove substantive forms (noun forms of adjectives) which can add 2-3 entries. For this, the MatchFilter class implements a method `remove_substantives()` which will (rather aggressively) seek out any nouns with identical stems to adjectives, and remove them from the matched words list. Use with care.

Some parts of speech (numeral, preposition, PACK, TACKON, the latter two being used only internally by Whitaker's original WORDS program) are not completely implemented in some places, because they are less significant. The original program's UNIQUES is not used. The English-to-Latin translation facility is unlikely to be implemented.

### Future Work

I would very much like to add a graphical front-end to make PyWORDS more user friendly. The fact is, many people familiar with Latin may be unfamiliar with Python. The ideal would be a web application which provides more user-friendly functionality, in addition to this more powerful programming/interpreted interface. Until then, I hope the examples above will be enough for people to make use of the tools even with only modest exposure to Python. 