import math
import heapq
import sys
import numpy as np
import random

if (len(sys.argv) != 2):
	print("Usage: python kk.py [INPUT FILE]")
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

# begin RANDOM hill climbing----------------------------------------------------
def rand_hc(numbers):
    plus_min_hc = gen_plus_min()
    total_hc = residue_calc(plus_min_hc, numbers)
    for j in range(0,25000):
        switch1 = np.random.random_integers(0,99)
        switch2 = np.random.random_integers(0,99)
        temp_plus_min = list(plus_min_hc)
        temp_plus_min[switch1] = -1 * temp_plus_min[switch1]
        if (np.random.random_integers(0,1) == 0):
            temp_plus_min[switch2] = -1 * temp_plus_min[switch2]
        temp_res = residue_calc(temp_plus_min, numbers)
        if (temp_res < total_hc):
            total_hc = temp_res
            plus_min_hc = temp_plus_min
    return total_hc

print "%i" % rand_hc(nums)
# end RANDOM hill climbing------------------------------------------------------