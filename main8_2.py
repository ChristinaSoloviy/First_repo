"""Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: month - номер місяця 
у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, 
що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
"""
from datetime import date


def get_days_in_month(month, year):
    days_count = 26
    days_max = 31
    try:
        for d in range(days_count, days_max+2):
            target_date = date(year=year, month=month, day=d)
            print(target_date)
            days_count += 1
    except Exception as error:
        print(error)

    return days_count - 1


result = get_days_in_month(2,2021)
print(result)
   