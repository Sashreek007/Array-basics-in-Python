import numpy as np

twod= np.array([[1,2,4],[3,5,6],[7,8,9]])
print(twod)
def Access_element(array,row,column):
    if row>= len(array) or column>=len(array[0]):
         print('Does not exist')
    else:
        print(array[row][column])
       
Access_element(twod,2,3)

def Array_traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
Array_traversal(twod)

def Searching(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== target:
                return str(i),str(j)
        return 'not found'
            
print(Searching(twod,4))
