room_numbers = [input().split() for _ in range(2)][1]
all_numbers = set()
duplicated_numbers = set()

for num in room_numbers:
    if num in all_numbers:
        duplicated_numbers.add(num)
    else:
        all_numbers.add(num)
        
print(list(all_numbers ^ duplicated_numbers)[0])
