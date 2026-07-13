print("Introduction & fundamental")
'''
#1.

print("Name:Digna")
print("Age: 18")
print("City:surat")

#2.

name=(input("Enter your name : "))
print(f"'Hello, [{name}]! Welcome to Pythpn!'")

#3.

num=int(10)
num2=float(20)
num3=bool(100)
print(type(num))
print(type(name))
print(type(num2))
print(type(num3))

#4.

a=10
b=20
c=10
print(id(a))
print(id(b))
print(id(c))

#5.

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print("Addition: " , a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Devision: ", a/b)
print("Modulus: ", a%b)
print("Exponemtion: ", a**b)
print("Floor division: ", a//b)

#6.

A=12.45
B=2.34
print(int(a),type(int(b)))

A=34.4
B=38.1
print(str(a),type(str(b)))

A=23.3
B=23.4
print(float(a),type(float(b)))

#7.

celsius=float(input("enter temperature in celsius:"))
fahrenhit=(celsius*9/5)+32
print(" temperature in fahrenhit=",fahrenhit)
'''


print("Control Structures & Looping")
'''
#1.

num=int(input("Enter a number:"))

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")


#2.

Marks = int(input("Enter marks:"))

if Marks >= 90:
    print("Grade A")

elif Marks >= 75:
    print("Grade B")

elif Marks >= 60:
    print("Grade C")

else:
    print("Fail")

#3.

day=int(input("Enter day number:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")

#4.

num=int(input("Enter a number:"))

i=1
while i <= 10:
    print(num,"x",i,"=",num*i)
    i+=1

#5.

for i in range(1,101,1):
    print(i)

#6.

rows=6

for i in range(1,rows+1):
    for j in range(i):
      print("*",end="")
    print()
'''
#7.

Secret_number = 7
Max_attempts = 3

for i in range(1, Max_attempts + 1):
    guess=int(input("Guess the number:"))
    if guess == Secret_number:
       print(f"Congratulations!")
    elif guess < Secret_number:
     print("low!")
    else:
       print("high!")
print("Game over")


       





