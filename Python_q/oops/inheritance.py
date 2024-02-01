class animal:
    def speak(self):
        print("shubham")

class dog:
    def kuta(self):
        print("manikant")

class all(dog,animal):
    def child(self):
       print("harkirat sir")  

obj=all()
obj.child()
obj.speak()
obj.kuta()