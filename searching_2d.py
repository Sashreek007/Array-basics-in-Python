import numpy as np

twod = np.array([[1, 2, 4], [3, 5, 6], [7, 8, 9]])

def Searching(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return str(i), str(j)
    return 'not found'

print(Searching(twod, 2))
