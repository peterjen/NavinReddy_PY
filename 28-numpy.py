import numpy as np
from numpy import *
a = array([1, 2, 3])
print(a)
print(a.dtype)

a = array([1, 2, 3],float)
print(a)
print(a.dtype)

# 2-D array
a = array([[1, 2, 3],[4,5,6]])
print(a)

# linspace - break 1 to 15 into 10 parts (by default: devide to 50 parts
# LINSPACE(START,END,PARTS<default 50>)
arr = linspace(0,15,10)
print(arr)

arr = linspace(0,15)
print(arr)

# arange - from 1 to 15 skip every 2 steps
# ARANGE(START,END,STEP)
arr = arange(1,15,2)
print(arr)

#logspace - ???????

arr = logspace(1,15,5)
print(arr)

# zeors / ones

arr = zeros(10)
print(arr)

arr = ones(10,int)
print(arr)