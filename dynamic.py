#!/usr/bin/env python

from graphics import plotting

# Data for plotting
range = range(10)
x = 0.1
y1 = []
for i in range:
    x = x*x+1.0
    y1.append(x)
x = 1.0
y2 = []
for i in range:
    x = x*x+1.0
    y2.append(x)
x = 10.0
y3 = []
for i in range:
    x = x*x+1.0
    y3.append(x)

plotting(y1,y2,y3)
