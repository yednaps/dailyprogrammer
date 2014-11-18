#!/usr/bin/python

import random, string

words = [l.strip().lower() for l in open('/usr/share/dict/words')]
wordse = [w for w in words if len(w) > 2 and len(w) < 6]
wordsm = [w for w in words if len(w) > 5 and len(w) < 10]
wordsh = [w for w in words if len(w) > 9]

def printMan(strikes):
    art = ['    ____',
           '   |/   |',
           '   |',
           '   |',
           '   |',
           '   |',
           '/-----\\']

    if strikes > 0:
        art[2] = '   |    O'
    if strikes > 1:
        art[3] = '   |   /|\\'
    if strikes > 2:
        art[4] = '   |   / \\'

    for i in art: print i

def update(word, guessed):
    out = ''
    for i in word:
        if i in guessed: out += i
        else: out += '_'
    return out

level = ''
while level in 'emh':
    level = raw_input('Select Level: easy[e], medium[m], or hard[h]? ')
    if level not in 'emhq': next
    if level == 'q': break

    if level == 'e':
        print('Easy Mode')
        word = random.choice(wordse)
    elif level == 'm':
        print('Medium Mode')
        word = random.choice(wordsm)
    else:
        print('Hard Mode')
        word = random.choice(wordsh)
    break

length = len(word)
current = '_'*length
guessed = ''
unguessed = string.lowercase
strikes = 0
guesses = 0

while strikes < 3:
    printMan(strikes)
    print(current)
#print('Number of guesses: %i' % guesses)
    guess = raw_input('Choose a letter: ')
    guessed += guess
    if guess in word: current = update(word,guessed)
    else:
        strikes += 1

if strikes == 3:
    printMan(strikes)
    print(word)
    print('Game Over')

if current == word:
    print('You win!')