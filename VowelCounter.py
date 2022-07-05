#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VowelCounter
Created by Braden Piper, bradenpiper.com
Created on Wed Jun 29, 2022
version = 1.0
------------------------------------------
VowelCounter is a simple, friendly program that will count the number of vowels
in any text string you provide it with. The program asks the user to input some
text, and it will return the vowel count within that text.
------------------------------------------
"""

# FUNCTION DEFINITIONS

def vowelCounter(string):
    '''
    Accepts a string. The string should be lowercase.
    Returns an int, the number of vowels in the string.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    numVowels = 0
    for letter in string:
        if letter in vowels:
            numVowels += 1
    print('Number of vowels:', numVowels)

def replayQuery():
    '''
    Asks the user if they want to run the program again.
    Returns a boolean. True if the answer is yes, False if the answer is no.
    '''
    yesAnswers = ['y','Y','yes','Yes','YES']
    noAnswers = ['n','N','no','NO']
        
    while True:
        print('Would you like me to count some more vowels for you?')
        print('y / n')
        answer = input()
        if answer in yesAnswers:
            return True
        elif answer in noAnswers:
            return False
        else:
            print("I did not understand your answer, please type 'y' or 'n' to answer.")
  
# PROGAM          
  
runProgram = True  
firstTime = True

while runProgram == True:    
    if firstTime == True:
        print("Hello, I am VowelCounter. I will tell you how many vowels are in the text string you input.")
        print('Please input your text below, then press enter:')
        firstTime = False
    else:
        print('Please input your text below, then press enter:')
    vowelCounter(input().lower())
    if replayQuery() == True:
        continue
    else:
        runProgram = False
        
print('If you ever need someone to count your vowels, I am here.')
print('That is why they call me VowelCounter.')
print('Thank you. Goodbye.')
