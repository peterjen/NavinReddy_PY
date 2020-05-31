def fact(n):
    s = 1
    for i in range(1,n+1):
        s =s * i
    return s

s = fact(8)
print(s)