# def fibonacci(num):
#
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
# x = int(input(" Какое число фибоначи по счету выдать: ")) + 1
# print(fibonacci(x))

# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. >


# def sqrt_(a, b):
#     if b == 1:
#         return a
#     else:
#         return (a * sqrt_(a, b -1))
# n1, n2 = int(input('Какое число возводим в степень: ')), int(input('В какую степень возводим: '))
# print(f'число {n1}, в степени {n2}, будет = {sqrt_(n1, n2)}')


# def summ_(a, b):
#     if a == 0:
#         return b
#     return summ_(a - 1, b + 1)
#
#
# n1, n2 = int(input()), int(input())
# print(summ_(n1, n2))
