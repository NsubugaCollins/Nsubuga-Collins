student = {
    'mark':78,
    'james':35,
    'kelvin':90,
    'casey':81,
    'babra':64
}

mark_dict = {}
for stud in student:
    marks = student[stud]
    if marks >= 90:
        mark_dict[stud]="A+"
    elif marks > 80:
        mark_dict[stud]="B"
    elif marks > 70:
        mark_dict[stud]="C"
    elif marks > 60:
        mark_dict[stud]="C"
    elif marks > 50:
        mark_dict[stud]="D"
    elif marks > 40:
        mark_dict[stud]="E"
    elif marks < 40:
        mark_dict[stud]="F"

print(mark_dict)

