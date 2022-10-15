n=int(input('Введите размерность первого массива '))
n2=int(input('Введите размерность второго массива '))
mas=[]
a=[int(i) for i in input('Введите элементы первого массива ').split()]
b=[int(i) for i in input('Введите элементы второго массива ').split()]
for i in a:
    if i in b and i not in mas:
        mas.append(i)
print('Общие элементы массивов',mas)
