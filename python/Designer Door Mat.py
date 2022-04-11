N,M = map(int,input().split())
mid_row = N//2
pattern = ".|."
repeat = 1
#print 'HackerRank'.center(M,'-')
for row in range(N):
    
    if row < mid_row:
        row_pattern = pattern * repeat
        print(row_pattern.center(M,'-'))
        repeat += 2
    elif row > mid_row:
        repeat -= 2
        row_pattern = pattern * repeat
        print(row_pattern.center(M,'-'))  
    else:
        print("WELCOME".center(M,'-'))
