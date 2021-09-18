import camelcase_wk4
import unittest
# from unittest import TestCase - need to import unittest 

class TestCamelCase(unittest.TestCase):

    def test_camelcase_one_word(self):

        self.assertEqual('helloWorld', camelcase_wk4.camel_case_it('Hello World'))
        self.assertEqual('', camelcase_wk4.camel_case_it(''))
        self.assertEqual('helloWorld', camelcase_wk4.camel_case_it('     HELLO          WorlD    '))
        self.assertEqual('💃👯‍♀️👙', camelcase_wk4.camel_case_it('💃 👯‍♀️ 👙'))
    
    def test_camelcase_blank(self):

        self.assertEqual('', camelcase_wk4.camel_case_it(''))
    

if __name__ == '__main__':
    unittest.main()