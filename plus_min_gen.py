import numpy as np
import sys

# usage: python plus_min_gen.py n

plus_min_list = []

def gen_plus_min():
    for i in range(0,100):
        x = np.random.random_integers(0,2)
        if x == 0:
            plus_min_list.append(-1)
        else:
            plus_min_list.append(1)

gen_plus_min()
print plus_min_list
