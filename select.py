#this program selects a random name from the provided list
import random
names = input("enter the names separated by commas:")
names_split = names.split(",")
length = len(names_split)
c=random.randint(0, length-1)
print(c)
print(f"{names_split[c]} will pay")