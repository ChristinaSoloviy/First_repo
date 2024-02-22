"""Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику. 
Першим параметром у функцію ми передаємо словник, 
а другим — значення, що хочемо знайти. Таким чином, результат може бути як список ключів, 
так і порожній список, якщо ми нічого не знайдемо.
"""
data = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
def lookup_key(data, value):
    result = []
    for grade_str, grade_value in data.items():
        print(grade_str, grade_value)
        if grade_value == value:
            result.append(grade_str)
    print(result)          
    return result      



lookup_key(data,6)        