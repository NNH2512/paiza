# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 03:37:51 2019

@author: ngochung
"""
import random
guessesTaken=0
print('hello ! What is your name?')
myName=input('nhap ten:')
number=random.randint(1,20)
print('Well,'+myName+',I am thinking of a number between 1 and 20.')

while guessesTaken<6:
    print('Taken a guess.')#there are four spaces in font of print.
    guess=input('nhap so ban doan:')
    guess=int(guess)
    
    guessTaken=guessesTaken+1
    
    if guess<number:
        print('Your guess is too low.')#There are eight spaces in fornt of print
    if guess>number:
        print('Your gues is too high.')
    if guess== number:
        break
if guess==number:
    guessesTaken=str(guessesTaken)
    print('Good job,'+myName+'!You guessed my number in '+ guessesTaken +' guesses!')
if guess!=number:
    number=str(number) 
    print('Nope.The number Iwas thinking of was'+number)   