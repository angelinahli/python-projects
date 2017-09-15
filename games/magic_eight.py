"""
Creates a Magic 8 ball the user can interact with
Date: 2/22/17
Written by: Angelina Li
"""

import random
import time

answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely, yes.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

# Welcome
print "*".join(list("MAGIC 8"))
print "\nYou're invited to test out the Magic 8 ball! Ask me a yes/no question and I can generate an answer!"

def another():
    ask = raw_input("\nWould you like to ask me another? Enter Y or N. ")
    if ask.lower() == "y":
        question()
    elif ask.lower() == "n":
        print "\nThanks for playing!"
    else:
        print "\nSorry, I don't understand your answer."
        another()

# Ask me a question
def question():
    q = raw_input("\nWhat question do you have for me today? ")
    print "\nThinking . . ."
    time.sleep(random.randint(1,4))
    print random.choice(answers)
    another()

question()
