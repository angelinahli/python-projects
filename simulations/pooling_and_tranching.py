"""
ECON202 PS05 Q3
A simple model demonstrating the concepts of pooling and tranching financial
instruments.

Model parameters:
* Allows for n number of tranches;
* No interest; 
* Base instrument pays off in 1 year.

Date: 3/22/17
Writen by: Angelina Li
"""

import random
import numpy

def base_instrument(default, payoff):
    """default is the percentage default risk.
    payoff is the amount of money each instrument pays.
    """
    risk = random.uniform(0,1) # randint between 0 and 100
    if risk <= default:
        return 0
    else:
        return payoff

def pool(psize, default, payoff):
    """psize is the # of instruments in each pool.
    """
    pl = 0  # pl is an accumulator returning total rev in pool.
    for i in range(psize):  # generates psize iid instruments.
        pl += base_instrument(default,payoff)
    return pl

def tranche(tshares, psize, default, payoff):
    """tshares is a list of the ratios of the pot that each tranche gets. 
    e.g. [20, 60, 20] means 1st tranche holders divide up 20% of the shares, 
    2nd tranche holders divide up next 60%, etc.
    """
    tshares = make_valid_shares(tshares)
    total = psize*payoff
    pl = pool(psize,default,payoff)
    rev = []
    
    for share in tshares:
        if pl >= share*total:
            rev.append(payoff)
            pl -= share*total
        elif pl == 0.0:
            rev.append(0)
        else:
            rev.append(pl/float(share*psize))
            pl = 0.0
    return rev

def make_valid_shares(shares):
    """takes in a list of relative shares, e.g. [1,4,2] and returns a list
    of percentages.
    """
    total = sum(int(i) for i in shares)
    return [float(i)/total for i in shares]

def one_pt_mc(nsim, tshares, psize, default, payoff, cor):
    """nsim (an int) is the number of times to run the simulation.
    cor is the percentage risk of correlated defaults (in which case everyone
    defaults).
    """
    tranches = [ [] for t in tshares]
    for i in range(nsim):
        risk = random.uniform(0,1)
        if risk <= cor:
            for i in range(len(tshares)):
                tranches[i].append(0)
        else:
            sim = tranche(tshares,psize,default,payoff)
            for i in range(len(tshares)):
                tranches[i].append(sim[i])
    
    print """\nMonte Carlo Simulation: {n_number} n, {t_shares} tranche ratios,
    {p_size} pool size, {default} default ratio, {cor_risk} chance of cor risk 
    and payoffs of {payoff} per period""".format(
        n_number=nsim, 
        t_shares=tshares, 
        p_size=psize,
        default=default,
        cor_risk=cor,
        payoff=payoff)

    # uses numpy to calculate mean and stdevs, and prints these.
    print "means: " + ", ".join([str(numpy.mean(i)) for i in tranches])
    print "stdevs: " + ", ".join([str(numpy.std(i)) for i in tranches])

one_pt_mc(10000,[1,1],100,0.25,1000,0)
one_pt_mc(10000,[1,1],100,1.0/6,1000,0.1)

