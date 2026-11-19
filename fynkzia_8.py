# Задание 8 (Напишите функцию display_info, которая принимает любое количество именованных аргументов и для каждой пары выводит строку «<ключ>: <значение>».)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Анна", age=20, city="Москва")
