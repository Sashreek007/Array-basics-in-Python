import numpy as np

arr1= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

arr2= np.insert(arr1,0,[[40,42,78,91]],0)
print(arr2)

arr3= np.append(arr1,[[40,42,78,91]],0)
print(arr3)

def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traversal(arr1)

def access_element(array,row,column):
    if row >= len(array) or column>= len(array[0]):
        print("Not possible")
    else:
        print(array[row][column])
access_element(arr1,2,2)

def linear_search(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if target == array[i][j]:
                return str(i),str(j)
    return "Doesn't exist"
print(linear_search(arr1,15))

arr4= np.delete(arr1,0,1)
print(arr4)