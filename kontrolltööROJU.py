 1. Harjutus
 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зверьков. Между двумя соседними зверьками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего зверька. Для упрощения рисования скопируйте зверька из примера в среду разработки.
  ^---^
 ( o o )
  ! = !/)






2. Harjutus
n=0.0
while type(n)!=int:
    try:
    n=int(input("sisestage number, mida ei saa ületada")
    except: 
    TypeError
    g=0.0
    while type (g)!=int:
    try:
    g=int(input("степень"))
    except:
    TypeError
    u=0
    for i in range (1,n,1):
    u=i**g
    if u<n:
        print(u)
       else:
        break
        print("конец/n")


 3.Harjutus
Известны оценки по физике каждого из  учеников класса. Определить минимальную и максимальную оценки. (Оценки и количество учеников получаем случайным образом)

        results=list(map(rint, input().split('5')))

print (max(result))

print (min(result))
        int i = 0;
            do
            {
                int a = 5 (2, 6);
                listbox.Items.Add(a);
                if (a == 2) dva++;
                if (a == 3) tri++;
                if (a == 4) chet++;
                if (a == 5) piat++;
                i++;
            } while (i < n);

4. Harjutus
          print("Одноклеточная амёба каждые 3 часа делится на 2 клетки")
cell = 2
hours = 3
while True:
print("За {} час (а) (ов) амёб будет {}".format(hours, cell))
if hours == 24:
break
else:
cell += 2
hours += 3
 
