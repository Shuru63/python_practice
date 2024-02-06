import numpy as np 

var=np.array([1,2,3,4,5,6,7])
co=var.copy()
print("the copy of array\n")
print(var)
print(co)

print("the view of array\n")
var2=np.array([9,8,7,4,6,5,4,3,2,1])
vi=var2.view()
print(var2)
print(vi)


print("the join of array\n")
var4=np.array([9,8,7,4])
var3=np.array([19,18,17,14])
con = np.concatenate((var4, var3), axis=0) 
print(con)


print("the join of 2D array\n")
var5=np.array([[9,8,7],[4,6,5],[3,2,1]])
var6=np.array([[19,18,17],[14,16,15],[13,12,11]])
con2d = np.concatenate((var5, var6), axis=0) 
print(con2d)

print("the join using Stack of 2D array\n")
var5=np.array([[9,8,7],[4,6,5],[3,2,1]])
var6=np.array([[19,18,17],[14,16,15],[13,12,11]])
con2d = np.stack((var5, var6), axis=0) 
print(con2d)

print("the split of array\n")
var8=np.array([19,18,17,14])
con2d = np.array_split(var8,3) 
print(con2d)


print("the split of 2D array\n")
var7=np.array([[9,8,7],[4,6,5],[3,2,1]])
split2d = np.array_split(var7,3) 
print(con2d)