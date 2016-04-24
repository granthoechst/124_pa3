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

# begin karmarkar karp----------------------------------------------------------
# heapq.heapify(kk_nums)

def karmarkar_karp(heap):
    heapq.heapify(heap)
    while(len(heap) != 1):
        largest = heapq.heappop(heap)
        sec_largest = heapq.heappop(heap)
        heapq.heappush(heap, (largest - sec_largest))
    return -heap[0]


print ("%i") % karmarkar_karp(kk_nums)
# end karmarkar karp------------------------------------------------------------