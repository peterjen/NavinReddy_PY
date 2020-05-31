f = open("MyData-65.txt",'r')

#print(f.read())

#print(f.readline())

for i in f:
    print(i,end='')

with open("MyData-65.txt",'r') as g:
    for i in g:
        print(i,end='')