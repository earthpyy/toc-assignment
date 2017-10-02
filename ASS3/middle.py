import matplotlib.pyplot as plt
import math

# seed of random function
seed = 69
# number of digits
n = len(str(seed))
# max integer
max_i = 100
# random times
r_times = 20

# print("0000\r", end="")

ans = [0 for i in range(max_i)]
for i in range(r_times):
    x = (seed**2 % (10 ** (n + n // 2)) // (10 ** (n // 2)))
    ans[x] += 1
    seed = x
    # print(format(i + 1, '04d'), "\r", end="")
    print(x)

# zero forever
ans[0] += (10**11) - 20

f = open('middle.txt', 'w')
print(i + 1, ": ", ans, file=f)
f.close()

plt.bar(range(max_i), ans, 0.9, edgecolor='b')
plt.title("Middle-Square PRNG")

plt.show()