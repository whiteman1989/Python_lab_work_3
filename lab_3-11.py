def sum_of_number(number):
    string = str(number)
    return sum(int(i) for i in string)

n = input("Веедіть число: ")
print("Сума цифер числа : ", sum_of_number(n))