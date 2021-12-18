from random import randint
import statistics

first_list = [randint(1,100) for i in range(randint(1,15))]
second_list = [randint(1,100) for i in range(randint(1,15))]
third_list = [randint(1,100) for i in range(randint(1,15))]

print("Масив А: ", first_list)
print("Середнє ар. масиву А: ", statistics.mean(first_list))
print("Сума чисел масиву А:  ", sum(first_list),"\n")

print("Масив B: ", second_list)
print("Середнє ар. масиву B: ", statistics.mean(second_list))
print("Сума чисел масиву B:  ", sum(second_list),"\n")

print("Масив C: ", third_list)
print("Середнє ар. масиву C: ", statistics.mean(third_list))
print("Сума чисел масиву C:  ", sum(third_list),"\n")