# -*- coding: utf-8 -*-
import random
import math
"""
def powitanie(imie):
    Witaj= "Witaj "+ imie
    return Witaj
a=powitanie("Ania")
b=powitanie("Ala")
c=powitanie("Ola")

print (a,b,c)
"""
#2 pyta o 3 imiona
"""

def powitanie(imie):
    Witaj= "Witaj "+ imie
    return Witaj

L = []

for i in range(1, 4):
    L.append(powitanie(input("podaj imię: ")))
print(L)
"""
'''
def dodawanie(a,b):
    wynik=a + b
    return wynik
res = dodawanie(14, 25)
print(res)
'''
# Anonim wystąpi jak zabraknie imienia
"""
def dodawanie(a,b,imię="Anonim"):
    wynik =a + b
    print(a, b)
    print(imię)
    return wynik

res = dodawanie(a=14,imię="Anna",b=25)
print(res)
"""
'''
#P 69 n!= n!=n(n-1 * ... * 1) np 3!=3*2*1
#-------------
def silnia(n):
    res =1
    i=1
    while(i<=n):
        res *= i
        i+=1
    return res
#------------
print(silnia(4))
'''
'''
#P 69 n!= n!=n(n-1 * ... * 1) np 3!=3*2*1
#-------------
def silnia(n):
    res =1
    L=[]
    i=1
    while(i<=n):
        res *= i
        L.append(res)
        i+=1
    return L
#------------
print(silnia(4))
# 2 sposób wyświetlania danych (bez przecinków i nawiasów)
for i in elementy:
    print(i, end=' ')
elementy=silnia(4)
'''
# 2 definicją

#-------------
"""
def silnia(n):
    res =1
    L=[]
    i=1
    while(i<=n):
        res *= i
        L.append(res)
        i+=1
    return L
#------------
def wyświetl(lista):
    for i in lista:
        print(i, end=' ')
wyświetl(silnia(7))
"""
#P70 Ciąg Fibonacciego 0,1,2,4,7,12 ???
"""
=[0, 1, 1]
def fib(n):
    i=2
    F=[0, 1]
    suma = 0
    a=0
    while(i < n):
        a=(F[i-2],F[i-1])
        F.append(a)
        i= i + 1
    for i in F:
        suma = suma + i
    return F[len(F)-1], suma, F
fib=(fib(2))
print("(Element, suma, kolejne elementy) ", fib)
"""

# losowo 5 słów w ciągu
"""
def Generator_zdan (a=5):
    wyrazy=("noc","dzień","wstaje","zapada","słońce","kwitnie","paproć")
    i=0
    Zdanie=[]
    #Zdanie=random.sample(wyrazy)
    while(i<a):
        Zdanie.append(wyrazy[random.randint(0,len(wyrazy)-1)])
        i+=1
    return Zdanie
# format?????? 
def format(Generator_zdan):
    for i, v in enumerate(Zdanie):
        if(i==0):
            print(v.capitalize(), end=" ")
        elif(i== len(Zdanie)-1):
            print(v, end=" .")
        else:
            print(v, end= " ")
format(Generator_zdan())
print(Generator_zdan())
"""
#długość miedzy odległościami na płaszczyźnie
import math
# trzeba zainportować f-cje matematyczne gdy import math muszę wpisać z jakiej biblioteki
'''
def dist(x1,y1,x2,y2):
    d= math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d,2)
i="a"
x=[]
y=[]
while(i==2):
    u1=input()
    u2=input()
    x.append(u1)
    y.append(u2)
    i=i+1
print (dist(1,1,5,5))
'''
'''
# 2 sposób
def dist(x1,y1,x2,y2):
    d= math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d,2)
i=0
x=[]
y=[]
while(i<2):
    if (i == 0):
        print("podaj położenie końcowe: ")
    else:
        print("podaj położenie początkowe: ")
    u1=int(input())
    u2=int(input())
    x.append(u1)
    y.append(u2)
    i=i+1
print("Dystans", dist(x[0],y[0],x[1],y[1]))
'''
# f-cja która dla dowolnej liczby parametrów zwróci średnią artmetyczną lub 0 dla 0 parametrów
'''
def suma (*arg):
    suma=0
    sr=0
    for v in arg: 
        suma+= v
        sr = suma/len(arg)
        return sr
print(suma(2,3,4))
print(suma())
'''
# rysowanie wykresu przez wstawienie znaczków w kolejnych wierszach inp jakiznak, wartości liczbowe (ilości znaku) ok
'''
def wykres(znak= "*", ilość =10):  
    i=0
    wartości = []
    while (i < ilość):
        wartości.append(int(input(" podaj wartość")))
        i += 1
        for v in wartości:
            print (znak * v)
wykres( "* ", 5)
'''
# rysowanie wykresu przez wstawienie znaczków w kolejnych wierszach inp jaki znak, wartości liczbowe (ilości znaku) 
#lub generuje losowo ilości wykres ???????????????????

