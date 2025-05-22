size= input("which size do u want(S/M/L)")
bill = 0
if size == "s" or size == "S":
    bill += 500
    print(f"the price of the small size is {bill}")
elif size =="m" or size =="M":
    bill += 2000
    print(f"the price of the medium size is {bill}")
else:
    bill += 5000
    print(f"the price of the large size is {bill}")

refreshment = input("Do you want a refreshment(Y/N)")
if refreshment == "y" or refreshment == "Y":
    bottle= input("which size do you want(S/L)")
    if bottle == "s" or size == "S":
        bill +=120
    if bottle == "l" or size == "L":
        bill += 200
else:
    print("no refreshment required")

print(f"your final bill is {bill}")
