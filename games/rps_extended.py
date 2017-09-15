"""
Rock Paper Scissors Extended Game

This program:
(a) Determines if a gesture is valid based on a list of acceptable functions.
(b) Create a function to generate a random gesture.
(c) Prints out a cute list of rules.
(d) Determine which of two given gestures wins.
(e) Plays a game between two given opponents.
(f) Plays a game between you and the computer.

Date: 2/19/17
Written by: Angelina Li
"""

import random

# You can change the gestures used in this game here.
# Please make sure your list of gestures includes exactly 5 gestures!
g1 = 'Rock'
g2 = 'Paper'
g3 = 'Scissors'
g4 = 'Lizard'
g5 = 'Spock'

hierarchy = {
    g1: [g2, g3],
    g2: [g3, g4],
    g3: [g4, g5],
    g4: [g5, g1],
    g5: [g1, g2] 
}

gesture_list = hierarchy.keys()


fun_death_words = ['beats up','blasts','crushes','demolishes','destroys',
                   'extinguishes','lambasts','pummels','ruins','shatters',
                   'smashes','torpedoes','vaporizes','wrecks']

def is_valid_gesture(gesture_name):
    return gesture_name.lower() in [x.lower() for x in gesture_list]

def random_gesture():
    return random.choice(gesture_list)

def beats(gesture1, gesture2):
    """
    Determines whether gesture1 beats gesture 2. 
    If the gesture is invalid, beats() returns nothing.
    """
    if not(is_valid_gesture(gesture1) and is_valid_gesture(gesture2)):
        return
    else:
        return gesture2 in hierarchy[gesture1]
        
def play_opponent(you,opponent,opp_name):
    if you.lower() == 'random':
        you = random_gesture()
        print 'Your random gesture is ' + you.lower() + '.'
    if is_valid_gesture(you) == False:
        print '\nYour gesture (' + you + ') is INVALID!'
    elif is_valid_gesture(opponent) == False:
        print '\n' + opp_name + '\'s gesture (' + opponent + ') is INVALID!'
    else:
        if you.lower() == opponent.lower():
            print '\nGame is a TIE!'
        elif beats(you, opponent):
            print '\nYOU WIN!'
        else:
            print '\nOPPONENT WINS!'
        
def generate_rules(your_name, opponent_name):
    print("Welcome to this game of %s between %s and %s!!!\n" %
                        ('-'.join(gesture_list).lower(),
                         your_name, opponent_name))
    print "RULES OF THE GAME:"
    for gesture in gesture_list:
        print "%s %s %s and %s" % (gesture, random.choice(fun_death_words),
                                   hierarchy[gesture][0], hierarchy[gesture][1])

def play_computer():
    generate_rules('yourself', 'the computer')
    computer_gesture = random_gesture()
    user_gesture = raw_input("What gesture do you choose? (Enter "+
                             "'random' to generate a random gesture) ")
    print 'The computer chose ' + computer_gesture.lower() + '.'
    return play_opponent(user_gesture,computer_gesture,'Computer')

play_computer()
