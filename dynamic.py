#!/usr/bin/env python3

#from graphics import plotting
from sympy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import random as rn

#./dynamic -f formulae.dat
# USAGE
#./dynamic.py -e a*x^n+b -a 1 10 1  -b 1 5 1 -n 2 2 1 -x0 0.1 1.0 0.1 -i 6
#from readcol import fgetcols

def plotting(fig,ax,time,y1,title,filename,caption):
    ax.plot(time,y1,label=caption)
    #ax.plot(y2,label='x=1.0')
    #ax.plot(y3,label='x=10.0')
    #ax.set_yscale('log')
    ax.set(xlabel='hours', ylabel='g',
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
    time = []
    mitosis=3.0#h
    dtime=0.0
    weight=1e-12#g
    
    for i in iterations:
        time.append(dtime)
        dtime+=mitosis
        z = f(z)
        y1.append(z*weight)
        
    return time,y1


def function_system(formulae_str,a0,b0,n0,x0,noise_flag,noise):
    x,a,b,n = symbols("x a b n")
    print(a0,b0,n0,x0)
    y = sympify(formulae_str)
    y = y.subs(a,a0)
    y = y.subs(b,b0)
    y = y.subs(n,n0)
    print(y)
    f=lambdify(x,y,"numpy")
    y1 = f(x0)
    #print(y1)

    if noise_flag:
        #for i in range(len(y1)):
        for i, value in enumerate(y1):    
            y1[i]= value + (rn.random()-0.5)*2.0*noise
    
    return x0,y1

def plot_histo(fig_histo,ax_histo,f,g,bind):
    data_histo=[]
    #for i, (v1,v2) in enumerate(zip(f,g)):
    for i, value in enumerate(f):
        data_histo.append(f[i]-g[i])
    ax_histo.hist(data_histo,bind)
    plt.show()

def plot_observations(fig,ax,obs_z,obs_d,obs_d_err):
    ax.errorbar(obs_z, obs_d, yerr=obs_d_err, fmt='o')
    
#formulae='x^2+1.0'
#def f(x):
#    return x*x+1.0

#formulae= fgetcols('formulae.dat')
#print(formulae)
#formulae_str= (formulae[0])[0]
#print(formulae_str)

file_flag = False
equation_flag = False
dynamic_flag=False
histo_flag=False
obs_flag=False
obs_filename=''
bind=1
formulae_str = 'x'
x0=a0=b0=n0=1.0
x1=a1=b1=n1=1.0
dx=da=db=dn=1.0
itera=5
n = len(sys.argv)
noise=0.0
#Z = 10
obs_z=[]
obs_d=[]
obs_d_err=[]


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

    if  '-dynamic' in sys.argv[i]:
        dynamic_flag=True

    if '-random' in sys.argv[i]:
        noise_flag=True
        i+=1
        noise=float(sys.argv[i])

    if '-histo' in sys.argv[i]:
        histo_flag=True
        i+=1
        bind=int(sys.argv[i])

    if  '-o' in sys.argv[i]:
        obs_flag=True
        i+=1
        obs_filename=sys.argv[i]

if file_flag:
    with open(filename) as f:
        formulae=f.readlines()
        formulae_str=formulae[0]
        print('Using archive mode  with '+formulae_str)

if equation_flag:
    print('Using equation mode with '+formulae_str)

if dynamic_flag:
    print('Evaluating dynamic system')

if noise_flag:
    print('Inserting noise to functions: '+str(noise))

if histo_flag:
    print('Histogram activated: '+str(bind))

if obs_flag:
    print('Observation archive activated: '+obs_filename)
    
    with open(obs_filename) as f:
        data=f.readlines()
        for line in data:
            if line[0] != '#':
                z,d,d_err = line.split()
                obs_z.append(float(z))
                obs_d.append(float(d))
                obs_d_err.append(float(d_err))

        #formulae_str=formulae[0]
        #print('Using archive mode  with '+formulae_str)
    
A = np.arange(a0,a1,da)
B = np.arange(b0,b1,db)
N = np.arange(n0,n1,dn)    
X0= np.arange(x0,x1,dx)    
print(A)
print(B)
print(N)
print(X0)




fig, ax = plt.subplots()
if histo_flag:
    fig_histo, ax_histo = plt.subplots()


for a in A:
    for b in B:
        for n in N:
            if dynamic_flag:
                for x0 in X0:
                    time, y1 = dynamic_system(formulae_str,a,b,n,x0,itera)
                    filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(itera)+"_x0"+str(x0)+"_i"+str(n)+".png"
                    caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x0)+" i="+str(itera)
                    plotting(fig,ax,time,y1,formulae_str,filename,caption)
            else:
                time, g = function_system(formulae_str,a,b,n,X0,noise_flag,noise)
                time, f = function_system(formulae_str,a,b,n,X0,False,0)

                filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(itera)+"_x0"+str(x0)+"_i"+str(n)+".png"
                caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x0)+" i="+str(itera)
                plotting(fig,ax,time,f,formulae_str,filename,caption)
                plotting(fig,ax,time,g,formulae_str,filename,caption)
                if obs_flag:
                    plot_observations(fig,ax,obs_z,obs_d,obs_d_err)
                if histo_flag:
                    plot_histo(fig_histo,ax_histo,f,g,bind)
                
#pylab.legend(loc='upper left')
plt.show()
fig.savefig(filename)
