a=27
for num in range(2,27):
    for i in range(2, num):
        if num % i == 0:
            #print(num, " is not a prime")
            break
    else:
        print(num, " is a prime")
