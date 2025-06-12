import math

def painting(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area/cover)
    print(f"number of cans is {no_of_cans}")

height = int(input("enter the height: "))
width = int(input("enter width: "))
coverage = 7

painting(height=height, width=width, cover=coverage)

