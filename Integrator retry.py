# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:12:34 2023

@author: hphur
"""

import numpy as np
from timeit import default_timer as time
import matplotlib.pyplot as plt
from numpy import arange as arange

start = time()

#parameters in microns and nanoseconds
pi = np.pi # just easier to type
me = 9.11 * 10 ** -31 #mass of electron in kg
ee = 8.85 * 10 ** -12 # Vacuum Permittivity (doesn't change under unit conversion)
e = 1.6 * 10 ** -19 #Charge of the electron in C
v = 1 #initial velocity in microns/nanosecond
k = -( e**2 ) / (8 * pi * ee) #Coulomb Force prefactor
B = 10**-11 #magnetic field converted from microTesla into scaled units
hbar = 1 #1.05 * 10 ** -43
rho = .7
z0 = -1
# sigma
comp = (hbar/(4*me))
sigma = complex(0, comp)

#defining coulomb force
def coul(x,t):
    val = []
    for arr in x:
        val.append(complex(0,k * 1 / ( np.sqrt( rho ** 2 + ( arr + v * t - z0) ** 2 ))))
    return np.array(val)


# coul force debugging check
'''
trial = coul([0,1,2,3,4,5],0)
print(trial)
'''
#setting paramters of integration
dt = 10 ** -2
N = 10000 #number of grid points
L = float(10)
dx = L/(N-1)
tfinal = 300
tpoints = tfinal / dt
x_grid = np.array([j*dx for j in np.arange(N)])
t_grid = np.array([j*dt for j in np.arange(tpoints)])

#debugging grid check
'''
print(len(x_grid))
print(len(t_grid))
'''

#initial conditions
init = np.array([np.exp(- ((i - 5) ** 2  )/ (.5**2) ) for i in x_grid])

#defining matrices
A_upper_diag = np.array([-sigma * dt / dx ** 2 for i in np.arange(0,  N - 1)])
A_lower_diag = np.array([-sigma * dt / dx ** 2 for i in np.arange(0, N - 1)])

B_upper_diag = np.array([sigma * dt / dx ** 2 for i in np.arange(0, N - 1)])
B_lower_diag = np.array([sigma * dt / dx ** 2 for i in np.arange(0, N - 1)])

#matrix debugging
'''
print(A_upper_diag)
print(A_lower_diag)
print(B_upper_diag)
print(B_lower_diag)
'''

m = True

if m:
    nu = coul(x_grid,0)
    print(nu)

#making time steps, updating coulumb term and recalculating rhs of matrix equation at each time step
rhs = init
for k in range(1):
    nu = coul(x_grid,0)
    #print(nu)
    A_main_diag = np.array([1+ 2 * sigma * dt / dx ** 2] + [1 + 2 * sigma * dt / dx **2 - nu[i] for i in np.arange(0 , N -1)] )
    #print(A_main_diag)
    #print(A_main_diag[0])
    B_main_diag = np.array([-2 * sigma * dt / dx ** 2] + [-2 * sigma * dt / dx ** 2 + nu[i] for i in arange(0 , N-1)])
    #print(B_main_diag)
    #print(B_main_diag[0])


plt.figure()
plt.plot(x_grid,init)
plt.show()
#debugging
#print(init)



#stopping run timer
end = time()

#calculating run time and converting to hr/m/s
runtime = end - start
mins, sec  = divmod(runtime,60)
hours, mins = divmod(mins,60)
print('Runtime: ' + str(hours) + ' Hours ' + str(mins) + ' Minutes ' + 
      str(sec) + ' Seconds')


