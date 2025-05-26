class Bird:
    def fly(self):
        print("bird flies")

class Eagle(Bird):
    def fly(self):
        print("flies higher")

class Duck(Bird):
    def fly(self):
        print("fly lower")

#polyorphism
def test(bird):
    bird.fly()

#create objects
e = Eagle()
d = Duck()

#calling methods
test(e)
test(d)
