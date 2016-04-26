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

# end karmarkar karp------------------------------------------------------------

# begin PP simulated annealing--------------------------------------------------
def pp_sa(numbers):
    curr_pp_arr = gen_pp_arr()
    curr_sa = karmarkar_karp(apply_pp(curr_pp_arr, numbers))
    for j in range(0,25000):
        switch_index = np.random.random_integers(0,99)
        temp_pp_arr = list(curr_pp_arr)
        switch_content = np.random.random_integers(1,100)
        while (temp_pp_arr[switch_index][1] == switch_content):
            switch_content = np.random.random_integers(1,100)
        temp_pp_arr[switch_index] = (switch_index, switch_content)
        temp_sa = karmarkar_karp(apply_pp(temp_pp_arr, numbers))
        if (temp_sa < curr_sa):
            curr_sa = temp_sa
            curr_pp_arr = temp_pp_arr
        elif (random.random() < (math.exp(-((temp_sa-curr_sa)/t_iter(j))))):
            curr_pp_arr = temp_pp_arr
    return curr_sa

print "%i" % pp_sa(nums)
# end PP simulated annealing----------------------------------------------------
