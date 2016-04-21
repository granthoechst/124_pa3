import math
import heapq
import sys

if (len(sys.argv) != 2):
	print("Usage: python karmarkarkarp.py [INPUT FILE]")
	exit()

input_numbers = open(sys.argv[1], 'r')

nums = []

for line in input_numbers:
	for number in line.split():
		nums.append(-int(number))

heapq.heapify(nums)

def karmarkar_karp(heap):
	while(len(heap) != 1):
		largest = heapq.heappop(heap)
		sec_largest = heapq.heappop(heap)
		heapq.heappush(heap, (largest - sec_largest))
	return heap[0]


print(-karmarkar_karp(nums))