from collections import Counter

shoe_size = Counter([[int(x) for x in input().split()] for _ in range(2)][1])

income = 0
for _ in range(int(input())):
    
    size, price = [int(x) for x in input().split()]
    if shoe_size[size]: # return 0 if no key is in Counter
        income += price
        shoe_size[size] -= 1

print(income)
