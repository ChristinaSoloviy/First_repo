"""Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""
def real_len(text):
    result = "" 
    for el in text:
        if el in ["\n", "\f", "\r", "\t", "\v"]:
            continue
        else:
            result += el
    return len(result)
text_1 = 'Alex\nKdfe23\t\f\v.\r'
text_2 = 'Al\nKdfe23\t\v.\r'
answer_1 = real_len(text_1)
answer_2 = real_len(text_2)
print(answer_1, answer_2)

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'