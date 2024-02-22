""" У нас є список показників студентів групи – це список з отриманими балами з тестування. 
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), 
знаходить середнє значення бала у списку та ділить його на два списки. У перший потрапляють значення менше середнього, включаючи середнє значення, 
тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
"""

def split_list(grade):
    less_list = []
    more_list = []
    if grade == []:
        return less_list, more_list
    else:
        avg_grade = sum(grade) / len(grade)
        for score in grade: 
            if score <= avg_grade: 
                less_list.append(score)
            elif score > avg_grade:
                more_list.append(score)
        return less_list, more_list
    



grade = [1,3,5,4,2]
result = split_list(grade)
print(result)    