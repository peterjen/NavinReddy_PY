def topten():
    n = 1
    while n <= 10:
        yield n
        n += 1


def showList(lst):
    for i in lst:
        yield i


v = topten()
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())

for i in v:
    print(i, " loop")

gen = showList([2, 3, 5, 7, 11, 13])
for i in gen:
    print(i)
