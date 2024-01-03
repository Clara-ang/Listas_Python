def is_subsequence(sa, sb):
    i = 0
    j = 0

    while i < len(sa) and j < len(sb):
        if sa[i] == sb[j]:
            j += 1
        i += 1

    return j == len(sb)

# Leitura de entrada
A, B = map(int, input().split())
sa = list(map(int, input().split()))
sb = list(map(int, input().split()))


result = is_subsequence(sa, sb)

if result:
    print('S')
else:
    print('N')
