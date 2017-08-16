import numpy as np

x, y = np.loadtxt('/Users/earth/Documents/CEProjects/ToC/ASS2/LS.csv', delimiter=',', skiprows=1, unpack=True)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

#plotting
import matplotlib.pyplot as plt
xp = np.linspace(min(x), max(x), 100)
plt.plot(x, y, '.', xp, p(xp))
plt.show()
