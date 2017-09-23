from random import randint
import matplotlib.pyplot as plt

# max integer
max_i = 100
# random times
r_times = 10**11

print("0000\r", end="")

ans = [0 for i in range(max_i)]
for i in range(10**4):
    for j in range(r_times // 10**4):
        ans[randint(0, max_i - 1)] += 1
    print(format(i + 1, '04d'), "\r", end="")
    f = open('platform.txt', 'a')
    print(i + 1, ": ", ans, file=f)
    f.close()