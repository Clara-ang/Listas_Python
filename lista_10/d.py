from collections import Counter

def max_numbers_marked(N, sequence):
    count = Counter(sequence)
    
  
    max_single_number = max(count.values())
    
    
    max_two_numbers = 0
    for i in range(1, N+1):
        max_two_numbers = max(max_two_numbers, count[i] + count[i+1])
    
    return max(max_single_number, max_two_numbers)


N = int(input())
sequence = [int(input()) for _ in range(N)]

result = max_numbers_marked(N, sequence)
print(result)
