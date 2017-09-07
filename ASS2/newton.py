import matplotlib.pyplot as plt
from decimal import *

# number to square root
number = 13
# start number
start = Decimal(3)
# epsilon
epsilon = Decimal(0.00000000001)
# array of value
y = []

# derivative function
def derivative(x, h):
      return (f(x+h) - f(x-h)) / (Decimal(2) * h)

# function to solve
def f(x):
    return x**2 - number

# newton-raphson's method
def solve(x0, h):
    lastX = Decimal(x0)
    nextX = lastX + Decimal(10) * h
    while abs(lastX - nextX) > h:
        newY = f(nextX)
        lastX = nextX
        nextX = lastX - newY / derivative(lastX, h)
        
        # show value
        print nextX
        # add value to array to plotting
        y.append(nextX)
    return nextX

# call solve function
answer = solve(start, epsilon)

# show graph
x = list(range(len(y)))
plt.plot(x, y)
plt.plot(x, y, 'r.')
plt.show()