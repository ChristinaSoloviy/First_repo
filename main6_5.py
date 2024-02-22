"""Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
"""
def sanitize_file(source, output):
    with open(source, 'r') as reader:
        dirt_text = reader.read()
        clean_text = ''
        for element in dirt_text:
             if not element.isdigit():
                 clean_text += element
    with open(output, 'w') as writer:
        writer.write(clean_text)