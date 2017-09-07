import random as r
import math as m
import matplotlib.pyplot as plt

# number of darts
inside = 0
# total darts to throw
total = 10000
# enable plot window
plotCircleEnabled = True
plotDevelopEnabled = True
# plot develop every ... times
plotTime = 350
# array of value
x_pi = range(0, total, plotTime)
y_pi, x_in, x_out, y_in, y_out = [], [], [], [], []

# initialize plot window
if plotCircleEnabled:
    plt.figure(0)
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
        if plotCircleEnabled:
            x_in.append(x)
            y_in.append(y)
    elif plotCircleEnabled:
        #plot into graph
        x_out.append(x)
        y_out.append(y)

    # calculate pi
    pi = (float(inside) / (i + 1)) * 4

    # check if it's time to plot
    if plotDevelopEnabled and i % plotTime == 0:
        y_pi.append(pi)
        print(pi)

# print answer in console
pi = (float(inside) / total) * 4
print(pi)

# if plot is enable then show it
if plotCircleEnabled:
    plt.figure(0)
    plt.plot(x_in, y_in, 'g.')
    plt.plot(x_out, y_out, 'r.')
    plt.axis('scaled')
    plt.show()

if plotDevelopEnabled:
    plt.figure(1)
    plt.plot(x_pi, y_pi)
    plt.plot(x_pi, y_pi, 'r.')
    plt.show()