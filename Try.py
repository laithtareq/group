x = float(input("input x: "))
y = float(input("input y: "))
z = 0
try:
    z = x / y
#except ZeroDivisionError:
#    z = 0
#except NameError:
#    print("X is not defined")
except:
    pass
finally:
    print("Done")
print(z)