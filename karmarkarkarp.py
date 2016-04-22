import math
import heapq
import sys
import numpy as np
import random

if (len(sys.argv) != 2):
	print("Usage: python karmarkarkarp.py [INPUT FILE]")
	exit()

input_numbers = open(sys.argv[1], 'r')

nums = []

for line in input_numbers:
	for number in line.split():
		nums.append(-int(number))

kk_nums = list(nums)

def gen_plus_min():
    plus_min_list = []
    for i in range(0,100):
        x = np.random.random_integers(0,1)
        if x == 0:
            plus_min_list.append(-1)
        else:
            plus_min_list.append(1)
    return plus_min_list

def gen_pp_arr():
    pp_arr = []
    for i in range(0,100):
        pp_arr.append((i, np.random.random_integers(1,100)))
    return pp_arr

def apply_pp(pp_arr, numbers):
    copy_numbers = list(numbers)
    sorted_pp_arr = sorted(pp_arr, key=lambda x: x[1])
    for i in range(0,99):
        if(sorted_pp_arr[i][1] == sorted_pp_arr[i+1][1]):
            copy_numbers[sorted_pp_arr[i + 1][0]] += copy_numbers[sorted_pp_arr[i][0]]
            copy_numbers[sorted_pp_arr[i][0]] = 0
    return copy_numbers

def residue_calc(array, numbers):
    temp_total = 0
    for i in range(0,100):
            temp_total += (array[i] * numbers[i])
    return abs(temp_total)

def t_iter(n):
    return (10**10)*(0.8)**(n/300)

# begin karmarkar karp----------------------------------------------------------
# heapq.heapify(kk_nums)

def karmarkar_karp(heap):
    heapq.heapify(heap)
    while(len(heap) != 1):
        largest = heapq.heappop(heap)
        sec_largest = heapq.heappop(heap)
        heapq.heappush(heap, (largest - sec_largest))
    return -heap[0]


print ("The Karmarkar Karp value is: %i") % karmarkar_karp(kk_nums)
# end karmarkar karp------------------------------------------------------------

# begin RANDOM repeated random--------------------------------------------------
def rand_rep_rand(numbers):
    total = sys.maxint
    for j in range(0, 25000):
        plus_min = gen_plus_min()
        temp_total = residue_calc(plus_min, numbers)
        if(temp_total < total):
            total = temp_total
    return total

print "The RANDOM repeated random value is: %i." % rand_rep_rand(nums)
# end RANDOM repeated random ---------------------------------------------------


# begin PP repeated random------------------------------------------------------
def pp_rep_rand(numbers):
    total = sys.maxint
    for j in range(0, 25000):
        temp_total = karmarkar_karp(apply_pp(gen_pp_arr(), numbers))
        if(temp_total < total):
            total = temp_total
    return total

print "The PP repeated random value is: %i." % pp_rep_rand(nums)
# end PP repeated random--------------------------------------------------------


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

print "The RANDOM hill climbing value is: %i." % rand_hc(nums)
# end RANDOM hill climbing------------------------------------------------------


# begin PP hill climbing--------------------------------------------------------

# end PP hill climbing----------------------------------------------------------


# begin RANDOM simulated annealing----------------------------------------------
def rand_sa(numbers):
    plus_min_sa = gen_plus_min()
    total_sa = residue_calc(plus_min_sa, numbers)
    for j in range(0,25000):
        switch1 = np.random.random_integers(0,99)
        switch2 = np.random.random_integers(0,99)
        temp_plus_min = list(plus_min_sa)
        temp_plus_min[switch1] = -1 * temp_plus_min[switch1]
        if (np.random.random_integers(0,1) == 0):
            temp_plus_min[switch2] = -1 * temp_plus_min[switch2]
        temp_res = residue_calc(temp_plus_min, numbers)
        if (temp_res < total_sa or random.random() < (math.exp(-((temp_res-total_sa)/t_iter(j))))):
            total_sa = temp_res
            plus_min_sa = temp_plus_min
    return total_sa

print "The RANDOM simulated annealing value is: %i." % rand_sa(nums)
# end RANDOM simulated annealing------------------------------------------------


# begin PP simulated annealing--------------------------------------------------

# end PP simulated annealing----------------------------------------------------


