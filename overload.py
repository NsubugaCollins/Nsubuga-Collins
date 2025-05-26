def add(a=None, b=None):
    #checks if all the arguments are available
    if a != None and b == None:
        print(a)
    else:
        print(a+b)

add(2,4)
add(2)

# real life example
class Payment:
    def pay(self, amount=None, method=None):
        if amount == None and method == None:
            print("no payment details provided")
        elif method == None:
            print(f"paid {amount} using default method (cash)")
        else:
            print(f"paid {amount} using {method}")

p = Payment()
p.pay()
p.pay(100)
p.pay(250, "credit card")
