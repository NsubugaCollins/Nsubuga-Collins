phone_number = {'ram': 123, 'syma': 456, 'mohan': 789}
print(phone_number['ram'])

phone = dict({'ram': 123, 'syma': 456, 'mohan': 789})
print(phone)
#changing values in the dictionary
phone['ram']=999
print(phone)
#adding an item and a dictionary in a dictionary
phone['kevo'] = {1111, 2222, 3333}
print(phone)
for i, j in phone.items():
    print(f"{i}:{j}", end=",")