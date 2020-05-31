a = 1
b = 2
sum = 0
print(a)
print(b)
for i in range(0,50):
    sum = a + b
    print(sum)
    a,b = b,sum
