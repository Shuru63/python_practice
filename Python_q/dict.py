dic={"name":"shubham",
     "age":54,
     "dob":"26/05/2004",
     "roll_no":432}
print(dic)
print(dic["age"])
print(dic["name"])
print(dic["roll_no"])
for i in dic:  
    print(i)
    print(dic[i])

print("get function of dictionary")
print(dic.get("name"))


print("key of dictionary")
for a in dic.keys():
    print(a)    
print("values of dictionary")
for a in dic.values():
    print(a)      

print("items of dictionary")
for a in dic.items():
    print(a)      



dict={"shubham" :{
    "marks":5.71 , "dept":"cse", "gf":"no"
},
"manikant" :{
    "marks":9.71 , "dept":"CSE", "gf":8
},"raushan" :{
    "marks":8.71 , "dept":"it", "gf":5
},"deepanshu" :{
    "marks":6.71 , "dept":"it", "gf":1
}}
print(dict)

print(dict["manikant"])
print(dict["deepanshu"]["marks"])

for k,v in dict.items():
    print(k,v)