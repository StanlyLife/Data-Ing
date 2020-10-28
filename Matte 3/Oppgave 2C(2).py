# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:54:39 2020

@author: stian
"""
import math

a = 0
b = 2
c = 0
d = 1

m = 2

deltaX = (b-a)/m
deltaY = (d-c)/m
deltaA = deltaX*deltaY

rs = 0

def get_corners(m):
    bottomLeft = [b/m,d/m]
    bottomRight = [b,d/m]
    
    topLeft = [b/m,d]
    topRight = [b,d]
    
    return [bottomLeft,bottomRight,topLeft,topRight]


def get_corners2(m):
    corners = []
    for i in range(0,m):
        for j in range(0,m):
            x = b/(m/(m-i))
            y = d/(m/(m-j))
            corner = [x,y]
            corners.append(corner)
    return corners
            
            
    

#def f(x,y):
#    return 1/(1+pow(x,2)*y)
def f(x,y):
    return x*pow(math.e,-x*y)


corners = get_corners2(m);
for i in range(0,len(corners)):
    rs += f(corners[i][0],corners[i][1])

volume = rs * deltaA
print(len(corners))
print(volume)






