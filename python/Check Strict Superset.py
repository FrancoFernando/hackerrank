A = set(input().split())
other_sets = int(input())
results = []
for _ in range(other_sets):
    results.append(A.issuperset(set(input().split())))
        
print(all(results))
