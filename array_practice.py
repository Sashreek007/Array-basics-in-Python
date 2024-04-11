import array

arr1= array.array('i',[1,2,3,4,5,6])
arr2= array.array('i',[7,8,9,10])
tempList= [18,19,30]

print("Q1")

def Traversal_Array(array):
    for i in array:
        print(i)

Traversal_Array(arr1)

print("Q2")

def Array_access(array,index):
    if index >= len(array):
        print("Element does not exist")
    else:
        print(array[index])

Array_access(arr1,3)

print("Q3")

def append_array(array,element):
    array.append(element)
    print(array)

append_array(arr1,10)

print("Q4")

def insert_array(array,element,index):
    array.insert(index,element)
    print(array)
insert_array(arr1,69,4)
    
print("Q5")

def extend_array(array1,array2):
    array1.extend(array2)
    print(array1)
extend_array(arr1,arr2)

print("Q6")

def from_list(array,list):
    array.fromlist(list)
    print(array)
from_list(arr1,tempList)

print('Q7')

def Delete_element(arr,target):
        if target in arr:
            arr.remove(target)
            print(arr)
        else:
            print("Not found")

Delete_element(arr1,7)

print('Q8')

def remove_lastelement(array):
    array.pop()
    print(array)
remove_lastelement(arr1)

print('Q9')

def search_index(array,target):
    print(array.index(target))
search_index(arr1,69)

print('Q10')

def reverse_array(array):
    array.reverse()
    print(array)
reverse_array(arr1)

print('Q11')

print(arr1.buffer_info())

print('Q12')
print(arr1.count(1))

print('Q13')

tempstr= arr1.tobytes()
print(tempstr)
inttemp= array.array('i')
inttemp.frombytes(tempstr)
print(inttemp)

print('Q14')

print(inttemp.tolist())

print('Q15')

print(arr1[0:4])
