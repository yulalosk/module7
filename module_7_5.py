import os, time

directory='D:\\pythonforuniversity\\pythonProject\\module7'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
# print(os.getcwd())

# directory='D:\\pythonforuniversity\\pythonProject\\module7'
# for file in os.listdir(directory):
#     filepath = os.path.join(directory, file)
#     if os.path.isfile(filepath):  # Проверка, что это файл, а не папка
#         filesize = os.path.getsize(filepath)
#         filetime = os.path.getmtime(filepath)
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#         print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}')