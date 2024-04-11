import array
array1= array.array('i',[1,2,3,4,5])

def insertArray(array,index,number):
    array.insert(index,number)
    print(array)

insertArray(array1,5,6)

def TraversalArray(array):
    for i in array:
        print(i)

TraversalArray(array1)

def AccessingArray(array, index):
    if index>= len(array):
        print("Element does not exist")
    else:
        print(array[index])
AccessingArray(array1,5)

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search(array1,3))


