from student import Student
from group import Group
from exceptions import GroupLimitError

st1 = Student('Male', 30, 'Ded', 'Moroz', '2026')
st2 = Student('Female', 25, 'Snejnaya', 'Koroleva', '2026')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Moroz') == st1
assert gr.find_student('Moroz2') is None
assert isinstance(gr.find_student('Moroz'), Student)

gr.delete_student('Koroleva')
print(gr)

gr.delete_student('Koroleva')

try:
    for i in range(9):
        gr.add_student(Student('Male', 20, f'Name{i}', f'Last{i}', f'RB{i}'))
except GroupLimitError as e:
    print(e)
