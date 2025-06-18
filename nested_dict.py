my_dict = dict({
    'ram':{'age':8, 'home':'toru', 'course':'python'},
    'sham':{'age':10, 'home':'peru', 'course':'CS', 'phoneNo':'[070886567,778889776]'}
})
print(my_dict)
print(my_dict['sham']['phoneNo'])

def add():
    name=input("enter the name: \n")
    age=int(input("enter the age:\n"))
    home=input("enter the home:\n")
    course=input("enter your course:\n")
    my_dict[name] = {'age':age, 'home':home, 'course':course}

add()
print(my_dict)