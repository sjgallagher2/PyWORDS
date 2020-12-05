class MatchFilter:
    '''
    Collection of flags used to filter word matches
    To use this class:
        1) Create an instance
        2) Set desired parameters, or remove desired parameters, from lists
        3) Pass to a method which accepts a filter
    
    Examples: let `filt=MatchFilter()`
    filt.frequencies = filt.default_frequencies[:2] # Only 'X', 'A', and 'B'
    # only frequencies as common or more common than 'B' (the hard way):
    filt.frequencies = filt.default_frequencies[:filt.default_frequencies.index('B')]
    filt.frequencies = ['A','C'] # Only frequencies 'A' and 'C'

    MatchFilters are most useful for exclusions/selections or particular parameters.
    They will perform the best when only the desired filters are included.
    '''
    def __init__(self, ages=[], areas=[], geographies=[], frequencies=[],
        noun_declensions=[], verb_conjugations=[], adj_declensions=[],
        noun_kinds=[], verb_kinds=[], number_kinds=[], pronoun_kinds=[],
        comparisons=[], moods=[], genders=[], persons=[], numbers=[],
        tenses=[], voices=[], cases=[], variants=[], substantives=True):
        # DEFAULTS
        # Used to make initializing filter values easier
        self.default_ages = ['X','A','B','C','D','E','F','G','H'] # Coded time periods that are valid
        self.default_areas = ['X','A','B','D','E','G','L','P','S','T','W','Y']
        self.default_geographies=['X','A','B','C','D','E','F','G','H','I','J','K','N','P','Q','R','S','U']
        self.default_frequencies=['X','A','B','C','D','E','F','I','M','N']
        self.default_noun_declensions=['1','2','3','4','5','9']
        self.default_variants=['0','1','2','3','4','5','6','7','8','9']
        self.default_cases=['X','NOM','VOC','GEN','DAT','ACC','LOC','ABL']
        self.default_verb_conjugations=['0','1','2','3','4','5','6','7','8','9']
        self.default_adj_declensions=['0','1','2','3','9']
        self.default_noun_kinds=['X','S','M','A','G','N','P','T','L','W']
        self.default_verb_kinds=['X','TO_BE','TO_BEING','GEN','DAT','ABL','TRANS','INTRANS','IMPERS','DEP','SEMIDEPO','PERFEF']
        self.default_number_kinds=['X','CARD','ORD','DIST','ADVERB']
        self.default_pronoun_kinds=['X','PERS','REL','REFLEX','DEMONS','INTERR','INDEF','ADJECT']
        self.default_comparisons=['X','POS','COMP','SUPER']
        self.default_moods=['X','IND','SUB','IMP','INF','PPL']
        self.default_genders=['X','M','F','N','C']
        self.default_persons=['0','1','2','3']
        self.default_numbers=['X','S','P']
        self.default_tenses=['X','PRES','IMPF','PERF','FUT','FUTP','PLUP','INF']
        self.default_voices=['X','ACTIVE','PASSIVE']

        self.substantives = True  # Show noun forms of adjectives
        self.ages=ages 
        self.areas=areas 
        self.geographies=geographies
        self.frequencies=frequencies
        self.variants=variants
        self.noun_declensions=noun_declensions
        self.cases=cases
        self.verb_conjugations=verb_conjugations
        self.adj_declensions=adj_declensions
        self.noun_kinds=noun_kinds
        self.verb_kinds=verb_kinds
        self.number_kinds=number_kinds
        self.pronoun_kinds=pronoun_kinds
        self.comparisons=comparisons
        self.moods=moods
        self.genders=genders
        self.persons=persons
        self.numbers=numbers
        self.tenses=tenses
        self.voices=voices

    def check_inflection(self,infl,part_of_speech):
        '''
        Return True if inflection is OK
        part of speech must be provided for performance
        '''
        pos = part_of_speech

        # Common to all inflections
        if self.ages:
            if infl.age not in self.ages:
                return False
        if self.frequencies:
            if infl.frequency not in self.frequencies:
                return False
        if self.variants:
            if infl.var not in self.variants:
                return False
        if pos == 'N':
            if self.noun_declensions:
                if infl.decl not in self.noun_declensions:
                    return False
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
            if self.cases:
                if infl.case not in self.cases:
                    return False
        elif pos == 'ADJ':
            if self.adj_declensions:
                if infl.decl not in self.adj_declensions:
                    return False
            if self.comparisons:
                if infl.comparison not in self.comparisons:
                    return False
            if self.cases:
                if infl.case not in self.cases:
                    return False
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
        elif pos == 'V':
            if self.verb_conjugations:
                if infl.conj not in self.verb_conjugations:
                    return False
            if self.moods:
                if infl.mood not in self.moods:
                    return False
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.persons:
                if infl.person not in self.persons:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
            if self.tenses:
                if infl.tense not in self.tenses:
                    return False
            if self.voices:
                if infl.voice not in self.voices:
                    return False
        elif pos == 'VPAR':
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.persons:
                if infl.person not in self.persons:
                    return False
            if self.cases:
                if infl.case not in self.cases:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
            if self.tenses:
                if infl.tense not in self.tenses:
                    return False
            if self.voices:
                if infl.voice not in self.voices:
                    return False
        elif pos == 'PRON':
            if self.cases:
                if infl.case not in self.cases:
                    return False
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
        elif pos == 'NUM':
            if self.number_kinds:
                if infl.kind not in self.number_kinds:
                    return False
            if self.genders:
                if infl.gender not in self.genders:
                    return False
            if self.cases:
                if infl.case not in self.cases:
                    return False
            if self.numbers:
                if infl.number not in self.numbers:
                    return False
        return True
        

    def check_dictline_word(self,w):
        # Return True if word is OK
#        if self.ages:
#        if self.areas:
#        if self.geographies:
#        if self.frequencies:
#        if self.noun_declensions:
#        if self.verb_conjugations:
#        if self.adj_declensions:
#        if self.noun_kinds:
#        if self.verb_kinds:
#        if self.number_kinds:
#        if self.pronoun_kinds:
#        if self.comparisons:
#        if self.moods:
#        if self.genders:
#        if self.persons:
#        if self.numbers:
#        if self.tenses:
#        if self.voices:
        return True
    def remove_substantives(self,matches):
        '''
        Return list of substantive adjectives from list of matches
        NOTE: This is aggressive. If an adjective is found, ALL nouns with matching stems will be removed. With a
        word like 'bonum' this is safe. Other words might not be. 
        '''
        filtmatches = matches
        adjs = set()
        # First make a list of adjectives
        for m in matches:
            e = m[2]['entry']
            if e.pos == 'ADJ':
                adjs.add(m[2]['stem2'])
        for stem in adjs:
            for m in filtmatches[:]:
                if m[2]['stem2'] == stem and m[2]['entry'].pos == 'N':
                    filtmatches.remove(m)
        return filtmatches

