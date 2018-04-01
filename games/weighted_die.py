# filename: weighted_die.py
# desc: script written a long time ago to simulate a weighted die
# date: 2017?
# author: Angelina Li

import random
import re

def weighted_die(number_weight_tuples, precision_factor):
	"""Given a list of tuples of all numbers you want in order and a list of their
	relative weights (will be rounded to nearest integer numbers), returns a weighted
	random no. Tuples have structure (num, weight)
	Precision: how much to times each weight to before rounding."""
	num_tuples = rounded_tuples(number_weight_tuples, precision_factor)
	number_pool = []
	for tup in num_tuples:
		numbers = [tup[0] for n in range(tup[1])]
		number_pool.extend(numbers)
	return random.choice(number_pool)

def rounded_tuples(number_weight_tuples, precision_factor):
	return map(lambda num_wgt_tup: (num_wgt_tup[0],int(precision_factor*num_wgt_tup[1])), number_weight_tuples)

def gen_tuples():
	"""By convention, all numbers on a die start out with 1 weight, and you can
	choose to weight them further."""
	num_tuples = [(num, 1) for num in range(1,7)]
	weighting = True
	
	while weighting:
		weight = raw_input("To weight a number, input the number you want to weight and how much to weight it in the format 'num, weight' (e.g. '3, 9'). \nAll numbers start with a weight of 1. \nTo stop weighting, enter `quit'. ")
		weight = re.sub("'", "", weight).lower()
		if weight == "quit":
			weighting = False
		else:
			num, weight = [int(x) for x in weight.split(",")]
			num_tuples[num-1][1] = weight

	return num_tuples

def run():
	print "Welcome to the weighted die. First we'll assign weights."
	number_weight_tuples = gen_tuples()
	precision_factor = 1

	precision = raw_input("The default precision factor if all your weights are integers, is 1 (which is the most precise possible for integers). \nTo keep the same precision factor, press the enter key. \nTo choose a different precision factor, enter a number here. ")
	if precision != "":
		precision_factor = int(precision)

	print "Random no. is: "
	random_num = weighted_die(number_weight_tuples, precision_factor)
	print random_num
	
	return random_num

def quick_dirty_stats(number_weight_tuples, precision_factor, run_times):
	all_nums = []
	for i in range(run_times):
		all_nums.append(weighted_die(number_weight_tuples, precision_factor))

	stats = [(num, all_nums.count(num)) for num in range(1,7)]
	total = sum([x[1] for x in stats])
	stats = [(x[0], x[1], round(float(x[1])/total, 4)) for x in stats]

	for i in range(len(stats)):
		print "Number {num} appeared {count} times, or {percent}%".format(num=stats[i][0], count=stats[i][1], percent=stats[i][2]*100)

	return stats

num_tuples = [(1,1), (2,1), (3,1), (4,10), (5,1), (6,1)]

quick_dirty_stats(num_tuples, 1, 1000)

