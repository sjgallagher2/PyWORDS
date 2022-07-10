import unittest
import pywords.lookup as lookup
import pywords.definitions as definitions
from pywords.matchfilter import MatchFilter
#from generate_database import verify_database


class TestInflectionClasses(unittest.TestCase):
    def test_nouninfl_overrides_declvar(self):
        ninfl1 = definitions.build_inflection(part_of_speech='N', decl='1', variant='1')
        ninfl2 = definitions.build_inflection(part_of_speech='N', decl='2', variant='1')
        ninfl3 = definitions.build_inflection(part_of_speech='N', decl='0', variant='1')
        ninfl4 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0')

        # Should not override
        self.assertFalse(ninfl1.overrides(ninfl1))
        self.assertFalse(ninfl1.overrides(ninfl2))
        self.assertFalse(ninfl1.overrides(ninfl3))

        # Should override
        self.assertTrue(ninfl1.overrides(ninfl4))

    def test_nouninfl_doesnt_override_ages(self):
        ninfl1 = definitions.build_inflection(part_of_speech='N', decl='1', variant='1', age='X')
        ninfl2 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', age='A')
        self.assertFalse(ninfl1.overrides(ninfl2))

    def test_nouninfl_doesnt_override_frequencies(self):
        ninfl1 = definitions.build_inflection(part_of_speech='N', decl='1', variant='1', frequency='X')
        ninfl2 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', frequency='A')
        self.assertFalse(ninfl1.overrides(ninfl2))

    def test_nouninfl_doesnt_override_case_number_gender(self):
        ninfl1 = definitions.build_inflection(part_of_speech='N', decl='1', variant='1', case='GEN', number='S', gender='M')
        ninfl2 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', case='GEN', number='S', gender='M')
        ninfl3 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', case='NOM', number='S', gender='M')
        ninfl4 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', case='GEN', number='P', gender='M')
        ninfl5 = definitions.build_inflection(part_of_speech='N', decl='1', variant='0', case='GEN', number='S', gender='F')

        self.assertTrue(ninfl1.overrides(ninfl2))
        self.assertFalse(ninfl1.overrides(ninfl3))
        self.assertFalse(ninfl1.overrides(ninfl4))
        self.assertFalse(ninfl1.overrides(ninfl5))

    def test_adjinfl_overrides_declvar(self):
        ainfl1 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='1')
        ainfl2 = definitions.build_inflection(part_of_speech='ADJ', decl='2', variant='1')
        ainfl3 = definitions.build_inflection(part_of_speech='ADJ', decl='0', variant='1')
        ainfl4 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0')
        ainfl5 = definitions.build_inflection(part_of_speech='ADJ', decl='0', variant='0')

        # Should not override
        self.assertFalse(ainfl1.overrides(ainfl1))
        self.assertFalse(ainfl1.overrides(ainfl2))
        self.assertFalse(ainfl1.overrides(ainfl3))

        # Should override
        self.assertTrue(ainfl1.overrides(ainfl4))
        self.assertTrue(ainfl1.overrides(ainfl5))

    def test_adjinfl_doesnt_override_ages(self):
        ainfl1 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='1', age='X')
        ainfl2 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', age='A')
        ainfl3 = definitions.build_inflection(part_of_speech='ADJ', decl='0', variant='0', age='A')
        self.assertFalse(ainfl1.overrides(ainfl2))
        self.assertFalse(ainfl1.overrides(ainfl3))

    def test_adjinfl_doesnt_override_frequencies(self):
        ainfl1 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='1', frequency='X')
        ainfl2 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', frequency='A')
        ainfl3 = definitions.build_inflection(part_of_speech='ADJ', decl='0', variant='0', frequency='A')
        self.assertFalse(ainfl1.overrides(ainfl2))
        self.assertFalse(ainfl1.overrides(ainfl3))

    def test_adjinfl_doesnt_override_case_number_gender(self):
        ainfl1 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='1', case='GEN', number='S', gender='M')
        ainfl2 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', case='GEN', number='S', gender='M')
        ainfl3 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', case='NOM', number='S', gender='M')
        ainfl4 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', case='GEN', number='P', gender='M')
        ainfl5 = definitions.build_inflection(part_of_speech='ADJ', decl='1', variant='0', case='GEN', number='S', gender='F')

        self.assertTrue(ainfl1.overrides(ainfl2))
        self.assertFalse(ainfl1.overrides(ainfl3))
        self.assertFalse(ainfl1.overrides(ainfl4))
        self.assertFalse(ainfl1.overrides(ainfl5))

    def test_vinfl_overrides_declvar(self):
        vinfl1 = definitions.build_inflection(part_of_speech='V', conj='1', variant='1')
        vinfl2 = definitions.build_inflection(part_of_speech='V', conj='2', variant='1')
        vinfl3 = definitions.build_inflection(part_of_speech='V', conj='0', variant='1')
        vinfl4 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0')
        vinfl5 = definitions.build_inflection(part_of_speech='V', conj='0', variant='0')

        # Should not override
        self.assertFalse(vinfl1.overrides(vinfl1))
        self.assertFalse(vinfl1.overrides(vinfl2))
        self.assertFalse(vinfl1.overrides(vinfl3))

        # Should override
        self.assertTrue(vinfl1.overrides(vinfl4))
        self.assertTrue(vinfl1.overrides(vinfl5))

    def test_vinfl_doesnt_override_ages(self):
        vinfl1 = definitions.build_inflection(part_of_speech='V', conj='1', variant='1', age='X')
        vinfl2 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', age='A')
        vinfl3 = definitions.build_inflection(part_of_speech='V', conj='0', variant='0', age='A')
        self.assertFalse(vinfl1.overrides(vinfl2))
        self.assertFalse(vinfl1.overrides(vinfl3))

    def test_vinfl_doesnt_override_frequencies(self):
        vinfl1 = definitions.build_inflection(part_of_speech='V', conj='1', variant='1', frequency='X')
        vinfl2 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', frequency='A')
        vinfl3 = definitions.build_inflection(part_of_speech='V', conj='0', variant='0', frequency='A')
        self.assertFalse(vinfl1.overrides(vinfl2))
        self.assertFalse(vinfl1.overrides(vinfl3))

    def test_vinfl_doesnt_override_tense_number_person_voice_mood(self):
        vinfl1 = definitions.build_inflection(part_of_speech='V', conj='1', variant='1', tense='PRES', number='S', person='1', voice='ACTIVE', mood='IND')
        vinfl2 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', tense='PERF', number='S', person='1', voice='ACTIVE', mood='IND')
        vinfl3 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', tense='PRES', number='P', person='1', voice='ACTIVE', mood='IND')
        vinfl4 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', tense='PRES', number='S', person='3', voice='ACTIVE', mood='IND')
        vinfl5 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', tense='PRES', number='S', person='1', voice='PASSIVE', mood='IND')
        vinfl6 = definitions.build_inflection(part_of_speech='V', conj='1', variant='0', tense='PRES', number='S', person='1', voice='ACTIVE', mood='SUB')

        self.assertFalse(vinfl1.overrides(vinfl2))
        self.assertFalse(vinfl1.overrides(vinfl3))
        self.assertFalse(vinfl1.overrides(vinfl4))
        self.assertFalse(vinfl1.overrides(vinfl5))
        self.assertFalse(vinfl1.overrides(vinfl6))


class TestTackonClass(unittest.TestCase):
    def test_tackon_matches_dictline_entry(self):
        pass
    def test_tackon_matches_inflection(self):
        pass


if __name__ == '__main__':
    #dl_entry = lookup.dictline[11053]['entry']
    #for infl in definitions.get_possible_inflections(dl_entry):
    #    print(infl)
    dl_entry = lookup.dictline[36715]['entry']  # Deponent 2 1 (tueor)
    infls = definitions.get_possible_inflections(dl_entry)

