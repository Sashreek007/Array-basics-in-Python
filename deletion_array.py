import array

arr1= array.array('i',[1,2,3,4,5])

def Delete_element(arr,target):
        if target in arr:
            arr.remove(target)
            print(arr)
        else:
            print("Not found")

Delete_element(arr1,7)
            