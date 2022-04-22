from itertools import product

A, B = [[int(x) for x in input().split()] for _ in range(2)]
print(*product(A, B))
