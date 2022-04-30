from collections import OrderedDict

ordered_dict = OrderedDict()

for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    ordered_dict[item] = ordered_dict.get(item, 0) + int(price)
    
for item, price in ordered_dict.items():
    print(item + ' ' + str(price))
