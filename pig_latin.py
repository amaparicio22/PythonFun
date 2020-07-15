# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:49:10 2020

@author: Amanda Aparicio
@problem_author: Lee Vaughan from the book "Impractical Python Projects", pg. 15

Task: Take a word and "translate" it to its Pig Latin form
My next step: Take a sentence and "translate" it to its Pig Latin form

Please note: This is just *my* solution to the problem posed. 
"""

def make_pig_latin_word(word):
    """ Converts a single word to Pig Latin. Takes into account common punctuation.
    """
    try:
        pig_word = str(word.lower().strip())
        vowels =['a', 'e', 'i', 'o', 'u']
        punctuations = [',', '?','.', ':', ';', '!']
        if (pig_word[0] in vowels) and (pig_word[-1] not in punctuations):
            pig_word = pig_word +'way'
        elif (pig_word[0] in vowels) and (pig_word[-1] in punctuations):
            n = len(pig_word)
            pig_word = pig_word[:n-1]+'way'+pig_word[-1]
        elif (pig_word[-1] in punctuations):
            n = len(pig_word)
            pig_word = pig_word[1:n-1]+pig_word[0]+'ay'+pig_word[-1]
        else:
            pig_word = pig_word[1:]+pig_word[0]+'ay'
        return pig_word
    except:
        print("ERROR: Incorrect input")

def make_pig_latin_sent(sentence):
    """Converts a sentence into Pig Latin
    """
    try:
        pig_list = sentence.split()
        pig_sentence = ''
        for word in pig_list:
            pig_word = make_pig_latin_word(word)
            pig_sentence = pig_sentence+' '+pig_word
        return pig_sentence.strip()
    except:
        print("ERROR: Incorrect input.")