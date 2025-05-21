countries= ["uganda", "kenya", "rwanda", "sudan"]
'''
a=countries.copy()
print("original list : ", countries)
print("its copy :", a)
countries.sort()
print(countries)
countries.reverse()
print(countries)
'''

for country in countries:
    if 'd' in country:
        print(country, end=" ")
'''
for country in countries:
    print(country)

for country in countries:
    print(country, end=" ")
    print(country, end=" ")
'''