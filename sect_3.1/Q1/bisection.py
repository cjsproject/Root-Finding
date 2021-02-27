
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, exp

"""
Bisection Rootfinding Method

"""
# error tolerance
epsilon = 0.0001

# create a unique array of a,b,c for each function.
# this is necessary for the loop later on.
a = [0 for i in range(7)]
b = [2.0 for i in range(7)]
c = [(i+j)*0.5 for i, j in zip(a,b)]
x = np.linspace(0.0, 2.0, num=100)

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


# this is somewhat unique to python, 
# an array of functions. ha!
f = [f1, f2, f3, f4, f5, f6, f7]

# an array of fn(x) outputs for each function.
# allows for easy calling later
fx = [[f[i](j) for j in x] for i in range(7)]

# solves each of the roots in one go. 
# iterates through while-loop for each function.
for i in range(len(f)):
  while (b[i]-c[i]) > epsilon:
    if f[i](b[i])*f[i](c[i]) <= 0:
      a[i] = c[i]
    else:
      b=c
    c[i] = (a[i]+b[i])*0.5
    print(f"a: {a[i]}\nb: {b[i]}\nc: {c[i]}\n(b-c)={b[i]-c[i]}")

# creates an array of constant functions, each of which is the estimated bisection root.
roots = [[f[i](c[i]) for j in x] for i in range(len(f))]

"""
# with this method, each color represents a function and its root.
# stars represent fcn values, dashes: their estimated roots.
fig, ax = plt.subplots()

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.grid()
for i in range(7):
  ax.plot(x, fx[i], colors[i]+'*', label='f(x)=0')
  ax.plot(x, roots[i], colors[i]+"--", label='root')

ax.set_ylim(ymax=2, ymin=-2)

plt.title("Root Finding with Bisection Color-Coordinated")
"""


fig, ax = plt.subplots(2, 4, sharex=True)

# a very bad and lazy way to graph all functions using a subplot matrix in matplotlib
fig, ax = plt.subplots(2, 4, sharex=True)

ax[0, 0].axhline(y=0, color='k')
ax[0, 0].axvline(x=0, color='k')
ax[0, 0].grid()
ax[0, 0].plot(x, fx[0], 'k', label='f(x)=0')
ax[0, 0].plot(x, roots[0], 'r--', label='root')

ax[0, 1].axhline(y=0, color='k')
ax[0, 1].axvline(x=0, color='k')
ax[0, 1].grid()
ax[0, 1].plot(x, fx[1], 'k', label='f(x)=0')
ax[0, 1].plot(x, roots[1], 'r--', label='root')

ax[0, 2].axhline(y=0, color='k')
ax[0, 2].axvline(x=0, color='k')
ax[0, 2].grid()
ax[0, 2].plot(x, fx[2], 'k', label='f(x)=0')
ax[0, 2].plot(x, roots[2], 'r--', label='root')

ax[1, 0].axhline(y=0, color='k')
ax[1, 0].axvline(x=0, color='k')
ax[1, 0].grid()
ax[1, 0].plot(x, fx[3], 'k', label='f(x)=0')
ax[1, 0].plot(x, roots[3], 'r--', label='root')

ax[1, 1].axhline(y=0, color='k')
ax[1, 1].axvline(x=0, color='k')
ax[1, 1].grid()
ax[1, 1].plot(x, fx[4], 'k', label='f(x)=0')
ax[1, 1].plot(x, roots[4], 'r--', label='root')

ax[1, 2].axhline(y=0, color='k')
ax[1, 2].axvline(x=0, color='k')
ax[1, 2].grid()
ax[1, 2].plot(x, fx[5], 'k', label='f(x)=0')
ax[1, 2].plot(x, roots[5], 'r--', label='root')

ax[1, 3].axhline(y=0, color='k')
ax[1, 3].axvline(x=0, color='k')
ax[1, 3].grid()
ax[1, 3].plot(x, fx[6], 'k', label='f(x)=0')
ax[1, 3].plot(x, roots[6], 'r--', label='root')

# deletes fourth graph on top row
fig.delaxes(ax[0, 3])


#fix overlay of axes
plt.tight_layout()

#plt.savefig("grid_roots.png")
plt.show()