class Human:
    def __init__(self, name, age):
        self.age=age
        self.name=name
    def show(self):
        print(f"my name is {self.name} and i am {self.age} years old")
    def eat(self):
        print('i can eat')

class Male(Human):
    def sleep(self):
        print('i can sleep')

class Female(Human):
    def __init__(self,gender,name, age):
        Human.__init__(self,name,age)
        self.gender= gender
    def work(self):
        print('i can work')

fem = Female('female', 'job', 2 )
fem.show()
print(fem.gender)