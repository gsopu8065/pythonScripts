import numpy as np;

#create an array 
#way-1
a = np.array([2,3,4]) 
b = np.array([(1,2,3), (4,5,6)])

# Way -2 zeros, ones, empty
c = np.zeros( (3,4) )   #3-rows 4-colms

#Way- 3 create sequence of numbers
d = np.arange(0,10,1)  # (start[ default 0] , end, increment [default 1])

#way- 4 create random numbers
e = np.random.random((2,3))



#Printing an array
#print method (Way 1)
print a
print b

#two dimention array
for row in c:
    print row

#Way 2 flat method
for eachElement in e.flat:
    print eachElement
    

#Basic Operations +,-,*,/,%,+=, < , >, **
#Unary operators sum(), min(), max() with/without axis
print a*10
print a < 20
print a.sum()
print b.sum(axis = 0)  #sum of each column
print b.sum(axis = 1)  #sum of each row


#reshape resize the array
f = np.arange(12)
print f
print f.reshape(3,4)
print f.reshape(2,2,3)