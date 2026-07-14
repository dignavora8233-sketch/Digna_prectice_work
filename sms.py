#Student Mengement System



students=[
      {"id":101,"name":'Riva',"score":89},
      {"id":102,"name":'Mansi',"score":80},
      {"id":103,"name":'Sakshi',"score":69}
    ]

print(students)

print("*"*50)
print("Student name list")
print("*"*50)

for student in students:
    print(student["name"])

print("*"*50)
print("Student Average score")
print("*"*50)

sum = 0
for student in students:
    sum += student['score']

average = sum/3

print("\n Average student score :",average)

print("*"*50)
print("Add New student")
print("*"*50)

students.append({
       "id":104,
       "name":"Palak",
       "score":90
      })
print(students)

print("*"*50)
print("Updete Student score")
print("*"*50)

for student in students:
    if student['id'] == 103:
          student['score']=88

print(students)

print("*"*50)
print("Remove Students from list")
print("*"*50)

for student in students:
    if student['name'] == 'Sakshi':
       students.remove(student)
       break;

print(students)

print("*"*50)
print("Students score>80")
print("*"*50)

for student in students:
    if student['score']>80:
        print(student['name'])

print("*"*50)
print("Sort Decending")
print("*"*50)



    

