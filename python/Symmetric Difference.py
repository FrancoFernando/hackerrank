M = input()
A = set(int(x) for x in input().split())
N = input()
B = set(int(x) for x in input().split())
print(*sorted(A.symmetric_difference(B)), sep='\n')
#C = sorted(A.symmetric_difference(B))
#print('\n'.join(map(str,C)))

# possible oneliner for the input, but require key = int in sorted
# A,B = [set(input().split()) for _ in range(4)][1::2]
