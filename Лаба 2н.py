from math import *
import sys

# Ввод значений
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))

# Выбор функции f(x)
msg = "Выберите вид функции f(x): arcsin(v/x) -> 1, e^x -> 2, ln(x*y) -> 3"
f = float(input(msg + "\n -> "))
fx = None

from math import *
import sys

# Ввод значений
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))

# Выбор функции f(x)
msg = "Выберите вид функции f(x): sh(x) -> 1, e^x -> 2, x^4 -> 3"
f = float(input(msg + "\n -> "))
fx = None

# Определение значения f(x)
match f:
    case 1:
        fx = sinh(x)
    case 2:
        fx = exp(x)
    case 3:
        fx = pow(x, 4)
    case _:
        print("Неверный выбор")
        sys.exit()

# Вычисление a в зависимости от условий
a = None
if x/y > 0:
    a = pow(fx + log(y), 3)
elif x/y < 0:
    # Проверка, что sin(y) > 0 для корректного вычисления ln
    if sin(y) > 0:
        a = pow(log(sin(y)), 3)
    else:
        a = "значение не может быть вычислено"
else:  # если x/y = 0 или не определено
    # Проверка, что f(x) + y >= 0 для корректного вычисления корня
    if fx + y >= 0:
        a = pow(fx + y, 1/3)
    else:
        a = "значение не может быть вычислено"

print("Результат: ", a)