class Instructor:
    def __init__(self, name, address):
        self.name=name
        self.address=address

# object of the class
instructor_1 = Instructor('collins', 'kla')
print(instructor_1.name + " " + instructor_1.address)

instructor_2 = Instructor('john', 'wande')
print(instructor_2.name + " " + instructor_2.address)
