# set is a mutable data types

st={"monday",45,"tuesday",54,"shubham",68,55,21,55,445,68,55,55,45}
print(st) 
print(type(st))
l=[45,54,24,64,25,44,55,6,6,45,54,24.64]
print(l)
# set() function is used to tupple,list change into set
print("list change into tupple")
s=set(l)
print(s)
# add() function is used to add the element in set
print("add() function ")
s.add(400)
print(s)

# pop() function is used to delete the random element from set
print("pop() function ")
t=s.pop()
print(t)
print(s)
 
# remove() function is used to remove specialy element from set
print("remove() function ")
s.remove(45)
print(s)

#discard() function is used to deleted specific element
print("discard() function ")
de=s.discard(25)
print(de)
print(s)

print("update() function ")
St={10,20,30,40,50}
l={60,70,80,90}
St.update(l)
print(St)
