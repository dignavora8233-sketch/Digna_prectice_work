#3.COMPARISON OPERATORS

#Greater number between two inputs

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is", a)
else:
    print("Greater number is", b)

#Check if number is equal or not

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

#Voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is", a)
elif b >= a and b >= c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

#Pass/fail based on marks

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")





#4.LOGICAL OPERATORS

#Check if number is between 1-100

num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")

#Loing system(username+password)

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#Check leap year(multiple conditions)

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Check if number is divisible by 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")

#Validate input(age>18 and city=="surat")

age = int(input("Enter age: "))
city = input("Enter city: ")

if age > 18 and city == "Surat":
    print("Valid Input")
else:
    print("Invalid Input")
    



