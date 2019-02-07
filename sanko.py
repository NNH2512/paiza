# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:38:44 2019

@author: ngochung
"""
import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('You see two caves. In one cave,the dragon is friendly')
    print('and will share his treasue with you.The other dragon')
    print('is greedy and hungry,and will eat you on sight')
    print()
def chooseCave():
    cave=''
    while cave!='1' and cave!='2':
        print('Which cave will you go into ?(1 or 2)')
        cave=input('chon cave:')
    return cave
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(2)
    print('A large dragon jumps out in front of you ! He opens his jaws and...')
    print()
    time.sleep(2)
    friendlyCave=random.randint(1,2)
    if chosenCave==str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
playAgain='yes'
while playAgain=='yes' or playAgain=='y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again?(yes or no)')
    playAgain=input()