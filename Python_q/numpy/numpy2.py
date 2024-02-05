import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.ndim)
arr2=np.array([[1,2,3,4]], ndmin=10)
print(arr2)

# special types of array
# array filled by 0
ar_zero=np.zeros(4)
print(ar_zero)

# array filled by 1
ar_once=np.ones(4)
print(ar_once)

# array filled by empty
# empty function then above element is fill by default
ar_ety=np.empty(4)
print(ar_ety)

# array with range
arnge=np.arange(4)
print(arnge)