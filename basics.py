# Pyton Basics

#Print your name

print("Hello, my name is digna")

#Add two numbers

a=10
b=20
sum=a+b
print("the sum is:",sum)

#ask users name

name=input("what is your name:")
print("name")

#simple calculater

a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multipliction:",a*b)
print("division:",a/b)

#print()formatting using sep and end

print("Apple","Pineapple","Cherry","Banana",sep="|",end="<-------end of the list\n")

#fomatting message from user input

name=input("enter your name:")
age=int(input("enter your age:"))
hobby=input("enter your fovrite hobby:")

#F-string methad

print(f"Hello,{name},At{age},enjoying{hobby}sounds fun!!!!")

#Declare variable of diffrent data type and show their types

a=60
b=15.67
c="python"
d=True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
      
#python program

subject1=input("enter 1st subject name:")
marks1=int(input("enter your marks:"))
subject2=input("enter 2nd subject name:")
marks2=int(input("enter your marks:"))
subject3=input("enter 3ed subject name:")
marks3=int(input("enter your marks:"))

#calculate total and average

total=marks1+marks2+marks3
average=total/3

#decide grade

if average>=95:
   Grade="A"
elif average>=85:
     Grade="B"
elif average>=75:
     Grade="C"
elif average>=65:
     Grade="D"
else:
    Grade="Fail"
print("\n------reslut-----")
print(f"{subject1}:{marks1}")
print(f"{subject2}:{marks2}")
print(f"{subject3}:{marks3}")
print(f"total mark:{total}")
print(f"average mark:{average}")
print(f"Grade:{Grade}")

