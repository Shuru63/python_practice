import numpy as np
var=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(var)
sh=var.shape
print(sh)

# ndmin function
print("other function")
var1=np.array([1,2,3,4,5],ndmin=4)
print(var1)
vsh=var1.shape
print(vsh)

var2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_array = var.reshape(3, 3)
print(reshaped_array)

