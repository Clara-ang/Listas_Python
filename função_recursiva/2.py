def negativos(list):
    if not list:
        return 0
    else:
        if list[0] > 0:
            return 0 
        else:
            return 1 + negativos(list[1:])
    
        
num = [list(map(int, input().split()))]
r = negativos(list)
print(r)