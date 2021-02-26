
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, exp

"""
Bisection Rootfinding Method

"""

epsilon = 0.0001

a = [0 for i in range(7)]
b = [2.0 for i in range(7)]
c = [(i+j)*0.5 for i, j in zip(a,b)]
x = np.linspace(0.0, 2.0, num=100)



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

f = [f1, f2, f3, f4, f5, f6, f7]

fx = [[f[i](j) for j in x] for i in range(7)]

for i in range(len(f)):

  while (b[i]-c[i]) > epsilon:
    if f[i](b[i])*f[i](c[i]) <= 0:
      a[i] = c[i]
    else:
      b=c
    c[i] = (a[i]+b[i])*0.5
    print(f"a: {a[i]}\nb: {b[i]}\nc: {c[i]}\n(b-c)={b[i]-c[i]}")

roots = [[f[i](c[i]) for j in x] for i in range(len(f))]

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

fig.delaxes(ax[0, 3])
#plt.savefig("root1.png")
plt.show()