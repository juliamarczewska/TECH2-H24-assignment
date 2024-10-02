"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(x):

        x = [1, 2, 3, 4, 5]

    number = len(x)
    mean = 0

    
    for value in x:
        mean += value
    mean /= n

    vsum = 0
    
    
    for value in x:
        vsum += (value - mean) ** 2
        
    variance = vsum / number
    standard_deviation = variance ** 0.5
    
    return standard_deviation


result = std_loops([1, 2, 3, 4, 5])
print(f'The standard deviation equals: {result:.10f}') 
 
    
import math
from math import sqrt
def std_builtin(x):

        x = [1, 2, 3, 4, 5]
        mean = sum(x) / len(x)
        variance = sum((xi - mean) ** 2 for xi in x) / len(x) 

        standart_deviation = math.sqrt(variance)

        return standart_deviation
        
result = std_builtin([1, 2, 3, 4, 5])
print(f'The standard deviation equals: {result:.10f}') 
        
        
     
    
