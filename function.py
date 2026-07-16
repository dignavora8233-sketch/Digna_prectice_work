#Arbitrary Arguments(*args)

#Write a python function that accept any number of arguments and return their sum.

def addition (*args):
    total=0

    for i in args:
        total += i

        return total
print(addition (10,20,40,50))

#Keyword Arguments(**kwargs)

#Write a Python function that accept student information using keyword arguments and prints all student details.

def student(**kwargs):
   print("Student Details")

   for key , value in kwargs.items():
           print(f"{key} : {value}")

student(Name="Digna" , Age=17 , city="Surat")

# doc (Documentation String)

# Write a function to calculate the area of a rectangle and display its Documentation.

def rectangle(length , width):
    """
    Function Name : reactangle

    Purpose:
        Calculate rectangle area.

    Parameter:
        length : int
        width : int
        
    Return:
        Area of rectangle
    """
    return length * width

print("Area : " , rectangle(20 , 20))

print(rectangle.__doc__)

#Lambda with map()

num=[10,20,30,40]

result=list(map(lambda X : X ** 2 , num))

print(result)

#Lambda with filter()

numbers=[5,10,15,20]

even = list(filter(lambda X:X % 2 == 0 , numbers))

print(even)

#Lambda with sorted()

students = [("Digna",17) , ("Riva",18) , ("Mansi",19)]

print(students)

result = sorted (students , key = lambda X:X [0])

print(result)

    
