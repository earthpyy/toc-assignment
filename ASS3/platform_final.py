from random import randint
import matplotlib.pyplot as plt

# max integer
max_i = 100
# random times
r_times = 10**11

# print start progress
print("0000\r", end="")

ans = [0 for i in range(max_i)]
for i in range(10**4):
    # inner loop to show progress
    for j in range(r_times // 10**4):
        # rand() in platform
        ans[randint(0, max_i - 1)] += 1

    # show progress
    print(format(i + 1, '04d'), "\r", end="")
    # save result to file
    f = open('platform.txt', 'a')
    print(i + 1, ": ", ans, file=f)
    f.close()

# show graph
plt.bar(range(max_i), ans, 0.9, edgecolor='b')
plt.title("Platform's PRNG")
plt.show()