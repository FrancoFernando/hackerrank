# without add
#countries = set([input() for _ in range(int(input()))])
#print(len(countries))

# with add
countries = set()
for _ in range(int(input())):
    countries.add(input())
print(len(countries))
