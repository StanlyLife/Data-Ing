# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:21:32 2020

@author: stian
"""
#Funksjon
def f(x):
    return (x**3)+(x**2)-x

def riemannSum(a, b, numberOfRectangles):
    intervalLength = float(b - a)
    deltaX = intervalLength / numberOfRectangles
    rs = 0

    for i in range(0, numberOfRectangles):
        test = a + i * deltaX
        rs += f(test) * deltaX

    return rs

print(riemannSum(0,2.5,100000))

