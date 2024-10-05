"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

#using loops function 
def std_loops(x):

    number = len(x)

    total_sum = 0
    
    for value in x:
        total_sum += value
    mean = total_sum / number
 
    vsum = 0
    for value in x:
        vsum += (value - mean) ** 2
    
    variance = vsum / number
    standard_deviation = variance ** 0.5
    
    return standard_deviation

result_loops = std_loops([1, 2, 3, 4, 5])

#using builtin function 
    
import math
from math import sqrt
def std_builtin(x):

        x = [1, 2, 3, 4, 5]
        mean = sum(x) / len(x)
        variance = sum((xi - mean) ** 2 for xi in x) / len(x) 

        standart_deviation = math.sqrt(variance)

        return standart_deviation
        
result_builtin = std_builtin([1, 2, 3, 4, 5])

#using std() from numpy 

import numpy as np

x = np.array([1, 2, 3, 4, 5])

result_numpy = np.std(x)
  

#checking if loops, builtin functions, and std() from numpy calculate the same result

x = [1, 2, 3, 4, 5]


result_loops = std_loops(x)
result_builtin = std_builtin(x)
result_numpy = np.std(x)

print(f'Standard Deviation (loops): {result_loops:.10f}')
print(f'Standard Deviation (builtin): {result_builtin:.10f}')
print(f'Standard Deviation (std() from NumPy): {result_numpy:.10f}')


    
