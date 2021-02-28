
import matplotlib.pyplot as plt
import numpy as np

"""
Newton's Rootfinding Method mth root of (a)
"""

# error tolerance
epsilon = 1.0e-6

# can define a to be any number.
# guess can also be any number (should be an educated guess)
a = 8
guess = 3
# array of powers, allows for reusability.
p = [3, 4, 5, 6 ,7, 8]
epsilon = 1.0e-6
x = np.linspace(0.0, 4.0, num=100000)

# flexible function definition
# gives ability to define a function
# of multiple powers, defined in p
def f(t, ind):
  return pow(t, p[ind]) - a

def rel_err(estims, index):
  return (-0.5)*((np.sqrt(a)-estims[index-1])*np.sqrt(a))

# generalized derivative: (dy/dx)^n
# customized to call specific power of p
def dydx(fcn, v, index, degree=1):
  h = np.exp(-5)
  if degree == 0: 
    return fcn(v, index)
  elif degree > 1:
    return dydx((fcn(v+h, index) - fcn(v, index))/(h), degree-1)
  
  return (fcn(v+h, index) - fcn(v, index))/(h)

# an array of fn(x) outputs for each function.
# allows for easy calling later
fx = [[f(j, i) for j in x] for i in range(len(p))]

estimates = []

# solves each of the roots in one go. 
# iterates through while-loop for each function.
# uses a for initial guess
est = [guess for j in x]

# this will solve any newton's method for p size amt of fcns
for i in range(len(p)):
  for j in range(len(x-1)):
    est[j]-est[j-1]
    if np.isclose(est[j]-est[j-1], 0.0, atol=epsilon):
      estimate = abs(est[j] - (f(est[j], i)/(dydx(f,est[j], i))))
      estimates.append(estimate)
      break
    else:
      est[j+1] = abs(est[j] - (f(est[j], i)/(dydx(f,est[j], i))))


fig, ax = plt.subplots(3, 2)

# black axis horizontal line at  y=0
ax[0, 0].axhline(y=0, color='k')
ax[0, 0].grid()
ax[0, 0].plot(x, fx[0], color='k') 
ax[0, 0].axvline(x=estimates[0], color='r')
# black axis horizontal line at  y=0
ax[0, 0].axhline(y=0, color='k')

ax[0, 1].grid()
ax[0, 1].plot(x, fx[1], color='k')
ax[0, 1].axvline(x=estimates[1], color='r')
# black axis horizontal line at  y=0
ax[0, 1].axhline(y=0, color='k')

ax[1, 0].grid()
ax[1, 0].plot(x, fx[2], color='k') 
ax[1, 0].axvline(x=estimates[0], color='r')
# black axis horizontal line at  y=0
ax[1, 0].axhline(y=0, color='k')

ax[1, 1].grid()
ax[1, 1].plot(x, fx[3], color='k')
ax[1, 1].axvline(x=estimates[1], color='r')
# black axis horizontal line at  y=0
ax[1, 1].axhline(y=0, color='k')

ax[2, 0].grid()
ax[2, 0].plot(x, fx[4], color='k')
ax[2, 0].axvline(x=estimates[1], color='r')
# black axis horizontal line at  y=0
ax[2, 0].axhline(y=0, color='k')

ax[2, 1].grid()
ax[2, 1].plot(x, fx[5], color='k')
ax[2, 1].axvline(x=estimates[1], color='r')
# black axis horizontal line at  y=0
ax[2, 1].axhline(y=0, color='k')

#super title
fig.suptitle(f'mth root of (a) With Newton a={a}', fontsize=16)

#subtitles
ax[0,0].set_title(f"{p[0]}rd root")
ax[0,1].set_title(f"{p[1]}th root")
ax[1,0].set_title(f"{p[2]}th root")
ax[1,1].set_title(f"{p[3]}th root")
ax[2,0].set_title(f"{p[4]}th root")
ax[2,1].set_title(f"{p[5]}th root")


#fix overlay of axes
plt.tight_layout()

plt.savefig("newt_mth_root.png")
plt.show()