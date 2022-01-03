from random import *
s=null=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """Kui a>b, siis vahetame neid
    :param:int a: Arv, mis on suurem kui b
    :param:int b: Arv, mis on väiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Genereerib numbreid a-st b-ni väärtuses n
    :param:int n:negatiivsed numbrid
    :param:list loend:kõigi numbrite loend
    :param:int a:Arv, mis on suurem kui b
    :param:int b:Arv, mis on väiksem kui a
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:int,null:list):
    """
    :param:list loend:kõigi numbrite loend
    :param:list p:positiivsed numbrid
    :param:int n:negatiivsed numbrid
    :param:int a:Arv, mis on suurem kui b
    :param:list null:nullid
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            null.append(el)

def keskmine(loend:list):
    """Arvutame keskmine arv
    :param:list loend:kõigi numbrite loend
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Numbrite lisamine loendisse
    :param:list loend:kõigi numbrite loend
    :param:float el:
    """
    loend.append(el)
    loend.sort()

arvud_loendis()
