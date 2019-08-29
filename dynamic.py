#!/usr/bin/env python3

#from graphics import plotting
from sympy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys

#./dynamic -f formulae.dat
# USAGE
#./dynamic.py -e a*x^n+b -a 1 10 1  -b 1 5 1 -n 2 2 1 -x0 0.1 1.0 0.1 -i 6
#from readcol import fgetcols

def plotting(fig,ax,y1,title,filename,caption):
    ax.plot(y1,label=caption)
    #ax.plot(y2,label='x=1.0')
    #ax.plot(y3,label='x=10.0')
    ax.set_yscale('log')
    ax.set(xlabel='i', ylabel='$x_i$',
           title=title)
    ax.grid()
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
x1=a1=b1=n1=1.0
dx=da=db=dn=1.0
itera=5
n = len(sys.argv)
Z = 10

#argv[Z++]
#argv[++Z]

for i in range(n):
    if  '-a' in sys.argv[i]:
        #file_flag=True
        i+=1
        a0=float(sys.argv[i])
        i+=1
        a1=float(sys.argv[i])
        i+=1
        da=float(sys.argv[i])

    if  '-b' in sys.argv[i]:
        #file_flag=True
        #b0=float(sys.argv[i+1])
        i+=1
        b0=float(sys.argv[i])
        i+=1
        b1=float(sys.argv[i])
        i+=1
        db=float(sys.argv[i])
        
    if  '-n' in sys.argv[i]:
        #file_flag=True
        #n0=float(sys.argv[i+1])
        i+=1
        n0=float(sys.argv[i])
        i+=1
        n1=float(sys.argv[i])
        i+=1
        dn=float(sys.argv[i])

        
    if  '-x0' in sys.argv[i]:
        #file_flag=True
        #x0=float(sys.argv[i+1])
        i+=1
        x0=float(sys.argv[i])
        i+=1
        x1=float(sys.argv[i])
        i+=1
        dx=float(sys.argv[i])

        
    if  '-i' in sys.argv[i]:
        #file_flag=True
        itera=int(sys.argv[i+1])
        
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


A = np.arange(a0,a1,da)
B = np.arange(b0,b1,db)
N = np.arange(n0,n1,dn)    
X0= np.arange(x0,x1,dx)    
print(A)
print(B)
print(N)
print(X0)

fig, ax = plt.subplots()

for a in A:
    for b in B:
        for n in N:
            for x0 in X0:
                y1 = dynamic_system(formulae_str,a,b,n,x0,itera)
                filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(itera)+"_x0"+str(x0)+"_i"+str(n)+".png"
                caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x0)+" i="+str(itera)
                plotting(fig,ax,y1,formulae_str,filename,caption)

#pylab.legend(loc='upper left')
fig.savefig(filename)
