# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:40:55 2020

@author: stian
"""
import numpy as np
import math
from sympy import symbols, diff




def f(u,v):
    return u * v * (u**3 + v**3)*math.sqrt(9*(u**4) + 9*(v**4) + 1)


def g(t):
    return 3*t**2

def flateIntegral():
    u_min = 0
    u_max = 1
    v_min = 0
    v_max = 1
    n = 100
    m = 100
    deltaU = (u_max - u_min)/n
    deltaV = (v_max - v_min)/m
    
    uArray = np.linspace(u_min + deltaU/2, u_max - deltaU/2, n)
    vArray = np.linspace(v_min + deltaV/2, v_max - deltaV/2, m)
    s = 0
    for i in range(1,m):
        for j in range(1,n):
            s = s + f(uArray[j], vArray[i]) * deltaU * deltaV
    print(s)


def linjeIntegral():
    t_min = 0
    t_max = 2
    
    n = 20
    deltaT = (t_max - t_min)/n
    
    t = np.linspace(t_min, t_max,n + 1)
    
    w = 0
    
    for i in range(1,n):
        w = w + ( g(t[i]) + g(t[i + 1]) ) / 2 * deltaT
    print(w)

flateIntegral()
linjeIntegral()