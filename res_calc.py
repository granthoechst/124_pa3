import sys

data = open(sys.argv[1], 'r')

data_arr = []

for line in data:
    for number in line.split():
        data_arr.append(number)

def res_calc(arr):
    total_sum = 0
    for i in range(0,50):
        total_sum += float(arr[2*i])
    return total_sum / 50.

print "The random rr average residue is %f." % res_calc(data_arr)

