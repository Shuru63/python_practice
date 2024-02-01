class bike:
    def __init__(self,stock) :
        self.stock=stock

    def displaybike(self):
        print("total bike : ",self.stock)

    def ren_on_bike(self,q):
        if q<0:
            print("enter the positive value or greater then zero ")

        elif(q>self.stock):
             print("enter the positive value or greater then zero ")

        else:
             print("sorry kuch nhi hai")

while True:
    obj=bike(100)
    uc=int(input("1 display stock \n2 bike for rent \n3 out of program"))
    if(uc==1):
        obj.displaybike()
    elif(uc==2):
        n=uc=int(input("enter the number of bike: "))
        price=n*50
        print("the price of bike :",price)
    else:
        break
