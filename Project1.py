import math
import random


x= random.randrange(2,101)

y= random.randrange(0,91)

z= round ((random.uniform(0,10.0) + x),3) 


A1 = (float(x*math.sin(math.radians(y))))
A2 = z-A1*(x+math.cos(math.radians(y)))
Q1=0
Q2=0

print ('A1 = x*sin(y)')
print ('A2 = z-A1*(x+cos(y))')

print ("what is the value of A1 if x = {} , y = {}-degree , z = {}".format(x , y , z))

A1_answer = float(input("A1 = ")


if (A1 == A1_answer):
    print ("what is the value of A2 ?")
    A2_answer = (float(input("A2 = "))
    Q1=5
    if (A2 == A2_answer):
       Q2=5
    else: 
       Q2=0
else:
    Q1=0
    A2 = z-A1_answer*(x+math.cos(math.radians(y)))
    A2_answer = float(input("A2 = "))
   
    if A2 == A2_answer :
        Q2=5
    else :
        Q2=0

if Q1 == 0:
    if A1_answer<=A1+1 and A1_answer>=A1-1:
        Q1=5

if Q2 == 0:
    if A2_answer<=A2+1 and A1_answer>=A2-1:
        Q2=5

print ("your mark is <{}> of 10".format(Q1+Q2))

