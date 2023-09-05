print()

def largest_number (a,b):
    return max(a,b)
print(largest_number(6,4))
print()

d=135
c=135
if c-d==135 or d-c==135:
    print('YES')
else:
    print('NO')

print()


e=6
if e==12 or 1<=e<=2:
    print('Зима')
elif e in range(3,6):
    print('Весна')
elif e in range(6,9):
    print('Лето')
elif e in range(9,12):
    print('Зима')
else:
    print('Введите верные данные')

print()

r=12
f=32
j=14
if  r>10:
    print('YES')
elif f>10:
    print('YES')
elif j>10:
    print('YES')
else:
    print('NO')

print()


x = [1, 2, 3, 5, -6]
positiv = 0
for num in x:
    if num >= 0:
        positiv += 1

print('Кол-во положительных чисел=', positiv)

print()



def y(z:int,m:int):
    return (z*12*29)+(m*29)
print(y(1,1))







