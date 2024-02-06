import numpy as np 
var=np.array([1,2,3,4,5,6,7,8,9])
print("\nthe searching of element of array\n")
x=np.where(var==2)
print(x)

y=np.where(var%2==0)
print(y)

print("\nthe searchsort of element of array\n")
z=np.searchsorted(var,5)
print(z)

print("\nthe sort of element of array\n")
var1=np.array([6,2,8,3,5,7,4,1,9,87,14,58,68])
sort=np.sort(var1)
print(sort)

print("\nthe filter of element of array\n")
str=np.array(['a','d','r','e','a','f','s','x','b','we','df'])
sort=np.sort(str)
print(sort)