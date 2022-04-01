import math
import cmath

num = complex(input())
print(math.sqrt(num.real**2+num.imag**2))
print(cmath.phase(num))
