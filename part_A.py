"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

#using loops function 

from math import sqrt

def std_loops(x):
    N = len(x)
    mean = sum(x) / N
    sum_squares = sum([(i - mean) ** 2 for i in x])
    variance = sum_squares / N
    return sqrt(variance)
    
#using builtin function 
    
def std_builtin(x):
    N = len(x)
    mean = sum(x) / N
    mean_of_squares = sum([i**2 for i in x]) / N
    variance = mean_of_squares - (mean ** 2)
    return sqrt(variance)
    
#using std() from numpy 

import numpy as np

def std_numpy(x):
    return np.std(x)
    
#checking if loops, builtin functions, and std() from numpy calculate the same result

x = [1, 2, 3, 4, 5]

print("Standard Deviation using loops:", std_loops(x))
print("Standard Deviation using built-in functions:", std_builtin(x))
print("Standard Deviation using NumPy:", std_numpy(x))

    
