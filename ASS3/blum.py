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
# real random times
rr_times = 110

# print("0000\r", end="")
s = seed
ans = [0 for i in range(max_i)]
for i in range(rr_times):
    x = (s**2) % (p * q)
    # ans[x] += 1
    ans[x % max_i] += (r_times // rr_times)
    s = x
    # print(format(i + 1, '04d'), "\r", end="")
    # print(x)

# repeat forever
s = seed
for i in range(r_times % rr_times):
    x = (s**2) % (p * q)
    ans[x % max_i] += 1
    s = x

f = open('blum.txt', 'w')
print(ans, file=f)
f.close()

plt.bar(range(max_i), ans, 0.9, edgecolor='b')
plt.title("Blum Blum Shub PRNG")

plt.show()