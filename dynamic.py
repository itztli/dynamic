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

def plotting(y1,title,filename):
    fig, ax = plt.subplots()
    ax.plot(y1,label='x=0.1')
    #ax.plot(y2,label='x=1.0')
    #ax.plot(y3,label='x=10.0')
    ax.set_yscale('log')
    ax.set(xlabel='i', ylabel='$x_i$',
           title=title)
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig(filename)
    #plt.show()

def dynamic_system(formulae_str,a0,b0,n0,x0,N):
    x,a,b,n = symbols("x a b n")
    print(a0,b0,n0,x0,N)
    y = sympify(formulae_str)
    y = y.subs(a,a0)
    y = y.subs(b,b0)
    y = y.subs(n,n0)

    print(y)
    
    #yprime = y.diff(x)
    f=lambdify(x,y,"numpy")

    # Data for plotting
    iterations = range(N)
    z = x0
    y1 = []
    for i in iterations:
        z = f(z)
        y1.append(z)
        
    return y1
    
    
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
x0=a0=b0=n0=1.0
N=5

n = len(sys.argv)

for i in range(n):
    if  '-a' in sys.argv[i]:
        #file_flag=True
        a0=float(sys.argv[i+1])
    if  '-b' in sys.argv[i]:
        #file_flag=True
        b0=float(sys.argv[i+1])
    if  '-n' in sys.argv[i]:
        #file_flag=True
        n0=float(sys.argv[i+1])
    if  '-x0' in sys.argv[i]:
        #file_flag=True
        x0=float(sys.argv[i+1])
    if  '-i' in sys.argv[i]:
        #file_flag=True
        N=int(sys.argv[i+1])
        

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


y1 = dynamic_system(formulae_str,a0,b0,n0,x0,N)

filename=formulae_str+"_a"+str(a0)+"_b"+str(b0)+"_n"+str(n0)+"_x0"+str(x0)+"_i"+str(N)+".png"
plotting(y1,formulae_str,filename)
