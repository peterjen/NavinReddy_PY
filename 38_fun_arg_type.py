

###  POSITION
def add(x,y):
    return x + y
print(add(2,3))


### KEYWORD
def person(name,age):
    print(name,age)
person(age=33, name='Peter')


### DEFAULT
def person(name, age=18):
    print(name,age)
person('Peter')

## Variable Length
def addall(*x): ## x will be a TUPLE
    c = 0
    for i in x:
        c += i
    print(c)

addall(1,2,3,4)

### Keyworded Variable Length Arguments in Python | **kwargs

def person(**data):   # USE : **variable
    print(type(data)) # DICTIONARY
    for i,j in data.items():
        print(i,j)

person(name='Peter',age=33,city="Bridgewater")

