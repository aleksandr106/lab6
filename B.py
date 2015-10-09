'''
Задача B
++++++++

Одна фирма обслуживает автоматы по продаже чая и кофе.

Стоимость стакана чая и кофе в автомате равна пяти рублям. Автомат принимает монеты по 5 и 10 рублей, а также купюры в
10, 50 и 100 рублей. Когда покупателю надо выдавать сдачу (т.е. когда пассажир бросил в автомат десятирублёвую монету
или 10-, 50- или 100-рублёвую купюру), автомат выдаёт сдачу пятирублёвыми монетами; если же покупатель бросил в автомат
пятирублёвую монету, то автомат её сохраняет и может использовать для сдачи следующим покупателям.

Ясно, что, чтобы обеспечить возможность выдачи сдачи всем покупателям, может потребоваться изначально загрузить в
автомат некоторое количество пятирублёвых монет. Сейчас автоматы проходят испытания с целью определить минимальное
количество монет, которые надо загрузить в автомат перед началом дня. Вам дан протокол одного из таких испытаний:
известен порядок, в котором покупатели оплачивали свои покупки различными монетами и купюрами. Определите, какое
минимальное количество пятирублёвых монет должно было изначально находиться в автомате, чтобы всем покупателям хватило
сдачи.

В первой строке входных данных находится одно натуральное число N — количество покупок в автомате, которые были
совершены в ходе испытания (1≤N≤50000). Во второй строке находятся N натуральных чисел, каждое из которых равно номиналу
монеты или купюры, которую использовал очередной покупатель для оплаты; каждый номинал может принимать одно из четырёх
значений: 5, 10, 50 или 100.

Выведите одно число — минимальное количество пятирублёвых монет, которые надо было загрузить в автомат изначально, чтобы
всем покупателям хватило сдачи.

+----------+-------+
| Ввод     | Вывод |
+==========+=======+
| 3        | 19    |
+----------+-------+
| 10 5 100 |       |
+----------+-------+
+----------+-------+
| 3        | 0     |
+----------+-------+
| 5 5 10   |       |
+----------+-------+
+----------+-------+
| 4        | 9     |
+----------+-------+
| 50 5 5 5 |       |
+----------+-------+
'''
input=open('input.txt','r')
output=open('output.txt','w')
b=''
b=input.readline()
b=b.rstrip()
b=int(b)
a=['']*b
c=0
s=input.readline()
s=s.rstrip()
j=0
for i in range(len(s)):
    if s[i]!=' ':
        a[j]+=s[i]
    else:
        a[j]=int(a[j])
        j+=1
a[b-1]=int(a[b-1])
for i in range(b):
    if a[i]==5:
        c-=1
    else:
        c+=((a[i])-5)//5
if max(a)==a[0]:
    c=(int(a[0])-5)//5
if c>0:
    print(c, file=output)
else:
    print('0',file=output)
input.close()
output.close()
