import random as r
import math as m
import matplotlib.pyplot as plt

# number of darts
inside = 0
# total darts to throw
total = 10000000
# enable plot window
plotEnabled = False

# initialize plot window
if plotEnabled:
    plt.axes()
    # create circle with radius=1 and color=blue
    circ = plt.Circle((0, 0), radius=1, color='b', fill=False)
    plt.gca().add_patch(circ)

for i in range(0, total):
    # generate x, y randomly in range [0, 1]
    x = r.random()
    y = r.random()
    # check if it is in circle
    if m.sqrt(x ** 2 + y ** 2) < 1.0:
        inside += 1
        # plot into graph
        if plotEnabled:
            plt.plot(x, y, 'g.')
    elif plotEnabled:
        #plot into graph
        plt.plot(x, y, 'r.')

# calculate the last answer
pi = (float(inside) / total) * 4

# print answer in console
print(pi)

# if plot is enable then show it
if plotEnabled:
    plt.axis('scaled')
    plt.show()