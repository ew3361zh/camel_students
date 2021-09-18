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

    def test_camel_case_international(self):

        input_and_expected_outputs = {
            '你叫 什么 名字': '你叫什么名字',
            'Write a résumé': 'writeARésumé',
            'Über die Brücke': 'überDieBrücke',
            'Fahre über die Brücke': 'fahreÜberDieBrücke',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camelcase_wk4.camel_case_it(input_val))
    

if __name__ == '__main__':
    unittest.main()