n = int(input())
i = 1

for i in range(0, 10):
    i += 1
    num = i * n
    print("{:1d} x {:1d} = {:1d}".format(i, n, num))