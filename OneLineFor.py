#L = [4,8,7,9,5,6]
#z = []
#for i in L:
#    z.append(i*2)
#print(z)
#
#z = [[i*2 for i in L] for y in range(6) ]
#print(z)

Names = ['Python','C++']
L = [i for i in Names if len(i) > 5]
print(L)