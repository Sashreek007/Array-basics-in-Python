import array
array1= array.array('i',[1,2,3,4,5])

def Access_Array(array, index):
    if index>= len(array):
        print("This element does not exist")
    else:
        print(array[index])

Access_Array(array1,5)