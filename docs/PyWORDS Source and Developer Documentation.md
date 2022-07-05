# PyWORDS Source and Developer Documentation



### I. How the DICTLINE and INFLECTS Files Are Used

At the heart of the original WORDS program are two "databases" (Whitaker simply used text files), `DICTLINE.GEN` containing the word stems and definitions, and `INFLECTS.LAT` containing the endings for various parts of speech. Thus if you want to look up a word from its *stem only*, whichever stem that may be, you would "query" `DICTLINE.GEN`, while you would use `INFLECTS.LAT` to determine whether an ending is valid with the given part of speech, declension/conjugation, etc, and to determine the inflection of that ending. 

---

Aside: When beginning to parse these text files, I decided to simply align them to particular column widths, (depends on the part of speech, so these are hard-programmed). I've now converted them to `.tsv` (tab-separated) files so they can be modified through any spreadsheet program, or imported into a SQLite database. The biggest difference is a unified set of columns for all parts of speech, as opposed to Whitaker's original files, which had columns that were part-of-speech-dependent.

One obvious drawback to changing the file format is we cannot diff with the [Whitaker's WORDS](https://github.com/mk270/whitakers-words) repository on github. This doesn't seem to be a big deal, considering the last commit to those files was 3 years ago (as of June 2022). 

---

The main data files are now `DICTLINE.tsv` and `INFLECTS.tsv` which have the following columns:

| Dictline Column   | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| `dl_id`           | Primary key                                                  |
| `dl_stem1`        | First stem, meaning is dependent on part of speech, declension/conjugation, and variant, but those details are managed by `INFLECTS.tsv` |
| `dl_stem2`        | Second stem                                                  |
| `dl_stem3`        | Third stem                                                   |
| `dl_stem4`        | Fourth stem                                                  |
| `dl_pos`          | Part of speech; string: `{N,PRON,ADV,ADJ,NUM,V,VPAR,`<br />`INTERJ,CONJ,SUPINE,PREP,PACK,TACKON,PREFIX,SUFFIX, X}` |
| `dl_grammar_code` | Type, variant, gender, comparison, kind, depending on part of speech. This is left over in case something went wrong when parsing it into the proper columns, will eventually be removed. |
| `dl_type`         | Declension or conjugation, depending on part of speech; integer as a string |
| `dl_variant`      | Variant code; integer as a string                            |
| `dl_gender`       | Gender (for noun-like parts of speech), either masc., fem., neut., common<br />(context-dependent gender), or N/A (`X`) |
| `dl_comparison`   | Comparison for adjective-like parts of speech; positive, comparative, or superlative; some entries have their comparative and superlative stems in the entry itself, others use a separate entry; depends on how inflections are handled |
| `dl_kind`         | Noun kind, pronoun kind, verb kind, or number kind           |
| `dl_aux_case`     | Preposition auxiliary cases (e.g. *ad* => accusative)        |
| `dl_age`          | Time period code, from archaic to modern (for this and others below, see `definitions.py`) |
| `dl_area`         | Subject area (e.g. A="Agriculture, Flora, Fauna, Land, Equipment, Rural") |
| `dl_geography`    | Geographical relevance, where applicable                     |
| `dl_frequency`    | How frequent or infrequent this form is                      |
| `dl_source`       | Source of definitions                                        |
| `dl_senses`       | Definitions for this word                                    |



| Inflects Column   | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| `infl_id`         | Primary key                                                  |
| `infl_pos`        | Part of speech                                               |
| `infl_type`       | Declension/conjugation                                       |
| `infl_variant`    | Variant                                                      |
| `infl_case`       | Case (e.g. NOM, GEN, ACC)                                    |
| `infl_tense`      | Verb tense                                                   |
| `infl_plurality`  | Plurality of noun-like parts of speech (singular, plural)    |
| `infl_gender`     | Gender of noun- and adjective-like parts of speech           |
| `infl_person`     | First, second, or third person                               |
| `infl_comparison` | Adjective/adverb comparison                                  |
| `infl_voice`      | Verb voice (active or passive)                               |
| `infl_mood`       | Verb mood (indicative, imperative, infinitive, subjunctive)  |
| `infl_numtype`    | Number type (cardinal, ordinal, adverbial, distributive)     |
| `infl_stem_id`    | ID of stem (1,2,3,4) on which this inflection applies; dependent on part of speech, declension/conjugation, and variant |
| `infl_ending`     | Inflection ending                                            |
| `infl_age`        | Age when inflection was used, from archaic through modern    |
| `infl_frequency`  | Inflection frequency, from most frequent to very rare        |



Performing a word lookup can be done without PyWORDS, by querying either with the find function in a spreadsheet program like LibreOffice Calc, or by converting to a database (e.g. SQLite) and actually using a SQL query. For a given word, one can do the following:

1. Determine the possible stem/ending pairs to find candidate stems; this is done by looking for ending substrings at the end of the lookup word which can possibly appear in Latin
2. Look up each of the resulting stems in `DICTLINE` and record all matches in the dictionary
3. Verify that the ending and the stem are compatible based on the part of speech, declension, and variant. This is the biggest step, because there are several edge cases to watch out for.



For an example, let's take the word *pulchritudinis*. 

1. Possible endings are found by searching the `INFLECTS` endings column. We have `pulchritudinis|` (no ending), `pulchritudini|s`, and `pulchritudin|is`, and no other endings (e.g. "-nis", "-inis", "-dinis") appear in `INFLECTS` so we're done. At this point we're looking at all endings in all parts of speech, just to narrow down our search for stems.
2. The stems "pulchritudinis", "pulchritudini-", and "pulchritudin-" are looked up in the stem1, stem2, stem3, and stem4 columns of `DICTLINE`. Only "pulchritudin-" returns a match, at `dl_id=31209`, stem2. The entry is:

```
pulchritudo	pulchritudin			N	3	1	F		T		X	X	X	B	X	beauty, excellence;
```

3. This is a noun (N) third declension first variant (3 1) feminine (F) thing (T). The ending we found was "-is", so we check `INFLECTS` for any `N 3 1` (third decl., first var.), and `N 3 0` (third decl., common var.) with the ending "-is". If there is overlap (i.e. an inflection marked `N 3 1` that has the same case, gender, number, inflection age, and inflection frequency as an inflection marked `N 3 0`), the more specific `N 3 1` should be used and the other discarded. It turns out we have two: `infl_id=127` and `infl_id=142`.

```
127	N	3	0	GEN		S	X						2	is	X	A
142	N	3	1	ACC		P	C						2	is	X	C
```

Both of these have `infl_stem_id=2` which is the same stem as we matched to, and the genders are`X` and `C`, which are valid for feminine. Therefore this is our answer: this word possibilities include *pulchritudo, pulchritudinis* (f) meaning "beauty, excellence", with matching inflections of the genitive singular (frequency A=common) and accusative plural (frequency C=uncommon).

Other parts of speech have their own quirks. For example, verbs also have the `V 0 0` common conjugation/variant pair, and there are participle inflections with part of speech `VPAR` that must be added, as well as the supine `SUPINE 0 0`, of which there are only two entries. Depending on the word kind (e.g. `verb_kind=DEP`, meaning deponent), these selections might need to be limited further. 

If nothing is returned, we have more options. First is to check for any *uniques*, words which are sufficiently irregular that they must be listed explicitly in `UNIQUES.LAT`. This hasn't been implemented yet, but it's not far off. Another special case is *sum, esse* which is like its own unique in all inflections, and so it's stored separately as `ESSE.LAT`, or at least it was originally.



The PyWORDS program basically does the above steps for you with the method `lookup._simple_match(w)`. This method is private because the main word lookup method `lookup.match_word(w)` also tries tricks, like removing enclitics (-que, -ve, -ne) if no matches were found. This method returns a list of matches, where a match itself is a list with the word stem and ending we matched to (recall that multiple stem/ending combinations are possible), and a dictionary containing `stem1`, `stem2`, `stem3`,`stem4` and `entry` (separate from stems). This inner list is a "match" in the PyWORDS sense, used in methods like `lookup.get_dictionary_string()`. For example, the output from `match_word("pulchritudinis")` should be

```python
matches = [  # List of matches
['pulchritudin','is',{'stem1':'pulchritudo','stem2':'pulchritudin',...,'entry':<pywords.definitions.DictlineNounEntry object>}]  # This whole thing is one match
]  # Only one stem/ending pair with one dictline entry returned
```

To use this with a method like `get_word_inflections(match)`, pass `matches[0]` as the match object, and PyWORDS does the rest by comparing the known information to the full set of inflection objects, built from the `INFLECTS` file when `pywords.lookup` is imported.

I recently updated the lookup engine to work as follows: 

1. When `match_word` is called, we run `_simple_match` to get a basic lookup; see step 2. If we didn't find anything, we try removing enclitics, and run `_simple_match` again. Then we're done!
2. `_simple_match` makes a list of possible stem/ending pairs with `lookup.find_endings(w)`, ignoring inflections and parts of speech. For each stem/ending pair that's possible, we search for the stem in the alphabetized list of all stems, starting with stem1, then stem2, stem3, and stem4. A bisect search is used. These are all the potential matches, but we haven't checked if the stem/ending pair is actually *possible* given what we now know about the word's part of speech, declension/conjugation, variant, gender, etc. 
3. At the end of `_simple_match` we call `lookup.is_possible_ending(match)` on all potential matches. This is where we check which of the four stems actually matched our stem (e.g. with pulchritudo, only stem 2 actually matches; in other words, multiple stems can match). For each of these, we get a list of possible inflections with `definitions.get_possible_inflections(match,infl_age,infl_frequency)`. This method is where most of the logic is found. A late check for a special case with `V 3 1` words is made, then we add endings from the list of inflections which apply to our stem (every inflection has an associated stem, we only match to inflections that apply to our stem). 
4. Currently, only the most common and general inflections are considered during `_simple_match`, to avoid including rare inflections or inflections from early or late Latin only. For more details about all the logic in `definitions.get_possible_inflections()`, see the code, it's documented. Basically, we make a list of all possible inflections given the information we have available, and that list gets cached. E.g. there is a cache for `N 1 1` which includes all the inflections which apply, including `N 1 0`. Then we check for the word kind and limit results based on that. 



