#LAB-4
#Diagonal Interchange
import numpy as np


values = [0, 1, 2, 3,4, 5, 6, 7, 8]


matrix = np.array(values).reshape(3, 3)

print(matrix)
for i in range(3):
    for j in range(3):
        matrix[0][0],matrix[0][2]=matrix[0][2],matrix[0][0]
        matrix[2][0],matrix[2][2]=matrix[2][2],matrix[2][0]
print(matrix)


#Index Finder
def index(arr, num):
    indices = []
    for i in range(len(arr)):
        if arr[i] == num:
            indices.append(i)
    return indices

arr= [ 2, 7, 3, 9, 4, 5]
num= 4
print("find the element index:",index(arr, num))