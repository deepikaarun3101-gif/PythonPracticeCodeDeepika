a= input("Enter a number:")
b= input("Enter second number:")
c= input("Enter third number:")
#print(type(a))
if (a == b == c):
    print ('a,b & c are equal')
elif (a >= b) and (a >= c):
    print('a is greater than b,c')
elif (b >= c) and (b >= a):
    print('b is greater than a,c')
elif (c >= a) and (c >= b):
    print('c is greater than b,a')
else:
    print('exceptional condition is met')


#print(type(a))

#if (isinstance(a, int)):
 #   print('good')
#else:
 #   print('Bad')