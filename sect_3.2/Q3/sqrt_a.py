
import matplotlib.pyplot as plt
import numpy as np

"""
Newton's Rootfinding Method sqrt(a)

"""
# error tolerance
epsilon = 1.0e-6
# can define a to be any number.
# guess can also be any number (should be an educated guess)
a = 5
guess = 2
x = np.linspace(0.0, 5, num=100000)

# simply defining each function 1-7
def f(t):
  return pow(t, 2) - a

def rel_err(estims, index):
  return (-0.5)*((np.sqrt(a)-estims[index-1])*np.sqrt(a))

# generalized derivative: (dy/dx)^n
def dydx(fcn, v, degree=1):
  h = np.exp(-5)
  if degree == 0: 
    return fcn(v)
  elif degree > 1:
    return dydx((fcn(v+h) - fcn(v))/(h), degree-1)
  
  return (fcn(v+h) - fcn(v))/(h)

# an array of fn(x) outputs for each function.
# allows for easy calling later
fx = [f(j) for j in x]

estimates = []

# solves each of the roots in one go. 
# iterates through while-loop for each function.
# uses a for initial guess
est = [guess for j in x]

# this will solve any newton's method
for j in range(len(x-1)):
  est[j]-est[j-1]
  if np.isclose(est[j]-est[j-1], 0.0, atol=epsilon):
    estimate = abs(est[j] - (f(est[j])/(dydx(f,est[j]))))
    estimates.append(estimate)
    break
  else:
    est[j+1] = abs(est[j] - (f(est[j])/(dydx(f,est[j]))))

# estimating relative error for 3.c)
err_1 = [rel_err(est, i) for i in range(1,5)]


est = [guess for j in x]

for j in range(len(x-1)):
  est[j]-est[j-1]
  if np.isclose(est[j]-est[j-1], 0.0, atol=epsilon):
    estimate = abs(0.5*(est[j]+a/est[j]))
    estimates.append(estimate)
    break
  else:
    est[j+1] = abs(0.5*(est[j]+a/est[j]))


# estimating relative error for 3.c)
err_2 = [rel_err(est, i) for i in range(1,5)]

print(f"Relative Error of the first four estimations: {err_2}")

# with this method, each color represents a function and its root.
# stars represent fcn values, dashes: their estimated roots.
fig, ax = plt.subplots(2)

# black axis horizontal line at  y=0
ax[0].axhline(y=0, color='k')
#ax.axvline(x=0, color='k')

ax[0].grid()
ax[0].plot(x, fx, color='k') 
ax[0].axvline(x=estimates[0], color='r')


# black axis horizontal line at  y=0
ax[1].axhline(y=0, color='k')
#ax.axvline(x=0, color='k')

ax[1].grid()
ax[1].plot(x, fx, color='k')
ax[1].axvline(x=estimates[1], color='r')
#super title
fig.suptitle(f'sqrt(a) With Newton a={a}', fontsize=16)

#subtitles
ax[0].set_title("xn+1 = xn + (f(xn)/f'(xn))")
ax[1].set_title("xn+1 = 0.5(xn + (a/xn))")

#fix overlay of axes
plt.tight_layout()

#plt.savefig("newt_sqrta.png")
plt.show()