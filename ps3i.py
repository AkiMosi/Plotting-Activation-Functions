# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:30:11 2019

@author: 17pd04
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math

#x=list(np.arange(1,101,1))
#y=[]
#for i in range(100):
#    y.append(rnd.randint(1,10))
#xy=[]
#sumxy=[0]
#for i in range(len(x)):
#    xy.append(x[i]*y[i])
#    sumxy.append(x[i]*y[i]+sumxy[i])
#sumxy=sumxy[1:]
#threshold = int(input("Enter the threshold : "))
#for i in range(len(x)):
#    if(sumxy[i]<threshold):
#        sumxy[i]=0
#plt.plot(x,sumxy)

threshold=5
xrange=50
x=list(np.arange(1,xrange+1,1))
y=[]
for i in range(threshold):
    y.append(0)
for i in range(threshold,xrange):
    y.append(1)
plt.subplot(3,2,1)
plt.title("Threshold")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)

for i in range(xrange):
    y[i]=1/(1+np.exp(-x[i]))
plt.subplot(3,2,2)
plt.title("Sigmoid")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)

for i in range(xrange):
    y[i]=(np.exp(x[i])-np.exp(-x[i]))/(np.exp(x[i])+np.exp(-x[i]))
plt.subplot(3,2,3)
plt.title("Tan h")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)

x=list(np.arange(-(xrange)/2,xrange/2,1))
y=[]
for i in range(xrange):
    y.append(np.max([0,x[i]]))
plt.subplot(3,2,4)
plt.title("Re LU")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)

x=list(np.arange(-(xrange)/2,xrange/2,1))
y=[]
a=4
for i in range(xrange):
    y.append(np.max([x[i],a*x[i]]))
plt.subplot(3,2,4)
plt.title("Re LU")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y)




