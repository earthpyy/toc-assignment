# number to square root
number = 13
# start number
start = 1
# epsilon
epsilon = 0.000001

# derivative function
def derivative(x, h):
      return (f(x+h) - f(x-h)) / (2.0 * h)

# function to solve
def f(x):
    return x**2 - number

# newton-raphson's method
def solve(x0, h):
    lastX = x0
    nextX = lastX + 10 * h
    while (abs(lastX - nextX) > h):
        newY = f(nextX)
        lastX = nextX
        nextX = lastX - newY / derivative(lastX, h)
    return nextX

# call solve function
answer = solve(start, epsilon)
# print answer
print answer