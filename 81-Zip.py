first = ['Peter','June','Chloe','John']
last = ['Jen','Chen','Jen','Jen']

print("\n### ZIP")
zipper = zip(first,last)
print(zipper)
for a, b in zipper:
    print(a,b)

print("\n### ZIP LIST")
zipper = list(zip(first,last))
print(zipper)

print("\n### ZIP SET")
zipper = set(zip(first,last))
print(zipper)

print("\n### ZIP DICTIONARY")
zipper = dict(zip(first,last))
print(zipper)

