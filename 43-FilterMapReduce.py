from functools import reduce

nums = [2, 4, 1, 8, 6, 3, 8, 0]

print("\n#### FILTER(function, sequence)")
evens = list(filter(lambda a: a % 2 == 0, nums))
odds = list(filter(lambda a: a % 2 == 1, nums))
print(evens)
print(odds)

print("\n#### MAP(function, sequence)")
add_two = list(map(lambda a: a + 2, nums))
print(add_two)

# print(sum(nums))
print("\n#### REDUCE(function, sequence)")
total = reduce(lambda a, b: a + b, nums)
print(total)
