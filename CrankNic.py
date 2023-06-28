#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:31:17 2023

@author: howardhurd
"""

import numpy as np
from numba import jit
from timeit import default_timer as time
import matplotlib.pyplot as plt

start = time()

def cranky(B, sigma, init, t_range, x_range, dx, dt, fun = None):
    #setting number of grid points
    x_min, x_max = x_range
    xpoints = int((x_max - x_min) / dx ) + 1
    t_min, t_max = t_range
    tpoints = int((t_max - t_min) / dt ) + 1
    
    #initializing matrices and right side vector
    
    A_upper_diag = np.zeros(xpoints -1, dtype = np.complex128)
    A_middle_diag = np.zeros(xpoints, dtype = np.complex128)
    A_lower_diag = np.zeros(xpoints - 1, dtype = np.complex128)
    
    if fun == None:
        vec = np.zeros(xpoints, dtype = np.complex128)
    else:
        vec = fun(np.linspace(x_min,x_max,dx),0)
        rhs = np.dot(B,vec)
        
        
    
    
    
            
#stopping run timer
end = time()

#calculating run time and converting to hr/m/s
runtime = end - start
mins, sec  = divmod(runtime,60)
hours, mins = divmod(mins,60)
print('Runtime: ' + str(hours) + ' Hours ' + str(mins) + ' Minutes ' + 
      str(sec) + ' Seconds')