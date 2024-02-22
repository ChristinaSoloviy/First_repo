"""Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у 
вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
Перетворене значення функція повертає під час виклику.
"""
from datetime import datetime

# Thursday 27 May 2021
# 2021-05-27 17:08:34.149Z
def get_str_date(date):
    only_date = date.split(' ')[0]
    date_object = datetime.strptime(only_date, '%Y-%m-%d')
    return date_object.strftime('%A %d %B %Y')