class Human:
    def __init__(self,heart):
        self.heart=heart
    def eat(self):
        print('i can eat')
    def work(self):
        print('i can work')

class Male(Human):
    def __init__(self, name):
        self.name= name
    def sleep(self):
        print('i can sleep')

class Boy(Male):
    def __init__(self, play,heart, name):
      Human.__init__(self, heart)
      Male.__init__(self, name)
      self.play=play
    def work(self):
        Human.work(self)
        print('i can code')


boy_1 = Boy('football', 1, 'job')
boy_1.work()
print(boy_1.heart)
print(boy_1.play)
print(boy_1.name)
