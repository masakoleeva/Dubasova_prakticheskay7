# Задание 7 (Напишите функцию multiply, которая принимает любое количество чисел и возвращает их произведение. Если числа не переданы, функция возвращает 1)
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))
print(multiply())
