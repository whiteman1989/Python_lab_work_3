import math

def calc_p(tringle):
    tringle = dict(tringle)
    p = (sum(tringle.values()))/2
    return p

def get_area(tringle):
    tringle = dict(tringle)
    p = calc_p(tringle)
    return math.sqrt(p*(p - tringle['a'])*(p - tringle['b'])*(p - tringle['c']))

tringles = []

for i in range(3):
    tringle = {}
    tringle['a'] = float(input("Введіть сторону a трикутника №"+str(i+1)+": "))
    tringle['b']= float(input("Введіть сторону b трикутника №"+str(i+1)+": "))
    tringle['c']= float(input("Введіть сторону c трикутника №"+str(i+1)+": "))
    tringles.append(tringle)

areas = [get_area(i) for i in tringles]
print("Площі трикутників: ", areas)
if(len(set(areas))==1):
    print("Всі трикутники рівновеликі!")
elif(len(set(areas))==2):
    print("2 з 3 трикутників рівновеликі!")
else:
    print("Всі трикутники різні!")
