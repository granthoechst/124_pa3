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

# begin PP repeated random------------------------------------------------------
def pp_rep_rand(numbers):
    total = sys.maxint
    for j in range(0, 25000):
        temp_total = karmarkar_karp(apply_pp(gen_pp_arr(), numbers))
        if(temp_total < total):
            total = temp_total
    return total

print "%i" % pp_rep_rand(nums)
# end PP repeated random--------------------------------------------------------