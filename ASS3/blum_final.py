import matplotlib.pyplot as plt

# seed of random function
seed = 6
# function parameters
p = 47
q = 67
# max integer
max_i = 100
# random times
r_times = 10**11

# print start progress
print("0000\r", end="")

ans = [0 for i in range(max_i)]
for i in range(10**4):
    # inner loop to save some progress
    for j in range(r_times // 10**4):
        # blum blum shub method
        x = (seed**2) % (p * q)
        # mod by 100 and count in ans[]
        ans[x % max_i] += 1
        # x is next seed
        seed = x
        # print debug
        # print(x)

    # print progress
    print(format(i + 1, '04d'), "\r", end="")
    # save result to file
    f = open('blum.txt', 'a')
    print(i + 1, ": ", ans, file=f)
    f.close()

# show graph
plt.bar(range(max_i), ans, 0.9, edgecolor='b')
plt.title("Blum Blum Shub PRNG")
plt.show()