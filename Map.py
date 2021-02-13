import timeit
setup1 = """
x = [1,4,5,7]
y = [7,5,4,8]
z = []
for i in range(len(x)): # i >> 0,1,2,3
    # i = 1
    Sum = x[i] + y[i] # Sum = x[1] + y[1] >> 4+5 = 9
    z.append(Sum) # z.append(9)
"""
#x = [1,4,5,7]
#y = [7,5,4,8]
#z = []
#for i in range(len(x)): # i >> 0,1,2,3
#    # i = 1
#    Sum = x[i] + y[i] # Sum = x[1] + y[1] >> 4+5 = 9
#    z.append(Sum) # z.append(9)
#print(z)
setup2 = """
x = [1,4,5,7]
y = [7,5,4,8]
z = []
Sum = lambda x,y,w:x+y+w
z = map(Sum,x,y)
"""
x = [1,4,5,7]
y = [7,5,4,8]
w = [7,5,4,8]
z = []
Sum = lambda x,y,w:x+y+w
z = map(Sum,x,y,w)
for i in z:
    print(i)
#print(timeit.timeit(setup1,number=1000))
#print(timeit.timeit(setup2,number=1000))
