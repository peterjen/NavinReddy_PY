a = 6
b = 2
# b = 0
try:
    print(a / b)  # CHECK DIVIDE BY ZERO ERROR

    k = int(input("Please enter a CHAR: "))  # CHECK VALUE ERROR
    print(k)

    f = open("states1234.json", "r")  # CHECK FILE NOT FOUND ERROR
    # print(f)
    print("Name of the file: ", f.name)
    if not f.closed:
        print('File close here...')
        f.close()


except ZeroDivisionError as e:
    print("YOU DIVIDE BY 0", e)
except FileNotFoundError as e:
    print("The file not exist...", e)
except ValueError as e:
    print("Invalid Input...", e)
# except Exception as e:
#     print("EXCEPTION", e)

finally:
    print("---- FINALLY ALWAYS PROCESSED NO MATTER WHAT")
