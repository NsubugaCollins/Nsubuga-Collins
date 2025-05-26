class A:
    def show(self):
        print("A method")
        super().show()

class B:
    def show(self):
        print("B method")
        super().show()

class C:
    def show(self):
        print("C method")

class D(A, B, C):
    def show(self):
        print("D method")
        super().show()

# Create object of class D and call show()
obj = D()
obj.show()
