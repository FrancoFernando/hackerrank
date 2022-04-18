A = [set([int(x) for x in input().split()]) for _ in range(2)][1]

for _ in range(int(input())):
    op = input().split()[0]
    params = 'set([' + ','.join(input().split()) + '])'
    eval('A.'+op+'('+params+')')
    
print(sum(A))
