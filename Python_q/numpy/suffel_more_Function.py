import numpy as np 

var=np.array([1,2,3,2,4,5,6,7,4,2,5,4,1,2,3,4,3,5,6,7])
x=np.unique(var)
print(x)
print("the unique element of array")
y=np.unique(var,return_index=True)
print(y)

