"""
-*- coding: utf-8 -*-
Makes a rock-paper-scissors inspired game. Allows user to input any valid
list of gestures to play with. Will output a set of rules on which gestures
defeat other gestures, as well as allow the user to play a game against a

Valid gesture lists:
(1) Contain an odd set of gestures
(2) Contain unique gestures
(3) Contain at least 3 gestures (to ensure there are sufficient gestures needed
    for play)

Date: 6/21/17
Written by: Angelina Li
"""

import random
fun_death_words = ['beats up', 'blasts', 'crushes', 'demolishes', 'destroys',
                   'extinguishes', 'lambasts', 'pummels', 'ruins', 'shatters',
                   'smashes', 'torpedoes', 'vaporizes', 'wrecks', 'stampedes']

### ---- Functions for game below ---- ### 

def get_valid_gesture_list():
    """
    Prompts the user to input a valid list of gestures.
    The list has to be odd to ensure each gesture has an equal chance of winning."""
    gestures = raw_input("Insert a valid list of gestures here, separated by commas: ")
    gestures = [gesture.strip().lower() for gesture in gestures.split(",")]
    check_unique = len(gestures) > len(set([g.lower() for g in gestures]))
    check_odd = len(gestures) % 2 != 1
    check_three = len(gestures) < 3
    errors = {
        check_odd: 'Please enter an ODD list', 
        check_unique: 'Please enter a UNIQUE list', 
        check_three: 'Please enter at least THREE gestures'
    }
    if any(errors):
        print "\n".join([errors[x] for x in errors if x == True])
        gestures = get_valid_gesture_list()
    return gestures

def get_valid_gesture(gesture_list):
    """Prompts the user to choose a valid gesture."""
    g = raw_input("Choose a gesture! Input 'random' for a random gesture. ").lower()
    if g == "random":
        g = get_random(gesture_list)
        print "\nYour random gesture is %s!" % (g.upper())
        return g
    elif g not in gesture_list:
        print "Please pick a valid gesture."
        g = get_valid_gesture(gesture_list)
    return g

def get_random(gesture_list):
    """Returns a random gesture."""
    return random.choice(gesture_list)

def get_combos(gesture_list):
    """Returns a sorted list of combination pairs given a list of valid gestures."""
    combos = []
    for g in gesture_list:
        others = list(gesture_list); others.remove(g) #list of unique gestures so this is ok
        g_combos = [ tuple(sorted((g, other))) for other in others ]
        combos.extend(g_combos)
    return sorted(list(set(combos))) # sorted list of tuples.

def get_rules(gesture_list, combos):
    """
    Uses a list of combination pairs to assign win/losses to each gesture.
    Each key of rulebook is a unique gesture, which corresponds to a list of the
    gestures it beats."""
    rulebook = {g:[] for g in gesture_list}
    for i in range(len(combos)):
        c = combos[i]
        if i % 2 == 0:
            rulebook[c[0]].append(c[1])
        else:
            rulebook[c[1]].append(c[0])
    return rulebook

def print_rules(rulebook, gesture_list):
    print("\nWelcome to this game of %s!!!" % ('-'.join(gesture_list)))
    print "\n***RULES OF THE GAME***"
    death_words = random.sample(fun_death_words, len(gesture_list))
    for i in range(len(gesture_list)):
        gesture = gesture_list[i]
        beaten = [beat for beat in rulebook[gesture]]
        print "%s %s %s" % (gesture.upper(), death_words[i],
                            format_string(beaten))
    print "\n"

def format_string(string_list):
    # returns string formatted as "x", "x and y" or "x, y and z"
    if len(string_list) == 1:
        return "%s." % (string_list[0])
    first = ", ".join(string_list[:-1])
    return "%s and %s." % (first, string_list[-1])
    
def beats(gesture1, gesture2, rules):
    return gesture2.lower() in rules[gesture1.lower()]


### ---- Putting it all together ---- ###
    
def run_recur(gestures, rules):
    
    # Gets needed & valid gestures
    you = get_valid_gesture(gestures)
    comp = get_random(gestures)
    print "Computer's random gesture is %s" % (comp.upper())

    # Returns the winning conditions
    if you.lower() == comp.lower():
        print '\nGame is a TIE!'
    elif beats(you, comp, rules):
        print '\nYOU WIN!'
    else:
        print '\nCOMPUTER WINS!'
    
    if raw_input("Try again? :) ").lower() in ['yes','yup','y','yes!','sure','yeah','aye','yea','ok','k','okay','yes please','okey dokey','by all means','oak nuggins','roger','mhmm','mhm','yuppers','shrug','shrugz','¯\_(ツ)_/¯','peter thiel consumes the blood of the young in a dark gamble to escape from death']:
        print "Yay!"
        run_recur(gestures, rules)
    else:
        print "Ok - thanks for playing!"

def run():
    # Prints welcome messages
    print "Thanks for trying out this 'rock-paper-scissors' inspired game!"
    name = raw_input("What's your name? "); print "\nHi %s!" % (name)
    print "Please input an odd list of at least 3 different gestures to convert into a game."

    # Defines gestures and prints rules
    gesture_list = get_valid_gesture_list()
    rulebook = get_rules(gesture_list, get_combos(gesture_list))
    print_rules(rulebook, gesture_list)
    
    run_recur(gesture_list, rulebook)

### ---- End functions ---- ###

run()
