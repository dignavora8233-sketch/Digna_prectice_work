#Conrol Flow in Python

#Statnments in python

'''
1.if statnment
2.if....esle statnment
3.if....elif....esle statnment
4.match statnment
5.continue statnment
6.break satanment
'''

#1.if statnment

#The if satanment executes a block of code only if the specified condition is True. if the condition is false,the code inside the if blocks skipped.

'''
if condition:
     # code
'''

age=18
if age>=18:

    print("you are eligible to vote.")

#2.if....esle statnment

#The if....esle statnment is used when there are two possible outcomes:
#if the condition is Truw, the if block executes.
#if the condition is false, the esle block executes.

'''
is condition:
    #code
esle:
    #code
'''

number=60

if number>=55:
    print("positive number")
else:
    print("negative number")

#3.if....elif....else statnment

#is....elif....else statnment is used when multiple condition need to be checked.

'''
if condition1:
        #code
elif condition2:
        #code
elif condition3:
        #code
else condition4:
        #code
'''

marks=99

if marks>=90:
    print("Grade A")
elif marks>80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
else:
    print("Fail")

#4.match-case statnment

num1=90
num2=80
num3=70

operator=input("enter your opeartor sign:")

match operator:
    case "+":
        print("Addition:",num1+num2+num3)
    case "-":
        print("Substraction:",num1-num2-num3)
    case "**":
        print("Exponentiation:",num1**num2**num3)
    case "//":
        print("Floor division:",num1//num2//num3)
    case _:
        print("Invalid operator!!")

#Multiple Values in One Case Use

char="a"

match char:
    case "a" | "e" | "i" | "o" | "u" :
        print("vowel")
    case _:
        print("Consonents")
        
        

    

    
          

    

