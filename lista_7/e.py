n = int(input())
num = list(map(int, input().split()))

media_b = 0
media_acima = 0

media = sum(num) / n

for i in num:
    if i < media:
        media_b += 1
    if i >= media:
        media_acima += 1
       
print("{:.1f}".format(media))
print(media_b)
print(media_acima)