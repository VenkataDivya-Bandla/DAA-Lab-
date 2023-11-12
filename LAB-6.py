#LAB-6
#sort the  given matrix and replace diagnols with zero
import numpy as np


values =[7,6,5,1,2,3,8,4,9]


matrix = np.array(values).reshape(3, 3)
print(matrix)
for i in range(len(values)-1):
    for j in range(i+1,len(values)):
        if values[i]>values[j]:
            temp=values[i]
            values[i],values[j]=values[j],values[i]
matrix = np.array(values).reshape(3, 3)
print(matrix)
            
for i in range(4):
    for j in range(4):
        if(i==0 and j==0):
            matrix[i][j]=0
            print(matrix)
for i in range(4):
    for j in range(4):
        if(i==1 and j==1):
            matrix[i][j]=0
            print(matrix)
for i in range(4):
    for j in range(4):
        if(i==2 and j==2):
            matrix[i][j]=0
            print(matrix)
for i in range(4):
    for j in range(4):
        if(i==0 and j==2):
            matrix[i][j]=0
            print(matrix)
for i in range(4):
    for j in range(4):
        if(i==2 and j==0):
            matrix[i][j]=0
            print(matrix)





#Integer Multiplication without Operators
def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply(x, y - 1)
    if y < 0:
        return -multiply(x, -y)
    


result = multiply(5, 3)
print(result) 