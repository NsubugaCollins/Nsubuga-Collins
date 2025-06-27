class Human:
   def __init__(self):
        self.heart = 1
   def eat(self):
       print('i can eat')
   def work(self):
       print('i can work')
class Male:
    def __init__(self, name):
        self.name=name
    def flirt(self):
        print('i can flirt')
    def work(self):
        print('i can code')

class Boy(Human, Male):
    def __init__(self, name, language):
        Male.__init__(self, name)
        Human.__init__(self)
        self.language=language
    def sleep(self):
        print('i can sleep')
    def work(self):
        print('i can test')

boy = Boy('col', 'c++')
boy.eat()
boy.flirt()
boy.work()
#when i have the same methods of different super classes and i want to access the method of the second class
Male.work(boy)
print(boy.name)
print(boy.heart)
print(boy.language)
