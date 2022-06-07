# PyWORDS Source and Developer Documentation



### I. How the DICTLINE.GEN and INFLECTS.LAT Files Are Used

At the heart of the WORDS program are two "databases" (Whitaker simply used text files), `DICTLINE.GEN` containing the word stems and definitions, and `INFLECTS.LAT` containing the endings for various parts of speech. Thus if you want to look up a word from its *stem only*, whichever stem that may be, you would "query" `DICTLINE.GEN`, while you would use `INFLECTS.LAT` to determine whether an ending is valid with the given part of speech, declension/conjugation, etc, and to determine the inflection of that ending. 

---

Aside: When beginning to parse these text files, I decided to simply align them to particular column widths, (depends on the part of speech, so these are hard-programmed). This is a major **TODO** for the project: convert to a proper database or query-able file, because these text files are not doing it for me, even if they technically work. Really, simply migrating to a different file format would work fine. 

The original goal was to simply port over the WORDS program, so I kept the `DICTLINE.GEN` file as-is (with some added entries) and fixed some of the alignment in `INFLECTS.LAT` and worked around it. But as the functionality has departed quite a bit from the original program, it doesn't make sense to try to maintain this. 

The right approach is probably to create a SQLite database with a DICTLINE table and an INFLECTS table so that each dictionary entry is immediately related to its associated inflections. 

---