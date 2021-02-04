x = float(input("input x: "))
y = float(input("input y: "))

try:
    z = x / y
    print(z)
except NameError:
    print("Error")
except ZeroDivisionError:
    print("divide by zero")
except:
    print("error")
finally:
    print("Done")
