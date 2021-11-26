f = open("MyData-65.txt", 'r')

# print(f.read())
# exit(0)
# print(f.readline())
# exit(0)
for i in f:
    print(i, end='')

with open("MyData-65.txt", 'r') as g:
    for i in g:
        print(i, end='')

w = open('MyData-65.write.txt', 'w')
w.write("Something\n")
w = open('MyData-65.write.txt', 'a')
w.write("ABC\n")
