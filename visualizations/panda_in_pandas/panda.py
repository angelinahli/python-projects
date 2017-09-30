"""
Visualization of a panda using the pandas hexbin plot.

Methodology:
Create half of a face using shapes, then
flip the face to create a whole panda.
"""

import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
from pandas import DataFrame, Series

def weight(tuples_list, factor):
    new_list = []
    for _ in range(factor):
        new_list += tuples_list
    return new_list

def duplicate(tuples_list):
    """
    Given list of tuples, calculates inverse list of tuples with flipped x
    values and returns all tuples.
    """
    inverted_list = [(-tup[0], tup[1]) for tup in tuples_list if tup[0] != 0]
    return tuples_list + inverted_list

def get_fx(pt1, pt2):
    """Given two points (as tuples), returns tup (a,b) where y = a + bx"""
    x0, y0 = pt1
    x1, y1 = pt2
    b = float(y1 - y0) / float(x1 - x0)
    a = float(y0) - (b * x0)
    return (a, b)

def get_x(y, a, b):
    """Given y, a and b where y = a + bx, returns the nearest integer of x"""
    return int(round( (y-a) / b, 0))

def make_nose():
    """Nose ranges approx. from x in [0, 25] and y in [0, -50]"""
    nose_top = []
    a_top, b_top = get_fx((30, 0), (5, -30))
    for y in xrange(-30, -5):
        nose_top += [(x, y) for x in xrange(0, get_x(y, a_top, b_top) + 1)]

    nose_bottom = []
    a_bot, b_bot = get_fx((5, -30), (30, -50))
    for y in xrange(-46, -31):
        nose_bottom += [(x, y) for x in xrange(0, get_x(y, a_bot, b_bot) + 1)]

    return duplicate(nose_top + nose_bottom)

def make_eyes():
    eye = []
    a_st, b_st = get_fx((30, 45), (30 + 10, 0))
    a_ed, b_ed = get_fx((70, 45), (70 + 15, 0))
    for y in xrange(0, 42):
        x_start = get_x(y, a_st, b_st)
        x_end = get_x(y, a_ed, b_ed) + 1
        eye += [(x, y) for x in xrange(x_start, x_end)]
    return duplicate(eye)

def make_ears():
    ear = []
    x0 = 91
    x1 = x0 + 25
    x2 = x1 + 25

    y0 = 44
    y1 = y0 + 25
    y2 = y1 + 25

    a_st1, b_st1 = get_fx((x0, y1), (x1, y0))
    a_ed1, b_ed1 = get_fx((x1, y1), (x2, y0))
    for y in xrange(y0, y1):
        x_start = get_x(y, a_st1, b_st1)
        x_end = get_x(y, a_ed1, b_ed1)
        ear += [(x, y) for x in xrange(x_start, x_end)]
        ear += [(x, y) for x in xrange(x_end, x2 + 1)]

    a_st2, b_st2 = get_fx((x0, y2), (x1, y1))
    a_ed2, b_ed2 = get_fx((x1, y2), (x2, y1))
    for y in xrange(y1, y2 + 1):
        x_start = get_x(y, a_st2, b_st2)
        x_end = get_x(y, a_ed2, b_ed2)
        ear += [(x, y) for x in xrange(x0, x_start)]
        ear += [(x, y) for x in xrange(x_start, x_end + 1)]

    return duplicate(ear)

def get_face_x_above(y):
    """figured out the geometry using WolframAlpha"""
    return (125.0/73) * sqrt( (-y**2) + (26*y) + 5160 )

def get_face_x_below(y):
    return (125.0/73) * sqrt( (-y**2) + (16*y) + 5160 )

def make_face():
    face = []
    for y in xrange(-60, 13):
        face.append( (get_face_x_below(y), y) )
    for y in xrange(13, 87):
        face.append( (get_face_x_above(y), y) )
    return weight(duplicate(face), 4)

data = make_nose() + make_eyes() + make_ears() + make_face()

panda = DataFrame(data, columns=['x', 'y'])
ax = panda.plot.hexbin(x='x', 
                  y='y', 
                  gridsize=50,
                  colormap='Greys')
fig = ax.get_figure()
fig.savefig('pd_panda.png')