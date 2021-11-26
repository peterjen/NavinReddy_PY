d1 = {
    1: 'Peter',
    2: 'June',
    3: 'jj'
}
print(d1[2])
print(d1.get(3))
print(d1.pop(1))
print(d1)

####

keys = [11, 22, 33, 44]
values = ['qq', 'ww', 'ee', 'rr']
d2 = dict(zip(keys, values))
print(d2)

d2[55] = 'tt'
print(d2)

del d2[11]
print(d2)
print(d2.keys())
print(d2.values())

#x = list(range(10))
#print(x)
