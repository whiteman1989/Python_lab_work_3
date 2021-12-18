x = 5

def global_powering(n):
    global x
    x = pow(x, n)

print("Початкове значення X: ", x)
print("Зміна глобальної змінної через процедуру --")
global_powering(4)
print("Поточне значенн    X: ", x)