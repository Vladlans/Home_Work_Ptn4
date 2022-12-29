# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

from random import randrange


def create_rand_list(count):
    numbers = list()
    for i in range(count):
        numbers.append(randrange(count))
    return numbers


def uniq_nums(list_nums: list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)

    return result


all_list = create_rand_list(int(input("Укажите количество чисел: ")))
print(all_list)
print(uniq_nums(all_list))