lst = [2, 5, 3, 4]

it = iter(lst)

print(it.__next__())
print(it.__next__())
print(next(it))
# print(next(it))

print("##########")
for i in lst:
    print(i)

print("##### Customer Iterator")


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 11:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
it = iter(values)
print(it.__next__())
print(next(it))
#exit()

for i in values:
    print(i)
