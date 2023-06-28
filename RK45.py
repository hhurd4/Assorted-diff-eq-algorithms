# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:35:40 2023

@author: Perry
"""

import numpy as np

def RK4SS(fun, dt, t0, y0):
    f1 = fun( t0 , y0 )
    f2 = fun( t0 + (dt/2) , y0 + (dt/2) * f1 )
    f3 = fun( t0 + (dt/2) , y0 + (dt/2) * f2 )
    f4 = fun( t0 + dt , y0 + dt * f3 )
    ynext = y0 + (dt/6) * (f1 + 2 * f2 + 2 * f3 + f4)
    return ynext

def integrator(t0, tf, step, fun, y0):
    t0=t0
    y0=y0
    dt = step
    time_pts = int( (tf-t0)/step )
    y = np.zeros((len(y0) , time_pts))
    y[:,0] = y0
    t = np.linspace(t0, tf, time_pts)
    yin = y0
    for i in range(time_pts - 1):
        yout = RK4SS(fun,dt,t[i],yin)
        y[:, i + 1] = yout
        yin = yout
        
    return y,t

