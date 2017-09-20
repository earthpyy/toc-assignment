from random import randint
import matplotlib.pyplot as plt

# max integer
max_i = 100
# random times
r_times = 10**7

ans = [0 for i in range(max_i)]

for i in range(r_times):
    ans[randint(0, max_i - 1)] += 1

plt.bar(range(max_i), ans, 0.9, edgecolor='b')
plt.title("Platform's PRNG")

# plt.ylim(900000, 1100000)
plt.show()