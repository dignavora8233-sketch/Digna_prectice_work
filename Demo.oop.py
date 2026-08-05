class Student:

# contsructor

  def __init__(self , name=None , age=None , dob=None , marks=None):

    #user
    self.name = name
    self.age = age
    self.dob = dob
    self.marks = marks
   

  def User_Details(self):
    print(f"""
    Name : {self.name}
    Age : {self.age}
    DOB : {self.dob}
    Marks : {self.marks}
    """)

student1 = Student("Digna" , 17 , "01-01-2009" , 85)

student1.User_Details()


# Simple Creation

class Person:

  pass

p1 = Person()

print(type(p1))


class Person:

  name = "DIGNA"

  age = 17

  course = "AI"

p1 = Person()

print(p1.name)
print(p1.age)
print(p1.course)
