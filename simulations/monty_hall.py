"""
Monty Hall Simulation
Quick monte carlo simulation of the Monty Hall problem.

Rules:
==> 3 doors, random whether each contains a prize or a dud.
==> One of the doors that has a dud is revealed.
==> You can either switch or you can stick with your door.

Date: 4/12/17
Written by: Angelina Li
"""

import random
import numpy

def prize_generator():
    options = [[0,0,1], [0,1,0], [1,0,0]]
    return random.choice(options)

def prize_choose():
    a, b, c = prize_generator() # a is default the chosen door
    alt = [b, c]
    # or just alt.remove(0) <-- or whatever this fn is
    if b == 0:
        alt.pop(0)
    else:
        alt.pop(1)
    
    return alt[0], a #switch, stay

def choice_sim(n):
    switch = []
    stay = []
    for i in range(n):
        sw, st = prize_choose()
        switch.append(sw)
        stay.append(st)
    return numpy.mean(switch), numpy.mean(stay)

def monty_hall_sim(n):
    sw, st = choice_sim(n)
    print "Choosing to switch wins the prize with probability {}".format(
        str(round(sw, 3)))
    print "Choosing to stay wins the prize with probability {}".format(
        str(round(st, 3)))
