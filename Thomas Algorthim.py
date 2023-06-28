# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:48:07 2023

@author: Perry Hurd

Thomas Algorithm (Tridiagonal matrix algorithm) using 1D arrays for memory 
efficiency
"""

import numpy as np
from numba import jit 
from timeit import default_timer as time

start = time()


def tridag_solver(upper, main, lower, vec):
    n = len(main)
    x = np.zeros(n, dtype = np.complex128)
    #Arrays for tracking coefficients
    c_prime = np.zeros(n-1, dtype = np.complex128)
    d_prime = np.zeros(n, dtype = np.complex128)
    
    #Calculate inital c' and d' coeffecients (i=0)
    c_prime[0] = upper[0] / main[0]
    d_prime[0] = vec[0] / main[0]
    
    #calculating all variables except final d'
    for i in range(1,n-1):
        c_prime[i] = upper [i] / (main[i] - lower[i] * c_prime[i-1])
        d_prime[i] = (vec[i] - lower[i] * d_prime[i-1]) / (main[i] - lower[i] * c_prime[i-1])
    
    #final d' variable
    d_prime[-1] = (vec[-1] - lower[-1] * d_prime[-2]) / (main[-1] - lower[-1] * c_prime[-1]) 
    
    #back substituting to solve for new vector
    x[-1] = d_prime[-1]
    
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
        
    return x

end = time()

#calculating run time and converting to hr/m/s
runtime = end - start
mins, sec  = divmod(runtime,60)
hours, mins = divmod(mins,60)
print('Runtime: ' + str(hours) + ' Hours ' + str(mins) + ' Minutes ' + 
      str(sec) + ' Seconds')






