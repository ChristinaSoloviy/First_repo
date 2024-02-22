"""Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, 
додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
"""
def to_indexed(source_file, output_file):
    result = []
    with open(source_file, 'r') as reader:
        lines = reader.readlines()
        for indx, line in enumerate(lines):
            row = f'{indx}: {line}'
            result.append(row)
    with open(output_file, 'w') as writer:
        writer.writelines(result)
