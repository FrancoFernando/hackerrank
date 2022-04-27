from collections import defaultdict

d = defaultdict(list)
n, m = [int(x) for x in input().split()]
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

for i,a in enumerate(A,start=1):
    d[a].append(i)
    
for b in B:
    if b in d:
        print(" ".join([str(i) for i in d[b]]))
    else:
        print(-1)
