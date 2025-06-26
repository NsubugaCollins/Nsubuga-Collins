from oop_concepts import instructor_1


class Instructor:
    followers=0
    def __init__(self, name, address):
        self.name=name
        self.address=address

    def display(self, subject):
        print(f'hi, am {self.name} and i teach {subject}')

    def update_followers(self, follower_name):
        self.followers += 1
instructor_1 = Instructor('call','kla')
instructor_1.display(3)
instructor_1.update_followers('pal')
print(instructor_1.followers)