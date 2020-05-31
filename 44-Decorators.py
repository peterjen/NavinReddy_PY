print("\n#### DECORATOR RECAP EXISTING FUNCTION \nWITHOUT TOUCHING old function")
def div_dec(func):
    def inner(a, b):
        if a < b:  # ADD NEW LOGIC HERE
            a, b = b, a
        if b == 0:
            print("WRONG")
            return
        return func(a, b)  # CALL OLD FUNC

    return inner


@div_dec
def div(a, b):
    return (a / b)


print(div(2, 4))

# div = div_dec(div)  # Connect to existing function
print(div(4, 2))
