n = int(input())
nn = 1

for i in range(2, n):
    nn +=  1 / i 
print("{:.4f}".format(nn))
