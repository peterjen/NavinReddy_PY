
for i in range(5,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()

a1 = "ABCD"
a2 = "PQR"
for i in range(4):
    for j in range(i+1):
        for k in range(len(a2),0,-1):
            print(a1[0:j] + a2[0:k])
