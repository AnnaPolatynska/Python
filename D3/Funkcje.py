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


