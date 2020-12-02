# PYWORDS

### A Python Toolkit for Latin, Based on Whitaker's WORDS Program

As a student of new Latin who is learning from classical Latin books like Wheelock's, I have been dreaming of a way to automatically process documents, lookup obscure words, collect specific words (mathematical, scientific), and generate vocab lists from arbitrarily large uploaded texts. 

Fortunately, William Whitaker developed a fairly extensive dictionary written in a somewhat human-readable raw text format, and he provided an accompanying program written in Ada with very strong functionality. Several projects have aimed to bring WORDS to the Python language, but to date their attempts have been limited to word lookup alone. And so, I've decided to part with the existing work, and to develop *yet another* Python port of the WORDS program, to my own needs. 

## Current Functionality

So far only the inflections have been added. This still allows a reasonably large amount of functionality. 

```python
>>> from PYWORDS.definitions import *
```

A list of endings is provided:

```python
>>> endings_list
['', 'a', 'abam', 'abamini', 'abamur', 'abamus', 'abant',...,'uus', 'yn', 'yos']
```

And while the WORDS file INFLECTS.LAT, which provides a comprehensive list of inflections in a simply coded plaintext file, uses lines like:

`VPAR 3 0 NOM P F FUT  PASSIVE PPL 1 5 undae        B A `

These can be looked up and printed in human-readable dictionary-esque format:

```python
>>> interpret_inflection_key('VPAR 3 0 NOM P F FUT  PASSIVE PPL 1 5 undae        B A ')
'nominative plural feminine future passive participle of third conjugation verb participle'
>>> interpret_inflection_key('V     6 1 FUT   PASSIVE IND  1 S  2 3 bor            X A')
'indicative first person future singular passive of irregular verb'
```

Or use the key to obtain the ending, age, and relative frequency of the inflection (with associated lookup tables):

```python
>>> noun_inflections['N 1 1 NOM S C 1 1']
{'ending': 'a', 'age': 'X', 'frequency': 'A'}
>>> ages['X']
'common/unknown'
>>> inflection_frequencies['A']
'most freq'
```

This all makes it easy to provide detailed meanings of declensions and conjugations, useful when you want to try e.g. reverse ending lookups:

```python
>>> reverse_ending_lookup('ibus')
['locative plural form of  third declension noun', 'dative plural form of  third declension noun', 'ablative plural form of  third declension noun', 'dative plural  form of third declension positive adjective', 'ablative plural  form of third declension positive adjective', 'numeral', 'numeral']
```

The base functionality above will make parsing the full dictionary much easier.