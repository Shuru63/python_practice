import numpy as np

x=np.array([1,2,3,4,5])
print(x)
print(type(x))
y=[1,5,4,3,7,9,5,78,5,56,4,63,5]
ar=np.array(y)
print(ar)

l=[]
for i in range(1,6):
    a=int(input("enter"))
    l.append(a)

list_Ar=np.array(l)
print(list_Ar)