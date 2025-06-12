def me(**details):
    for key, value in details.items():
        print(key, value, end=" ")

me(name = 'kelly', age=5, hobby='swimming')
me(name = 'essy')