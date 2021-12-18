def swap_array_elements(array):
    array = list(array)
    a = array[0]
    array[0] = array[len(array)-1]
    array[len(array)-1] = a
    return array

m = int(input("Введіть довжину масиву: "))
array = [input("введіть елемент масиву №"+str(i)+": ") for i in range(m)]
print("Маисв    до: ", array)
print("Масив аісля: ", swap_array_elements(array))
