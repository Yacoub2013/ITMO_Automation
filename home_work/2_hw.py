a:int=2
b:float=2.4665
c:str='срока'
d:list=[1,2,3,4,5]
e:bool=True
print(' a:int=',a,'\n','b:float=',b,'\n','c:str=',c,'\n','d:list=',d,'\n','e:bool=',e)
def task_1(a:int=2, b:float=2.4665, c:str='строка', d:list=[1,2,3,4,5], e:bool=True)->str:
    return a, b, c, d, e
print()
print(task_1())
def task_2(a:list=[1,2,3,8,13,21]):
    return a[0:3]
print()
print(task_2())
# Данная последовательность чисел назывется списком
def task_3(k:int=5):
    return k**2
print()
print(task_3())


