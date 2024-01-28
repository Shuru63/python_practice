# play with list
lis=["shubham",45,4,'ch',123.2]
print(lis)
print(type(lis))
print(lis[2])
# iteration with list
for i in lis:
    print(i)

# indexing 
l=[2,3,"hello",[5,4,"pass",54]]
print(l)
print(l[3])
print(l[0:2])
print(l[0::2])

# iteration using range
t=len(l)
for i in range(t):
    print(l[i])
    t=len(l)

print(l[3][2])

t=len(l)
for i in range(t-1,-1,-1):
    print(l[i])
    t=len(l)

lis1=[45,54,"sdf",4]
lis2=[25,24,"ert",23]
# concatenation and memmber of list
m=lis1+lis2
print(m)
print(200 in m)
print(45 in m)
do=2*lis1
print(do)



