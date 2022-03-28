import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        a = 'Love'
        b = 'Amour'
        c =  'Hello'
        d = 'Bonjour'
        e = 'Null'
        
        self.assertEqual(english_to_french(a), b)
        self.assertEqual(english_to_french(b), b)
        self.assertEqual(english_to_french(e), e)
        self.assertEqual(english_to_french(c), d)
      
class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self):
        a = 'Love'
        b = 'Amour'
        c =  'Hello'
        d = 'Bonjour'
        e = 'Null'
        self.assertEqual(french_to_english(b),a)
        self.assertEqual(french_to_english(a), a)
        self.assertEqual(french_to_english(e), e)
        self.assertEqual(french_to_english(d), c)

unittest.main()