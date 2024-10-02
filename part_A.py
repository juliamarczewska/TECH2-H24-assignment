"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(x):

        x = [1, 2, 3, 4, 5]

    n = len(x)
    mean = 0

    
    for value in x:
        mean += value
    mean /= n

    vsum = 0
    
    
    for value in x:
        vsum += (value - mean) ** 2
        
    variance = vsum / n
    standard_deviation = variance ** 0.5
    
    return standard_deviation


result = std_loops([1, 2, 3, 4, 5])
print(f'The standard deviation equals {result:.10f}') 
 
    

    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
