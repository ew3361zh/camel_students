import camelcase_wk4
import unittest
# from unittest import TestCase - need to import unittest 

class TestCamelCase(unittest.TestCase):

    def test_camelcase_single_word(self):
        
        self.assertEqual('flumpy', camelcase_wk4.camel_case_it('FLUmPY'))

    def test_camelcase_multiple_words(self):

        self.assertEqual('helloWorld', camelcase_wk4.camel_case_it('Hello World'))
    
    def test_camelcase_multiple_spaces(self):

        self.assertEqual('', camelcase_wk4.camel_case_it('      '))
    
    def test_camelcase_multiple_words_multiple_spaces(self):

        self.assertEqual('helloWorld', camelcase_wk4.camel_case_it('     HELLO          WorlD    '))
    
    def test_camelcase_emojis(self):

        self.assertEqual('💃👯‍♀️👙', camelcase_wk4.camel_case_it('💃 👯‍♀️ 👙'))
    
    def test_camelcase_blank(self):

        self.assertEqual('', camelcase_wk4.camel_case_it(''))
    

if __name__ == '__main__':
    unittest.main()