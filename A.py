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
b=int(b.readline())
a=[]
c=0
for line in output:
    a.append(line)
for i in range(b):
    a[i]=int(a[i])
for i in range(b):
    j=i+1
    while j<b:
        if a[i]==a[j]:
            c=a[i]
print(c,file=output)
input.close()
output.close()
