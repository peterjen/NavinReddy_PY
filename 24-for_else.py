a1 = [12, 21, 11, 43]

for i in a1:
    if i % 5 == 0:
        print(i)
        break
else:  # Happens if the LOOP was not BREAK
    print("Not Found")
