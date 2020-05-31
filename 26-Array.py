import array as arr
import math

# import numpy as np

vals = arr.array('i', [1, 2, -3, 4, 5])
print(vals)
print(vals.buffer_info())
# vals.reverse()
# print(vals)
print(vals.index(2))
print(len(vals))

for i in vals:
    print(i)

newarr = arr.array(vals.typecode, (a for a in vals))
print(newarr)
newarr[0] = 9
print(newarr)
print(vals)
n = vals
n[0] = 9
print(n)
print(vals)

print(sorted(n))

print(math.factorial(5))
