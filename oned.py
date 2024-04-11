import array

arr1 = array.array('i', [1,2,3,4,5,6,7])

def insert_array(array,number,index):
    if index>=len(array)+1:
        print("Cannot do it")
    else:
        array.insert(index,number)
        print(array)
insert_array(arr1,21,2)

def traversal_array(array):
    for i in array:
        print(i)
traversal_array(arr1)

def access_array(array,index):
    if index >= len(array):
        print("Cannot be found")
    else:
        print(array[index])
access_array(arr1,0)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
        
print(linear_search(arr1,21))

def delete_element(array,target):
    if target in array:
        array.remove(target)
        print(array)
    else:
        print('not found')

delete_element(arr1,21)