#Sets, Dictionary, Type coversion, List of Dictionary

print("*" * 50)
print("1.Set Operations")
print("*" * 50)

numbers={1,2,3,4,5,6}

print(type(numbers))

numbers.add (7)

numbers.remove (4)

print("Is 5 present?",5 in numbers)

print("*" * 50)
print("2.Union, Intersection and Difference")
print("*" * 50)

set_1 = {'A','B','C','D'}
set_2 = {'C','D','E','F'}

print(set_1)

print(set_2)

print("Union:",set_1.union(set_2))

print("Intersection:",set_1.intersection(set_2))

print("Difference:",set_1.difference(set_2))

print("Difference:",set_2.difference(set_1))

print("*" * 50)
print("3.Dictionary operation")
print("*" * 50)

student={
          "Name":"Digna",
          "Age":17,
          "Grade":"A"
          }

for key in student.keys():
    print(f"{key}:{student[key]}")

for value in student.values():
    print(value)

print(student['Name'])

student["city"]='Surat'

student["Age"]=18

del student["Grade"]

print(student)

print("*" * 50)
print("4. Dictionary from Lists")
print("*" * 50)

keys = ['id' , 'name' , 'email']

values = [101 , 'Raja' , 'tdd@gmail.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

print(user)

print("*" * 50)
print("5. Type Conversion")
print("*" * 50)

num='315'

print(type(num))

num=int(num)

print(type(num))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)

tuple_1 =['A','B','C']

list_1 = list(tuple_1)

print(list_1)

pairs = [(1 , "ab") , (2 , "AB")]

print(dict(pairs))





          



    
