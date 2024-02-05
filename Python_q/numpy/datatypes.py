import numpy as np
var=np.array([1,2,3,4,5,6])
print(var)
print("data types=",var.dtype)

var1=np.array([1.2,2.3,3.3,4.1,5.9,6.4])
print(var1)
print("data types=",var1.dtype)
# change into
var2=np.array(['p','r','h','d',"f",'s'])
print(var2)
print("data types=",var2.dtype)
# change into float
var3=np.array([1,2,3,4,5,6])
new_arr=np.float32(var3)
print(new_arr)


