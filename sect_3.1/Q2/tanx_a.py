import matplotlib.pyplot as plt
import numpy as np

epsilon = 0.0001

x = np.linspace(np.pi*0.5, 2*np.pi, num=10000)

fx = np.tan(x)
y_x = [i for i in x]

root = 0

# this loop checks (a-b)
# if <= epsilon, saves root and breaks
for a, b in zip(fx, y_x):
    # prints the true difference of y values
    print(a-b)
    # note here, my options were to weight the
    # difference by 1/8 or compute over
    # one million points using linspace.
    if 0 <= abs((a-b))*0.0125 <= epsilon:
        root = a
        break

# prints the root, which is
# the x-value at which the functions intersect
print(root)

fig, ax = plt.subplots()

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.axvline(x=root, color='b', label='root')
ax.grid()

ax.plot(x, np.tan(x), 'g', label='tan(x)')
ax.plot(x, y_x, 'r--', label='y=x')

ax.set_ylim(ymin=-7, ymax=7)
ax.set_xlim(xmin=np.pi*0.5)

ax.legend()
plt.title("Smallest Root > 0, 0=tan(x)-x, 0.001 Error Tol")

plt.tight_layout()
#plt.savefig("0tan_sm_nz_rt.png")

plt.show()