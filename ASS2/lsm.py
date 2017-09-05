import numpy as np
import matplotlib.pyplot as plt

# load csv into array x, y
x, y = np.loadtxt('/Users/earth/Documents/CEProjects/ToC/toc-assignment/ASS2/LS.csv', delimiter=',', skiprows=1, unpack=True)

# calculate z and p
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# plotting graph
xp = np.linspace(min(x), max(x), 100, color='g')
plt.plot(x, y, 'r.', xp, p(xp))
plt.show()