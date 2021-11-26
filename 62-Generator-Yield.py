# https://www.youtube.com/watch?v=mziIj4M_uwk&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=67
def topten():
    n = 1
    while n <= 10:
        yield n  #### YIELD will make your function as GENERATOR
        n += 1


def showList(lst):
    for i in lst:
        yield i  #### YIELD will make your function as GENERATOR


v = topten()
# print(v.__next__())
# print(v.__next__())
# print(v.__next__())

for i in v:
    print(i, " loop")

gen = showList([2, 3, 5, 7, 11, 13])
for i in gen:
    print(i)
