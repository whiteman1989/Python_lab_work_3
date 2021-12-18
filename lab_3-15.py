from random import randint

first_list = [randint(1,100) for i in range(15)]

def count_defs(array):
    array = list(array)
    max_element = max(array)
    result = sum(1 for i in array if i/max_element < 0.9)
    return reSsult

print("Масив: ", first_list)
print("Кількість елементів масиву з відмінністю більше ніж 10%: ", count_defs(first_list))