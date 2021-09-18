""" 
revisited week 4 for testing
Niko Tomlinson week 1 8/25/21 Capstone project, revisited 9/6/21 for practice on git functions and processes

Write a program that turns a sentence into camel case. The first word is lowercase, 
the rest of the words have their initial letter capitalized, and all of the words 
are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
your program will output "fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a 
valid variable name. You don't need to be exhaustive in checking, but test for a 
few common issues, such as starting with a number, or containing invalid characters 
such as # or + or ". 

Test your program with different example inputs, and comment your code.  
"""
import re

def welcome():
    """Display welcome message, using stars"""
    message = 'Welcome my friend!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars} \n')

def instructions():
    """Give instructions to user for how program works"""
    print('Instructions: Enter a sentence and this program will convert it to a single camel case string\n')

def get_sentence():
    """Ask for user input on sentence, make sure it's not blank"""
    sentence = input('Please enter a sentence: ')
    while not sentence:
        sentence = input('You have to enter something here: ')
    return sentence

def camel_case_it(sentence):
    # check for characters we don't want
    sentence_regex = re.compile(r'[0-9#+"]+')
    sentence_found = sentence_regex.search(sentence)
    while sentence_found is not None:
        print('Please try again to enter a sentence - don\'t use any numbers or any non-letter characters like (" + #)')
        sentence = get_sentence()
        sentence_found = sentence_regex.search(sentence)
    sentence_list = sentence.split()
    final_sentence = ''
    # use for loop to go through list of sentence pieces numerically
    for sentence_piece in range(len(sentence_list)):
        # start with first piece of sentence and make it all lowercase
        if sentence_piece == 0:
            final_sentence = sentence_list[sentence_piece].lower()
        # for all other pieces, make them lowercase and then title-cased
        else:
            final_sentence = final_sentence + sentence_list[sentence_piece].lower().title()
    return final_sentence

def main():
    welcome()
    instructions()
    sentence = get_sentence()
    final_sentence = camel_case_it(sentence)
    print(final_sentence)

if __name__ == '__main__':
    main()