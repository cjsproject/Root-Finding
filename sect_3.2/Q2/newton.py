
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, exp

"""
Newton's Rootfinding Method

"""
# error tolerance
epsilon = 1.0e-6

x = np.linspace(0.0, 2.0, num=100000)

# simply defining each function 1-7
def f1(t):
  return pow(t, 3) - pow(t, 2) - t - 1

def f2(t):
  return 1 + (0.3*cos(t)) - t 

def f3(t):
  return 0.5 + sin(t) - cos(t)

def f4(t):
  return exp(-t)-t

def f5(t):
  return sin(t)-exp(-t)

def f6(t):
  return pow(t, 3) - 2*t - 2

def f7(t):
  return pow(t, 4) - t - 1

# generalized derivative: (dy/dx)^n
def dydx(fcn, v, degree=1):
  h = exp(-5)
  if degree == 0: 
    return fcn(v)
  elif degree > 1:
    return dydx((fcn(v+h) - fcn(v))/(h), degree-1)
  
  return (fcn(v+h) - fcn(v))/(h)


# this is somewhat unique to python, 
# an array of functions. ha!
f = [f1, f2, f3, f4, f5, f6, f7]

# an array of fn(x) outputs for each function.
# allows for easy calling later
fx = [[f[i](j) for j in x] for i in range(7)]

estimates = []
# solves each of the roots in one go. 
# iterates through while-loop for each function.
# uses a for initial guess
for i in range(len(f)):
  est = np.zeros(len(x))
  if i == 0 or i == 5:
    est = [1.7 for i in x]
  elif i == 6:
    est = [1.1 for i in x]
    
  for j in range(len(x-1)):
    if np.isclose(est[j]-est[j-1], 0.0, atol=epsilon):
      estimate = abs(est[j] - (f[i](est[j])/(dydx(f[i],est[j]))))
      estimates.append(estimate)
      break
    else:
      est[j+1] = abs(est[j] - (f[i](est[j])/(dydx(f[i],est[j]))))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

"""
# with this method, each color represents a function and its root.
# stars represent fcn values, dashes: their estimated roots.
fig, ax = plt.subplots()

# black axis horizontal line at  y=0
ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')

ax.grid()

# graphs each functionhttps://repl.it/@cjsproject/Root-Finding#sect_3.2/Q3/sqrt_a.py
# graphs x=root in a loop...
for i in range(7):
  ax.plot(x, fx[i], colors[i]+'--', label='f(x)=0') 
  ax.axvline(x=estimates[i], color=colors[i])


#ax.set_ylim(ymax=2, ymin=-2)

plt.title("Root Finding with Newton Color-Coordinated")
"""


fig, ax = plt.subplots(2, 4, sharex=True)

# a very bad and lazy way to graph all functions using a subplot matrix in matplotlib
fig, ax = plt.subplots(2, 4, sharex=True)

ax[0, 0].axhline(y=0, color='k')
ax[0, 0].axvline(x=0, color='k')
ax[0, 0].grid()
ax[0, 0].plot(x, fx[0], 'k')
ax[0, 0].axvline(x=estimates[0], color=colors[0], label='a')
ax[0, 0].legend()

ax[0, 1].axhline(y=0, color='k')
ax[0, 1].axvline(x=0, color='k')
ax[0, 1].grid()
ax[0, 1].plot(x, fx[1], 'k')
ax[0, 1].axvline(x=estimates[1], color=colors[1], label='b')
ax[0, 1].legend()

ax[0, 2].axhline(y=0, color='k')
ax[0, 2].axvline(x=0, color='k')
ax[0, 2].grid()
ax[0, 2].plot(x, fx[2], 'k')
ax[0, 2].axvline(x=estimates[2], color=colors[2], label='c')
ax[0, 2].legend()

ax[1, 0].axhline(y=0, color='k')
ax[1, 0].axvline(x=0, color='k')
ax[1, 0].grid()
ax[1, 0].plot(x, fx[3], 'k')
ax[1, 0].axvline(x=estimates[3], color=colors[3], label='d')
ax[1, 0].legend()

ax[1, 1].axhline(y=0, color='k')
ax[1, 1].axvline(x=0, color='k')
ax[1, 1].grid()
ax[1, 1].plot(x, fx[4], 'k')
ax[1, 1].axvline(x=estimates[4], color=colors[4], label='e')
ax[1, 1].legend()

ax[1, 2].axhline(y=0, color='k')
ax[1, 2].axvline(x=0, color='k')
ax[1, 2].grid()
ax[1, 2].plot(x, fx[5], color='k')
ax[1, 2].axvline(x=estimates[5], color=colors[5], label='f')
ax[1, 2].legend()

ax[1, 3].axhline(y=0, color='k')
ax[1, 3].axvline(x=0, color='k')
ax[1, 3].grid()
ax[1, 3].plot(x, fx[6])
ax[1, 3].axvline(x=estimates[6], color=colors[6], label='g')
ax[1, 3].legend()
# deletes fourth graph on top row
fig.delaxes(ax[0, 3])

#plt.title("Newton's Root Method")

#fix overlay of axes
plt.tight_layout()

#plt.savefig("newt_root_grid.png")
plt.show()