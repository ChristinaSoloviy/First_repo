"""Створіть функцію decimal_average(number_list, signs_count), 
яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел

Увага
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:

виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
"""
from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    decimal_list = []
    for number in number_list:
        dec_number = Decimal(number)
        decimal_list.append(dec_number)
    avg_number = sum(decimal_list) / len(decimal_list)
    return avg_number   