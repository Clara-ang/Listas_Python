n = int(input())

for i in range(2, n):
    if n % i == 0:
        print("Nao")
    if n == 1:
        print("Nao")

else:
    print("Sim")


