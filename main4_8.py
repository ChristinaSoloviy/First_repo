""" Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.
"""
def is_valid_password(password):
    if len(password) != 8:
        return False
    is_upper = False
    is_lower = False
    is_digit = False
    for el in password:
        if el.isupper() is True:
            is_upper = True
        elif el.islower() is True:
            is_lower = True
        elif el.isdigit() is True:
            is_digit = True
    if is_upper is True and is_lower is True and is_digit is True:
        return True
    else:
        return False


password = "aafgskkk"
result = is_valid_password(password)
print(result)        

