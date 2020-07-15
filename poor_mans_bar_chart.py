# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:23:53 2020

@author: Amanda Aparicio
@problem_author: Lee Vaughan from "Impractical Python Projects", pg. 15

Task: Take a sentence and create a bar chart which displays how many times each 
letter apppears in the sentence

My extra step: Create two versions of the chart: one version that only displays
letters which appears in the sentence and another which displays ALL letters, 
regardless of if it appears in the sentence or not.
"""

def create_dict(sentence):
    """Create a dictionary that counts how many times each letter appears 
    in the sentence
    """
    try:
        lower_sentence = str(sentence.lower())
        alpha_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
                      'j':0, 'k':0, 'l':0, 'm':0,'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
                      's':0, 't':0, 'u':0, 'v':0,'w':0,'x':0, 'y':0, 'z':0}
        
        for ele in lower_sentence:
            if (ele in alpha_dict):
                alpha_dict[ele] = alpha_dict[ele]+1
        return alpha_dict
    except:
        print("ERROR: Incorrect input.")

def make_short_dict(alpha_dict):
    """Creates a truncated version of the dictionary that only displays letters
    which have a value count greater than 0 
    """
    short_dict ={}
    for key,value in alpha_dict.items():
        if value !=0:
            short_dict[key] = value
    return short_dict

def poor_man(sentence, short = True):
    """ Create the Poor Man's Bar Graph. If short = True, only display letters which
    appear in the sentence. If short = False, display all letters, regardless if they
    appear in the sentence or not.
    """
    if short == True:
        full_dict = create_dict(sentence)
        short_dict = make_short_dict(full_dict)
        bar_chart = {}
        for key, value in short_dict.items():
            bar_chart[key] = [key]*value
        return bar_chart
    else:
        full_dict = create_dict(sentence)
        bar_chart = {}
        for key, value in full_dict.items():
            bar_chart[key]=[key]*value
        return bar_chart
        