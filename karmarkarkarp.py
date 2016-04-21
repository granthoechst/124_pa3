import math
import heapq
import sys
import numpy as np

if (len(sys.argv) != 2):
	print("Usage: python karmarkarkarp.py [INPUT FILE]")
	exit()

input_numbers = open(sys.argv[1], 'r')

nums = []

for line in input_numbers:
	for number in line.split():
		nums.append(-int(number))

kk_nums = nums

# beginning the repeated random:

def gen_plus_min():
    plus_min_list = []
    for i in range(0,100):
        x = np.random.random_integers(0,2)
        if x == 0:
            plus_min_list.append(-1)
        else:
            plus_min_list.append(1)
    return plus_min_list

def rep_rand(numbers):
    total = sys.maxint
    for j in range(0, 25000):
        temp_total = 0
        plus_min = gen_plus_min()
        for i in range(0,100):
            temp_total += (plus_min[i] * numbers[i])
        if(abs(temp_total) < total):
            total = abs(temp_total)
    return total

print "The repeated random low is: %i." % rep_rand(nums)

heapq.heapify(kk_nums)

def karmarkar_karp(heap):
	while(len(heap) != 1):
		largest = heapq.heappop(heap)
		sec_largest = heapq.heappop(heap)
		heapq.heappush(heap, (largest - sec_largest))
	return heap[0]


print(-karmarkar_karp(kk_nums))

