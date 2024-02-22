""" Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. 
Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна повернути рядок наступного виду 'first second'.
"""
import sys


def parse_args():
    result = ""
    input_data = sys.argv
    input_data.pop(0)
    print(input_data)
    if input_data != []:
       result = " ".join(input_data)
    
        
            
        
    return result


answer = parse_args()
print(answer)

