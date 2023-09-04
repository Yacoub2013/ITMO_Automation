num_float = 3.4

if num_float > 0:
    print('Положительное число')

elif num_float == 0:
    print('Ноль')

else:
    print('Число отрицательное')


print()

permit_print=True

num=2

if num>0 and permit_print:
    print('num- положительное число')

elif not permit_print:
    print('Печать завершена')

print()

a=8
if a>=1 and a<=4:
    print('Бакалавр')
elif a>=5 and a<=6:
    print('Магистр')
elif a>=7 and a<=9:
    print('Аспирант')
else:
    print('Введите верный код обучения')

print()


x=99
if x>100 or x<-100:
    print('-')
else:
    print('+')
