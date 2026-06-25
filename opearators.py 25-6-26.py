#python opearators variables and data types

'''
1.Arithmetic opearators
2.Assignment opearators
3.Comparsion opearators
4.Logical opearators
5.Bitwise opearators
6. Type conversion
'''

#Arithmetic opeartor

a=60
b=80

print("addition:",a+b)
print("substaction:",a-b)
print("multipliction:",a*b)
print("division:",a/b)
print("modulus:",a%b)
print("exponentiation:",a**b)
print("floor division:",a//b)

#Assinment opearator

#simple assignment

X=20
Y=40

#addition assignment

X+=Y#X=X+Y

print(X)
print(Y)

#substraction assignment

X-=Y

print(X)
print(Y)

#division assignment

X/=Y

print(X)
print(Y)

#modulus assignment

X%=Y

print(X)
print(Y)

#exponentiation assignment

X**=Y

print(X)
print(Y)

#floor assignment

X//=Y

print(X)
print(Y)

#Comparision opearator

X=50
Y=80
print(X==Y)
print(X!=Y)
print(X<Y)
print(X<=Y)
print(X>Y)
print(X>=Y)

X=Y

print(X)
print(Y)

#Logical opearator(and,or,not)

X=True
Y=False
Z=False

print(X and Y)
print(Y and Z)
print(X or Y)
print(Y or Z)
print(not X)
print(not Y)
print(not Z)

#Type conversion
'''
int()
float()
str()
tuple()
set()
list()
dict()
'''

num_str="345"
print(type(num_str))

num_int=int(num_str)
print(type(num_int))

num_int=int(num_str)
print(type(num_int+10))

#Multiple Assignment

X,Y,Z=20,50,70

print(X,Y,Z)

a=75
print(id(a))

a=55
b=95
print(id(a))
print(id(b))




