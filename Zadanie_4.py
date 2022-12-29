# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choice


def polynomial(num: int):
    
    poly = ""
    num_list = range(0, 100)

    with open("poly.txt", "a") as my_file:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "

        my_file.write(f"{poly}{choice(num_list)} = 0\n")


for _ in range(3):
    polynomial(int(input("Укажите степень многочлена: ")))