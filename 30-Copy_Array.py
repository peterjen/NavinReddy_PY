from numpy import *
import math as math

arr = array([1,2,3,4,5])
arr = arr + 5
print(arr)

arr2 = array([1,2,3,4,5])
arr3 = arr + arr2
print(arr3)

print(sum(arr2))
print(sin(arr2))
print(max(arr2))
print(sqrt(arr2))
print(concatenate([arr, arr2]))

#### COPY ARRAY
arr = array([2,4,6,8])
arr2 = arr
print(arr, id(arr))
print(arr2, id(arr2))  # both have same id
arr[0] = 99
print(arr)   #[99  4  6  8]
print(arr2)  #[99  4  6  8]  both array changed

#################### SHADOW COPY
arr = array([2,4,6,8])
arr2 = arr.view()          # SHADOW COPY
print(arr, id(arr))
print(arr2, id(arr2))  # have different id
arr[0] = 99
print(arr)   #[99  4  6  8]
print(arr2)  #[99  4  6  8]  BUT both array changed



#################### DEEP COPY
arr = array([2,4,6,8])
arr2 = arr.copy()          # DEEP COPY
print(arr, id(arr))
print(arr2, id(arr2))  # have different id
arr[0] = 99
print(arr)   #[99  4  6  8]
print(arr2)  #[99  4  6  8]