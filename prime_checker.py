def prime_check(number):
    is_prime = True
    if number==1:
        is_prime=False
    for i in range(2, number):
        if number % i ==0:
            is_prime = False
    if is_prime ==True:
        print("it is a prime number")
    else:
        print('its not a prime number')

n = int(input('enter the number\n'))
prime_check(n)

