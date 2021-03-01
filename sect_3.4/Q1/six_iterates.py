import matplotlib.pyplot as plt
import numpy as np

"""
    Iteration Method
    Xn+1 = 1+0.3sin(Xn)
    First Six Iterates
    x0=1, and x0=1.5
"""

# convergence is not related to the initial value x0
x0 = [1.0, 1.5]
row_labels = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6']
col_labels = [f"x0={x0[0]}", f"x0={x0[1]}"]

# iterate formula for nth iterate.
def next(current):
  return 1+(0.3*np.sin(current))

# have to create iterate array and
# text array for the table display
iterates = [[], [], [], [], [] ,[] ,[]]
text = [[], [], [], [], [] ,[] ,[]]
for j in range(7):
    for i in range(2):
        if j == 0:
            iterates[j].append(x0[i])
            text[j].append(str(x0[i]))
        else:
            current = iterates[j-1][i]
            nxt = next(current)
            iterates[j].append(nxt)
            text[j].append(str(nxt))

fig, ax = plt.subplots()

# super title
fig.suptitle("Xn+1 = 1 + 0.3sin(Xn)")
# creating the table
ax.table(cellText=text, rowLabels=row_labels, colLabels=col_labels, loc='center')
# tightening and removing axes from traditional graph
ax.axis('tight')
ax.axis('off')
#plt.savefig("Q1_iterates.png")
plt.show()
