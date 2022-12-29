# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal

def rounding(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
accur = float(input("Введите необходимую точность в формате 0.0001: "))
result = num1/num2

print(rounding(result, accur))