import random

'''
def wykres(d, znak = "*", ilosc = 10):
    i = 0
    Wartosci = []
    if (d == "M"):
        while(i < ilosc):
            Wartosci.append(int(input("Podaj kolejną wartość: ")))
            i += 1            
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1     
    for v in Wartosci:
        print(znak * v)
'''
# wybór dobierania auto 
import random
'''
def wykres(d, znak = "*", ilosc = 10):
    i = 0
    Wartosci = []
    if (d == "M"):
        while(i < ilosc):
            var = int(input("Podaj kolenjną wartość: "))
            while (var <0 or var > 9):
                print("Podaj wartość z przedziału (0-9)")
                var = int(input("Podaj kolenjną wartość: "))
            Wartosci.append(var)    
            i += 1            
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1     
    for v in Wartosci:
        print(znak * v)
               
def menu():
    znak_menu = input("podaj znak: ")
    ilosc_menu = input("podaj ilosc: ")       
    decyzja = input("Wybierz opcję: (A)-auto, (M)-manual")
    if (znak_menu == "" and ilosc_menu != ""):
        wykres(d=decyzja, ilosc = int(ilosc_menu))
    elif(znak_menu != "" and ilosc_menu == ""):
        wykres(d=decyzja, znak = znak_menu)
    elif (znak_menu != "" and ilosc_menu != ""):
        wykres(decyzja,znak_menu,int(ilosc_menu))
    else:
        wykres(d=decyzja)

menu()
'''
# #jeżeli oba źle wprowadzi
"""
def wykres(d, znak = "*", ilosc = 10):
    i = 0
    Wartosci = []
    if (d == "M"):
        while(i < ilosc):
            var = int(input("Podaj kolenjną wartość: "))
            while (var <0 or var > 9):
                print("Podaj wartość z przedziału (0-9)")
                var = int(input("Podaj kolenjną wartość: "))
            Wartosci.append(var)    
            i += 1            
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1     
    for v in Wartosci:
        print(znak * v)
               
def menu():
    znak_menu = input("podaj znak: ")
    ilosc_menu = input("podaj ilosc: ")       
    decyzja = input("Wybierz opcję: (A)-auto, (M)-manual")

    while(decyzja !='A'  and decyzja != 'M'):
            decyzja = input("zły znak Wybierz (A)-auto lub (M)-manual")
    if (znak_menu == "" and ilosc_menu != ""):
        wykres(d=decyzja, ilosc = int(ilosc_menu))
    elif(znak_menu != "" and ilosc_menu == ""):
        wykres(d=decyzja, znak = znak_menu)
    elif (znak_menu != "" and ilosc_menu != ""):
        wykres(decyzja,znak_menu,int(ilosc_menu))
    else:
        wykres(d=decyzja)

menu()
"""
# P 74 f-ja generująca wartości dla parametrów
'''
def HTML_export(napis, color= "black", size = "12px", weight= "5px"):
    return'<span style=color: ' + color+ "front size: " + size +" font weight: " +weight+'">' +napis + '</span>'
print (HTML_export("Witaj w HTLM"))
'''
# funkcja wywołująca raz biały raz czarny
'''
def b_w ():
    kolor=("biały","czarny")
    i=0
    powtórzenie=[]
    while(i<1):
        powtórzenie.append(wyrazy[random.randint(0,len(wyrazy)-1)])
        i+=1
return kolor
'''

##### ile razy występują wszystkie
'''
kolor = "black"
licznik = 0
def naprzemian():
    global kolor
    global licznik
    licznik+= 1
    if (kolor=="white"):
        kolor ="black"
    elif (kolor =="black"):
        kolor="white"
    return kolor
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(licznik)
'''
##### ?????? sprawdzić
'''
kolor = "black"
licznik = 0
licznik_b =0
licznik_a =0
def naprzemian():
    global kolor
    global licznik
    global licznik_a
    global licznik_b
    licznik+= 1
    licznik_a+= 1
    licznik_b+= 1 
    kolor= "white"
    if (kolor=="white"):
        kolor ="black"
    elif (kolor =="black"):
        kolor="white"
    return kolor
print(naprzemian())
print(naprzemian())
print(naprzemian())
print (licznik, licznik_a, licznik_b)
'''
# Ćw P 74 co uż•ytkownik chce wywołać: dodawanie 2 liczb, odejmowanie 2 liczb wyjśc z programu DECYZJE UŻYTKOWNIKA OK
'''
def dodawanie(a,b):
    return a+b
def odejmowanie(x,y):
    return x-y
def menu2():
    dec= ""
    while (dec!="Q"):
        dec= input("co robimy? dodawanie(+), odejmowanie(-), wyjście (Q)? ")
        if(dec == "+"):
            print( dodawanie(4,5))
        elif(dec == "-"):
            print( odejmowanie(7,2))
        elif(dec != "+" and dec!= "-" and dec != "Q"):
            print(" zły wybór")
menu2()
'''
        


  
    