lis=["shubham",45,4,'ch',123.2]
# delete function del() 
del lis[1] 

print(lis)
# pop() function it is used to delete random element from list
print(lis.pop())

# remove function which is used remove with particular element
lis.remove('ch')
print(lis)
# insert function which is used to insert the element in list
lis.insert(2,12)
print(lis)
n=[54,'dfg',548]
lis.append(n)
print(lis)

m=[454,'dfghfg',8]
lis.extend(m)
print(lis)

f=[54,5,4,6,88,1,45,36]
g=[4,21,7,99,6,4,8,3,5]
for i,j in zip(f,g):
    print(i,j)