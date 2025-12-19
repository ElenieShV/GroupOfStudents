class Human:
    def __init__(self, gender, age, first_name, last_name):
        self._gender = gender
        self._age = age
        self._first_name = first_name
        self._last_name = last_name

    @property
    def last_name(self):
        return self._last_name

    def __str__(self):
        return f'{self._first_name} {self._last_name}, {self._age} y.o., {self._gender}'
