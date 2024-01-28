# # string input
a=input("enter the first number : ")
b=input("enter the seconf number : ")
print(a+b)

# # # integer inputs
c=int(input("enter the first number : "))
d=int(input("enter the seconf number : "))
print(c+d)

# # # float inputs

e=float(input("enter the first number : "))
f=float(input("enter the seconf number : "))
print(e+f)


# # # eval() inputs
g=eval(input("enter the first number : "))
h=eval(input("enter the seconf number : "))
print(g+h)

# play with string 
str="shubham kumar garg"
print(str)
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[:])
print(str[0:])
print(str[:7])
print(str[1:8])
print(str[0::2])
t=len(str)
for i in range(t):
    print(str[i])

lw=str.lower()
up=str.upper()
ti=str.title()
cap=str.title()
print(lw)
print(up)
print(ti)
print(cap)