test_cases = int(input())

for _ in range(test_cases):
    A, B = [set(input().split()) for _ in range(4)][1::2]
    print(A.issubset(B))
