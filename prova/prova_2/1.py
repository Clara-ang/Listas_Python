def func1(listnum):
    k= listnum[0]
    for i in range(len(listnum)):
        k= k + listnum[i]

    return  k


x= list(map(int, input().split()))

print(func1(x))
