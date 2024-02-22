"""У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. 
Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи. 
Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням 
та повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
"""
def data_preparation(list_data):
    result_list = []
    for list in list_data:
        in_process = True
        delete_min = False
        delete_max = False
        while not (delete_min and delete_max):
            if len(list) <= 2:
                break
            else:
                if delete_min is False:
                    min_number = min(list)
                    list.remove(min_number)
                    delete_min = True
                elif delete_max is False:
                    max_number = max(list)
                    list.remove(max_number)
                    delete_max = True
        result_list.extend(list)
   
    return sorted(result_list, reverse=True)                

                

