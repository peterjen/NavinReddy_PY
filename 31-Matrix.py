from numpy import *

arr1 = array([
    [1,2,3],
    [4,5,6]
])

print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

# CONVERT 2-D array to 1-D array
arr2 = arr1.flatten()
print(arr2)

# CONVERT 1-D array to 2-D array
arr3 = arr2.reshape(3,2)
print(arr3)


# MATRIX
print('MATRIX ##########')

m = matrix(arr3)
print(m)

m = matrix('1,2,3;4,5,6;7,8,9')
print(m)

m1 = matrix('1,2,3;4,5,6;7,8,9')
m2 = matrix('11,22,33;44,55,66;77,88,99')

print(m1 + m2)
print(m1 * m2)





