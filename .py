#1.VARIABLES & BASIC INPUT PROGRAMS

#Store and print name,age,and city

print("Hello,My name is digna!")
print("I am 18 years old!")
print("I am from surat!")

#Take user input and display formatted output

name=input("what is your name:")
age=input("what is your age:")
city=input("which city do you live in:")

print("Name:",name)
print("Age:",age)
print("City:",city)

#Swap two varibles

a = input("Enter first value: ")
b = input("Enter second value: ")

print("Before swap")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swap")
print("a =", a)
print("b =", b)

#Square and cube of a number

num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)

#Convert temperature

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)




#2.ARITHMETIC OPERATORS

#Simple calculator(+,-,*,/)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

#Find remainder using%

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Remainder =", a % b)

#Calulate area of rectangle/circle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of Circle =", area)

#Calulate simple interest

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)

