from array import *

a = array('i', [])
n = int(input("How many elements: "))
for i in range(n):
    m = int(input("Enter value: "))
    a.append(m)
v = int(input("WHat num to search"))

print(a.index(v))
a.remove(v)
print(a)

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr[::-1])
arr.reverse()
print(arr)
