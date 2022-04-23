from itertools import combinations_with_replacement

S, k = input().split()
#return an iterator
sorted_combos = combinations_with_replacement(sorted(S),int(k))
combos_string = [''.join(combo) for combo in sorted_combos]
print(*combos_string, sep='\n')
