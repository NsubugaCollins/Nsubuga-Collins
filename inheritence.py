from numpy.polynomial.hermite_e import hermex


class Human:
    def __init__(self, heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print('i can eat')
    def work(self):
        print('i can work')

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name=name

    def flirt(self):
        print('i can flirt')
    def work(self):
        super().work()
        print('i can code')

male_1 = Male('kelly', 1)
male_1.eat()
male_1.work()
male_1.flirt()
print(male_1.eyes)
print(male_1.heart)