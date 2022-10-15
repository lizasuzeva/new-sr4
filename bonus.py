A=[]
n=int(input('Введите размерность массива '))
for i in range (n):
    i=float(input('Введите элементы массива: '))
    A.append(i)
print(A)
delta = int(input('Введите delta '))
result = A.count(min(A) + delta)
print('Результат ', result)
