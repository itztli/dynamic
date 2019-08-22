#!/usr/bin/env python3

#from graphics import plotting
from sympy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys

#./dynamic -f formulae.dat

#from readcol import fgetcols

def plotting(y1,y2,y3,title):
    fig, ax = plt.subplots()
    ax.plot(y1,label='x=0.1')
    ax.plot(y2,label='x=1.0')
    ax.plot(y3,label='x=10.0')
    ax.set_yscale('log')
    ax.set(xlabel='i', ylabel='$x_i$',
           title=title)
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig(title+'.png')
    #plt.show()

#formulae='x^2+1.0'
#def f(x):
#    return x*x+1.0

#formulae= fgetcols('formulae.dat')
#print(formulae)
#formulae_str= (formulae[0])[0]
#print(formulae_str)

file_flag = False
equation_flag = False
formulae_str = 'x'

n = len(sys.argv)

for i in range(n):
    if  '-f' in sys.argv[i]:
        file_flag=True
        filename=sys.argv[i+1]

    if  '-e' in sys.argv[i]:
        equation_flag=True
        formulae_str=sys.argv[i+1]

        
if file_flag:
    with open(filename) as f:
        formulae=f.readlines()
        formulae_str=formulae[0]
        print('Using archive mode  with '+formulae_str)

if equation_flag:
    print('Using equation mode with '+formulae_str)
    
x = Symbol("x")
y = sympify(formulae_str)
#yprime = y.diff(x)
f=lambdify(x,y,"numpy")

# Data for plotting
range = range(7)
z = 0.1
y1 = []
for i in range:
    z = f(z)
    y1.append(z)
z = 1.0
y2 = []
for i in range:
    z = f(z)
    y2.append(z)
z = 10.0
y3 = []
for i in range:
    z = f(z)
    y3.append(z)

plotting(y1,y2,y3,formulae_str)
