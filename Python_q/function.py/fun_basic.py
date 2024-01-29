# normal and basic function
def sum(a,b):
    return a*b

s=sum(4,3)
print(s)

def sqr(sq):
    return sq*sq

sq=int(input("enter the number of : "))
print(sqr(sq))

# default argument in function
def default(n1,n2=40):
    print("the N1 is :",n1)
    print("the N2 is :",n2)
    print(n1+n2)
    

d=default(20,30)
e=default(20)

any=lambda a,b:a*b
print("anonymous function multiply")
print(any(4,5))

print("anonymous function sqr")
any=lambda a,b:a**b
print(any(5,2))