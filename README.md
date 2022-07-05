# PyWORDS

### A Python Toolkit for Latin, Based on Whitaker's WORDS Program

As a student of New Latin who is learning from classical Latin books like Wheelock's, I have been dreaming of a way to automatically process documents, lookup obscure words, collect specific words (mathematical, scientific), and generate vocab lists from arbitrarily large uploaded texts. 

Fortunately, William Whitaker developed a fairly extensive dictionary written in a somewhat human-readable raw text format, and he provided an accompanying program written in Ada with very strong functionality. Several projects have aimed to bring WORDS to the Python language, but to date their attempts have been limited to word lookup alone. And so, I've decided to part with the existing work, and to develop *yet another* Python port of the WORDS program, to my own needs. 

The original Whitaker's WORDS program is available online in several places, including University of Notre Dame ([here](http://archives.nd.edu/words.html)), and mk270's Github repository ([repo](https://github.com/mk270/whitakers-words), [website](https://mk270.github.io/whitakers-words/)). This program also borrows (minimally) from other Python ports of WORDS, such as this ArchimedesDigital [open_words program](https://github.com/ArchimedesDigital/open_words), and this repository called [whitakers_words](https://github.com/blagae/whitakers_words) from blagae. 

To learn more about the original WORDS program, I highly recommend reading Whitaker's own original description, available using [the Wayback Machine here](https://web.archive.org/web/20111105213921/http://users.erols.com/whitaker/wordsdoc.htm). 



### Contributing

Interested in contributing? Things are moving fast at the moment, I'm making large changes I try to bring the project into better working order. Check the developer's documentation under `docs/`, and the source, which is commented a fair bit. Please reach out and keep me informed if you plan to work on PyWORDS, so we can coordinate changes. I'm not a full time programmer, so my methods are very hacky. 



### Status

The dictionary no longer distinguishes U and V, or I and J, so "adiuvat", "adjuvat", and "adjvvat" will all return the same results. I had toyed with the idea of using a SQLite database, but opted for a text file format (tab separated value, `.tsv`) instead, which I generate from a database I keep outside the repository. A lot of refactoring has gone on, so if you're using PyWORDS and haven't pulled the more recent updates, I'd really suggest it. 

Whitaker's original program had a large number of 'tricks' which would be great to add, and not too difficult. Mostly it's a matter of checking of checking for letter swaps, trying suffixes and prefixes then removing or adding them, and so on. 

It is often useful when looking up adjectives to remove substantive forms (noun forms of adjectives) which can add 2-3 entries. For this, the MatchFilter class implements a method `remove_substantives()` which will (rather aggressively) seek out any nouns with identical stems to adjectives, and remove them from the matched words list. Use with care.

Some parts of speech (preposition, PACK, TACKON, the latter two being used only internally by Whitaker's original WORDS program) might not be completely implemented in some places. The original program's UNIQUES is not used yet. The English-to-Latin translation facility is not yet implemented, but I might reconsider this in the future. 

### Future Work

I would very much like to add a graphical front-end to make PyWORDS more user friendly. The fact is, many people familiar with Latin may be unfamiliar with Python. The ideal would be a web application which provides more user-friendly functionality, in addition to this more powerful programming/interpreted interface. Until then, I hope the examples above will be enough for people to make use of the tools even with only modest exposure to Python. 





## Getting Started

The `pywords` Python module can be installed (assuming you have `pip`) by cloning the repository or downloading it through Github, then running `pip install .` from within the root directory to make `pywords` available anywhere. 

### Install on Windows

To install PyWORDS on Windows, first make sure you have a Python 3 installation. If you're a Latinist with minimal programming experience, you will find countless examples online about how to install Python, for example [here](https://realpython.com/installing-python/). If you're unfamiliar with the command prompt (`cmd.exe`), now might be a good time to look into the basics. Personally, I would recommend getting away from the ugly `cmd.exe` that Windows uses by default, in favor of something like [cmder](https://cmder.net/). This is like a friendlier front-end for the command prompt, and it comes with useful software packages like `git` installed. For Python, you need a *Python interpreter*, `python.exe`, and you call this executable in order to run your script. It's important to note that you can have multiple `python.exe` programs on your machine, which can either be helpful or a headache. Python itself can be installed several ways, such as the [official releases](https://www.python.org/downloads/), or through an IDE or environment manager.

Something like [Anaconda](https://www.anaconda.com/) will *not* provide you with a development environment (like an IDE would), but it *will* manage your Python interpreters (each one with its own packages, collectively called a Python environment), which is why it's so popular. For actual bare-bones programming, you can get by just fine using the terminal and Notepad, but an IDE (Integrated Development Environment) will give you everything in one place; you need to point it to your desired Python interpreter usually, which can be built-in or can be obtained by installing Python directly, or installing Python through something like Anaconda. Some IDEs, like the popular [PyCharm](https://www.jetbrains.com/pycharm/), work a little like an IDE and an environment manager, so they'll also give you the option of installing a Python interpreter. 

What route should you go? I would recommend the following steps. 

1. Install [cmder](https://cmder.net/) with `git-for-windows`
2. Install [PyCharm](https://www.jetbrains.com/pycharm/) and make sure it includes Python 3 (e.g. Python 3.9 or Python 3.10)
3. Follow the instructions [here](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#packages-tool-window) to install a Python package from a repository; the repository is PyWORDS: https://github.com/sjgallagher2/PyWORDS

Now you've got PyWORDS installed, so within PyCharm you can make a new file called `test_pywords.py` and try running the line `import pywords`. If it works, installation is complete. 

### Install on Linux

If you're running Linux, you can clone the repository and `pip install .` to install it, or go through your preferred IDE or environment manager to install from a repository or local directory. 

Example steps:

1. `git clone https://github.com/sjgallagher2/PyWORDS`
2. `cd PyWORDS`
3. `pip install .`





## Current Functionality

The dictionary builder is functional, and it works much faster than previous versions. Running the complete text of Euler's *Institutionum Calculi Integralis Vol. 1* through without filtering takes about 10 seconds. With filtering, the time is reduced, sometimes to as little as <1 second. 

To get started:

```python
# lookup is the main module
import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias

# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter

# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils
```

There's a lot of functionality available, but the most direct methods are:

* High level
  * `lookup.lookup_word(w)`
    * Print dictionary entries for words in the dictionary matching the given word `w`
    * Analogous to a typical single-word Latin dictionary lookup
  * `pwutils.find_example_sentences(text,word,word_filt,infl_filt)`
    * Search `text` for uses of the word `word` by breaking sentences up at periods
    * This is one of my favorite methods, and with the filtering, it is a very powerful learning tool
    * With some forms a Latin student may not be familiar with the grammar, e.g subjunctive or supine forms; the get_word_inflections() method can help here. 
    * This method is also an example of a quick and easy application of the infrastructure; many more possibilities are out there!
  * `pwutils.get_vocab_list(text, filt=MatchFilter())`
    * Take an arbitrary string (newlines allowed), eliminate unlikely words and punctuation, match each word, and return the dictionary entry
    * MatchFilter is a simple class of lists representing the declension, variant, frequency, conjugation, case, etc. By using the MatchFilter.check_dictline_word(DictlineEntry) method, filled in items will be matched exactly. This is a very powerful feature, and is very simple to use.
    * Used for converting large amounts of (preferably preprocessed) text into a dictionary, and a list of missed words.
  * `pwutils.format_dictline_entry()`
    * Interactive entry-builder for making new `DICTLINE` entries. Soon to be obsoleted as I move away from the text-based `DICTLINE.GEN`, but useful for updating that file in Whitaker's original format.
  * `pwutils.get_glossary_from_file(filename)`
    * Take a text file called `filename` and generated a glossary/dictionary as a markdown document
    * This is one of my most common uses for PyWORDS at the moment, the output markdown file can be converted into a Word or LibreOffice Writer document and compressed into a two-column 8-pt font format for a handy staple-on glossary to Latin texts
* Lower level
  * `lookup.match_word(w)`
    * Returns a list of matched words in the format `[stem,ending,{DictlineEntry dict}]` where the dictionary has keys `stem1`, `stem2`, `stem3`, `stem4`, and `entry` (an entry is considered separately from the stems, and contains the information about the word like senses, part of speech, etc.)
    * Used for finding any entries that match a plaintext latin word
  * `lookup.get_dictionary_string(m, full_info=False)`
    * Converts a match (from match_word) into a string, dictionary style. E.g. `series, seriei fem row, series, secession, chain, train, sequence, order (gen lacking, no pl.);`
    * If `full_info` is `True`, all known information (out of: relative frequency, subject area, time period, geography) is additionally printed
    * Used for converting matches into user-friendly text
  * `lookup.get_word_inflections(match,less=False)`
    * Use a match (from `match_word`) to look up the possible inflections of a word. Returned as list of plain text.
    * By default, inflections are printed in a form similar to `vocative singular neuter of third declension positive adjective cognominis -is -e`
    * If `less`is True, the verb/noun/adj/etc information is not shown, as with `vocative singular neuter of cognominis -is -e`
    * There may be some formatting issues, that's just me being lazy

There are other low-level methods in `definitions.py`, and much infrastructure, which make the raw dictionary elements highly accessible. Implementing a function to e.g. write out noun declensions or verb conjugations would be straightforward, and running statistics and reviewing the dictionary and inflection entries is greatly simplified. 

### Examples

#### Looking up a word

```python
word = 'aliqua'
# High level
lookup.lookup_word(word)  # Print matching words

# Lower level
matches = lookup.match_word(word)
for match in matches:
    print(lookup.get_dictionary_string(match,full_info=True))
```

Output (either option):

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



#### Generate a Markdown (Or MS Word) Style Glossary From a File

Suppose the file `loremipsum.txt` contains a large amount of Latin text, and we would like to generate a glossary and save it to Markdown format, or generate a Word document, with proper bold and italics in the dictionary definitions. This can be done by passing the `markdown_fmt=True` parameter to `lookup.get_vocab_list()`. Saving the file to Markdown format allows us to use something like Pandocs to convert the Markdown to any number of other formats. This has been automated in the `PYWORDS.utils.get_glossary_from_file(fname)` method, which also removes the '|' line continuations in the original dictionary line entries. 

Here's a simple working example.

```python
import PYWORDS.lookup

# Input filename
fname = 'loremipsum.txt'  # Path to file with text
fname2 = fname[:-4]+'_vocab.md'  # Replace '.txt' with '_vocab.md'; used to save vocab

# Read in from source file
with open(fname,'r') as f:
    txt = f.readlines()  # Read all text into a list (each item is a line of text)
txt = ''.join(txt)  # Combine everything into a single string (the ''. notation is used
# because the string that calls join() gets inserted between every item in the list,
# and we don't want any separator)

# Generate vocab list with markdown formatting
(vocab,missed) = lookup.get_vocab_list(txt,markdown_fmt=True)

# Save vocab list to file called 'loremipsum_vocab.md'
with open(fname2,'w') as f:
	for dictline in vocab:
        f.write(dictline+'  \n\n')  # NOTE: Different flavors of Markdown use different
        # conventions for new lines. Sometimes it's double-space, sometimes double-
        # newline (like here), sometimes it's a forward slash "/". This should be a
        # safe default.
# File is saved and closed.
```



The result will look something like this:

```markdown
**a** *prep* ante, abb. a.; [in calendar expression a. d. = ante diem => before the day]; 

**a** *prep* by (agent), from (departure, cause, remote origin/time); after (reference);  

**ab** *prep* by (agent), from (departure, cause, remote origin/time); after (reference);  
....
```

Which gets properly formatted in a Markdown reader such as Typora. 

Markdown is a fine format, but it's not the same as an XML-based format like .docx  (MS Word) or .odt. To convert, we can use Pandoc. The quirk here is that you need to convert to HTML first, then to your target format. This is the typical way of going about it (see e.g. [here](https://writing.stackexchange.com/questions/9056/from-markdown-to-odt-and-vice-versa-a-possible-distraction-free-writing-workfl)). If you have access to a command line, then it's a two-line solution, first converting to html, then to odt (as an example):

```sh
$ pandoc loremipsum_vocab.md -o tmp.html
$ pandoc tmp.html -o loremipsum_vocab.odt
```

Again, the above process (with some additional cleanup) has been automated in the `utils.get_glossary_from_file(fname)` method, and it prints the above pandoc commands for easier interfacing when pandoc is available. 



### Utilities

The `PYWORDS.utils`  module contains a few useful and somewhat powerful utilities for managing missed words. Current methods that have been implemented:

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



