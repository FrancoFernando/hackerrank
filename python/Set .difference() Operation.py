english, french = [set(input().split()) for _ in range(4)][1::2]
print(len(english - french))
