a = 10
print(id(a))

def myFunc():
    global a
    a = 20
    #x = globals()['a'] # globals() will give all global variables
    #print(id(x))
    print(a)
    globals()['a'] = 15


myFunc()
print(a)
