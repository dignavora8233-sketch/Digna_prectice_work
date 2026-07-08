# Basic pattern in pyathon

#1.Without space pattern
'''
size=6
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()
'''
#2.Right Angled Triangle pattern
'''
size=6
for i in range(1,size+1):
    for j in range(i):
        print("*",end="")
    print()
'''
#3.Inverted Right Angle Triangle pattern
'''
size=6
for i in range(size,0,-1):
    for j in range(i):
        print("*",end="")
    print()
'''
#4.With space pattern

rows=5

for i in range(1,rows + 1):
    print(" "*(rows -i),end="")
    if i == 1:
        print("*")
    
    else:
        print("*" + " " *(2 * i-3)+ "*")


for i in range(rows-1,0,-1):
    print(" "*(rows -i),end="")
    if i == 1:
        print("*")
   
    else:
        print("*" + " " *(2 * i-3)+ "*")
