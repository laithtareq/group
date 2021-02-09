import random 
from math import sin,cos,radians
mark = 0
random.seed(1)
x = random.randrange(2,101)
y = round(random.uniform(0,90),3)
z = x + round(random.uniform(0,11),3)
try:
    F = float(input("Enter value for F: "))
except:
    F = 0
A1_real = x * sin(radians(y))
print('A1 = {}'.format(A1_real))
A1 = float(input("What is A1 where x = {} , y = {} , z = {} ? ".format(x,y,z)))
if A1 >= A1_real-F and A1 <= A1_real+F:
    mark+=5

A2_real = z - A1*(x+cos(radians(y)))
print('A2 = {}'.format(A2_real))
A2 = float(input("What is the value of A2? "))
if A2 >= A2_real-F and A2 <= A2_real+F:
    mark+=5
print(mark)