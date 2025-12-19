from exceptions import GroupLimitError


class Group:
    def __init__(self, number):
        self._number = number
        self._students = set()

    def add_student(self, student):
        if len(self._students) >= 10:
            raise GroupLimitError('Group limit exceeded')
        self._students.add(student)

    def find_student(self, last_name):
        for student in self._students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self._students.remove(student)

    def __str__(self):
        students_str = '\n'.join(str(student) for student in self._students)
        return f'Group {self._number}:\n{students_str}'
