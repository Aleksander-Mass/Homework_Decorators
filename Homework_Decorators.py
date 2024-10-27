# Задание:
# Напишите 2 функции:
### 1. Функция, которая складывает 3 числа (sum_three)

### 2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
#      и "Составное" в противном случае.

# Функция, которая проверяет, является ли число простым

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Декоратор, который проверяет результат функции sum_three
def is_prime(func):
    def wrapper(*args, **kwargs): # внутреннюю функцию wrapper в is_prime
        result = func(*args, **kwargs)
        if check_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper  # Функция is_prime должна возвращать wrapper

# Функция, которая складывает три числа
@is_prime
def sum_three(a, b, c):
    return a + b + c

# @is_prime - декоратор для функции sum_three

# Пример использования
result = sum_three(2, 3, 6)
print(result)

# Вывод на консоль:
# Простое
# 11