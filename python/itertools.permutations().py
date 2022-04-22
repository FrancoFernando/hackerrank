from itertools import permutations

S, k = input().split()
sorted_permutations = sorted(list(permutations(S,int(k))))
perms = [''.join(perm) for perm in sorted_permutations]
print(*perms, sep = '\n')
#print('\n'.join(perms))
