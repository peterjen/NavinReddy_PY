a = 6
b = 2
b = 0
try:
    print(a / b)

except ZeroDivisionError as e:
    print("NOT DIV BY 0",e)
except Exception as e:
    print("EXCEPTION",e)

finally:
    print("---- FINALLY ALWAYS PROCESSED NO MATTER WHAT")