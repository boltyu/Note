import numpy as np
import scipy as sp
'''
a = np.array(([1,3,4],[4,5,6],[33,3,5],(515,3,1)))
a.shape = 2,6
print(a)
'''
'''
s = "abcdefgh"
d = np.fromstring(s,dtype=np.int16)
print(d)
'''

def func5(i,j):
    return i*10 + j
ar = np.fromfunction(func5,(6,6))
print(ar[1,2:])