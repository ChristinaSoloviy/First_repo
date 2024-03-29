""" Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. 
Функція повинна просканувати директорію path та повернути кортеж із двох списків. Перший — це список файлів усередині директорії, другий — список директорій.

Приклад виводу функції:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])
"""
def parse_folder(path):
    files = []
    folders = []
    for item in path.iterdir():
        if item.is_dir(): 
            folders.append(item.name)
        elif item.is_file():
            files.append(item.name)
    
        
            
        
            
    return files, folders