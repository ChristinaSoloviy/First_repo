"""Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
"""

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        counter = 0
        for i in self.data:
            if i.isdigit():
                counter += 1
        return counter    
