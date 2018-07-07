def sum(x, y, z=0):
    return x+y+z;

sum2 = lambda x,y,z=0: x+y+z;

print sum(10,20), sum2(100,200,300)
