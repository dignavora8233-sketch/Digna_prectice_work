#Global keyword in python
'''
total = 0

def increment():
    global total
    total +=1

increment()
increment()
increment()
increment()
increment()
print(total)
'''
#Multiple return values

def calculation(A, B, C):

    total = A + B + C

    average = total / 3

    maximum = max(A , B , C)

    minimum = min(A , B , C)

    return total , average , maximum , minimum

total , average , maximum , minimum = calculation(5 , 10 , 15)

print(total)
print(average)
print(maximum)
print(minimum)


