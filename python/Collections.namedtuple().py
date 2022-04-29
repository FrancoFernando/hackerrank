from collections import namedtuple

N = int(input())
column = namedtuple('Col',input().split())
marks_sum = 0

for _ in range(N):
    values = input().split()
    row = column(values[0], values[1], values[2], values[3])
    marks_sum += int(row.MARKS)
    
marks_avg = marks_sum/N
print(f'{marks_avg:.2f}')
