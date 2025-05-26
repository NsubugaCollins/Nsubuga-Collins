class Animal:
    def speak(self):
        print("animal makes sound")

 #subclass
class Cat(Animal):
    def sound(self):
        print("cat moew")

#create object
cat1 = Cat()
#call inherited method
cat1.speak()
#call subclass method
cat1.sound()
