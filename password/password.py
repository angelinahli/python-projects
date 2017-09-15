"""
Password Generator

Pulls a bunch of words from a random list of english words, and then generates
a password based on a specified difficulty level.

Date: 2/28/17
Written by: Angelina Li
"""

import random
from vocabulary import englishwords

# Create materials for us to work with.

def easy_words():
    easy = []
    for word in englishwords:
        if len(word) > 1 and len(word) < 8:
            easy.append(word)
    return easy

def large_words():
    large = []
    for word in englishwords:
        if len(word) >= 8:
            large.append(word)
    return large

NON_ALPNUM = '!@#$%^&*+'
JOINERS = '~./\-_='
NUM = '1234567890'
CAP_ALPH = 'qhzip'

easy = easy_words()
large = large_words()
change_alph = {'a': '4', 'e': '3', 'o': '0'}


def easy_pass(n):
    password = []
    for i in range(n):
        password.append(random.choice(easy).title())
    return random.choice(JOINERS).join(password) + random.choice(NUM)

def med_pass(n):
    password = []
    for i in range(n):
        order = {0: large, 1: easy}
        word = random.choice(order[i % 2])
        new_word = ""
        for char in word:
            if char in change_alph:
                new_word += change_alph[char]
            else:
                new_word += char
        password.append(new_word)
    return random.choice(JOINERS).join(password) + random.choice(NUM)

def strong_pass(n):
    password = []
    for i in range(n):
        word = random.choice(large)
        new_word = ""
        j = 1
        for char in word:
            if char in change_alph:
                new_word += change_alph[char]
            elif char in CAP_ALPH:
                new_word += char.upper()
            else:
                new_word += char
            if j % 4 == 0:
                order = [NON_ALPNUM, NUM]
                new_word += random.choice(random.choice(order))
            j += 1
        password.append(new_word)
    return random.choice(JOINERS).join(password)


def difficulty_generator():
    diff = get_difficulty()
    while diff not in '123' or len(diff) != 1:
        print "Please enter a NUMber from 1 to 3."
        diff = get_difficulty()
    return int(diff)
    
def get_difficulty():
    return raw_input("How secure should the password be, from a scale " \
        "of 1: least secure to 3: most secure? ")

def password_generator():
    diff = difficulty_generator()
    n = random.randint(2,4)
    password = {1: easy_pass(n), 2: med_pass(n), 3: strong_pass(n)}
    print "Your password is: " + password[diff]

password_generator()