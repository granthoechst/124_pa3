import numpy as np
import sys

# usage: python make_nums.py n

def gen_numbers():
    for i in range(0,100):
        print np.random.random_integers(1, 10**12)

gen_numbers()
