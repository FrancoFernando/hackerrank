from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *val = input().split()
    if cmd.startswith('pop'):
        exec('d.' + cmd + '()')
    else:
        exec('d.' + cmd + "(" + val[0] + ")")
    
print(*d)
