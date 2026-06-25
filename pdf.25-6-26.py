#Variables & Basic Input Progams

#store and print name,age,city
print("Hello,my name is Digna!!")
print("i am 18 years old!")
print("i live in surat,gujrat!")

name=input("what is your name:")
age=input("what is your age:")
city=input("which city do you live in:")

#take user input and display formatted output
print(name)
print(age)
print(city)

#swap two variables
a=50
b=70

print("Before swap")
print("a=",a)
print("b=",b)

a,b=b,a

print("After swap")
print("a=",a)
print("b=",b)

#find square and cube of a number
num=int(input("enter a number:"))
square=num**3
cube=num**7

print("square=",square)
print("cube=",cube)

#convert temperature
celsius=float(input("enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("temperature in fahrenheit=",fahrenheit)


#Arithmetic Opeartors

#simple calculator(+,-,*,/)

a=50
b=80

print("addition:",a+b)
print("substaction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)


#Comparison Opeartors

#greater number between two inputs

a=int(input("enter first number:"))
b=int(input("enter second number:"))

if a>b:
    print("greater number is:",a)
else:
    print("greater number is:",b)

#number is equal or not

a=int(input("enter first number:"))
b=int(input("enter second number:"))

if a==b:
    print("both numbers are equal")
else:
     print(" numbers are not equal")

#voting eligibility(age>=18)

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

#largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#pass/fail based on marks

marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")
