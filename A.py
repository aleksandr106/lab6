'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
input=open('input.txt','r')
output=open('output.txt','w')
b=''
b=input.readline()
b=b.rstrip()
b=int(b)
s=input.readline()
a=s.split()
c=0
for i in range(b):
   for i in range(j+1,b)
        if a[i]==a[j]:
            c=int(a[i])
            break
    if c>0:
       break   
print(c, file=output)
input.close()
output.close()




