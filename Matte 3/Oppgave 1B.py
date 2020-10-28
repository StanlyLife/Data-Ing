# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:50:44 2020

@author: stian
"""
import math
import matplotlib.pyplot as plt
import numpy as np
m = 20
n = m/2

xx = []
yy = []

for t in range(math.ceil(math.pi*20)):
    x = 2*math.cos(t/10)
    y = 2*math.sin(t/10)
    
    xx.append(x)
    yy.append(y)    
    
plt.plot(xx,yy,'-o')
plt.show()
xxt,yyt = np.meshgrid(xx,yy)
plt.plot(xx,yy, marker='.', color = 'r' , linestyle='none')
plt.show()
