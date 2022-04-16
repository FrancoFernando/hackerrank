n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, *arg = input().split()
    if cmd == "pop":
        s.pop()
    else:
        eval('s.'+cmd+'('+arg[0]+')')
print(sum(s))
