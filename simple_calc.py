print("********  A SIMPLE CALCULATOR  *******")

def add(a,b):
    return  a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def more_cal():
    while True:
        num1 = int(input('enter the first number\n'))

        while True:
            operand = input("enter '+' for addition, '-' for subtraction, '*' for multiplication , '/' for division\n")
            num2 = int(input('enter the second number\n'))
            if operand == '+':
                results = add(num1, num2)
            elif operand == '-':
                results = subtract(num1, num2)
            elif operand == '*':
                results = multiply(num1, num2)
            elif operand == '/':
                if num2 == 0:
                    print("cant divide by zero")
                    continue
                else:
                     results = divide(num1, num2)
            print(f"Results\n {num1} {operand} {num2} = {results}")
            more = input("do you want more calculations 'yes' to 'no' to use previous output and 'x' to exit").lower()
            if more == 'yes':
                more_cal()
            elif more == 'no':
                num1 = results
                continue
            elif more =='x':
                print('goodbye...........')
                return

more_cal()
