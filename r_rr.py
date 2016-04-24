import math
import heapq
import sys
import numpy as np
import random

if (len(sys.argv) != 2):
	print("Usage: python r_rr.py [INPUT FILE]")
	exit()

input_numbers = open(sys.argv[1], 'r')

nums = []

for line in input_numbers:
	for number in line.split():
		nums.append(-int(number))

def gen_plus_min():
    plus_min_list = []
    for i in range(0,100):
        x = np.random.random_integers(0,1)
        if x == 0:
            plus_min_list.append(-1)
        else:
            plus_min_list.append(1)
    return plus_min_list

def residue_calc(array, numbers):
    temp_total = 0
    for i in range(0,100):
            temp_total += (array[i] * numbers[i])
    return abs(temp_total)

def rand_rep_rand(numbers):
    total = sys.maxint
    for j in range(0, 25000):
        plus_min = gen_plus_min()
        temp_total = residue_calc(plus_min, numbers)
        if(temp_total < total):
            total = temp_total
    return total

print "%i" % rand_rep_rand(nums)