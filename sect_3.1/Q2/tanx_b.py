import matplotlib.pyplot as plt
import numpy as np

epsilon = 0.0001

x = np.linspace(np.pi*31, 32*np.pi, num=100000)

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
    if 0 <= abs((a-b))*(1/1024) <= epsilon:
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

ax.set_ylim(ymin=90, ymax=105)
ax.set_xlim(xmin=np.pi*31, xmax=101)

ax.legend()
plt.title("Closest to x=100, 0=tan(x)-x, 0.001 Error Tol")

plt.tight_layout()
#plt.savefig("tan_rt_100.png")

plt.show()
