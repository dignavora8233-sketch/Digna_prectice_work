#5.ASSIGNMENT OPERATORS

#Increment and decrement a number

num = int(input("Enter a number: "))

num += 12
print("After Increment:", num)

num -= 15
print("After Decrement:", num)

#Use+=,-=,*= in calculation

num = int(input("Enter a number: "))

num += 10
print("After += 10:", num)

num -= 54
print("After -= 5:", num)

num *= 23
print("After *= 2:", num)

#Create running total

total = 0

total += 100
print("Total:", total)

total += 200
print("Total:", total)

total += 300
print("Total:", total)

#Salary increment calcuation

salary = 50000

salary += 5000

print("New Salary =", salary)

#Discount calcution using assignment operators

price = 3000

price -= 200

print("Price After Discount =", price)



#6.MIXED PRACTICE

#Student marks-total & average

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("Total =", total)
print("Average =", average)

#Bill generator(price+tax)

price = float(input("Enter price: "))
tax = float(input("Enter tax %: "))

bill = price + (price * tax / 100)

print("Total Bill =", bill)

#Age calculator

birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year

print("Your age is", age)

#Even/odd+posotive/negative check

um = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

#Mini calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
