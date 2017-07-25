# -*- coding: utf-8 -*-
import random
# dzień 2
#słownik nawiasy{}
literki = {'a' : 'A', 'b' : 'B','c' : 'C','d' : 'D'}
print(literki)
print(len(literki))
print (literki["a"], literki["b"])
literki['c'] = "napis"
print(literki['c'])
"""
#dopisz d usuń c
literki["d"]="D"
del literki['c']
print(literki)

literki[2]= "abc"
print(literki)
# słownik
to_str=str(literki)
print(to_str[0], to_str [1])
# P44 słownie na wartość od 1 do 5
key1 = input ('Podaj liczbę (1-5) zapisaną słownie ')
to_dec= {'jeden':1, 'dwa':2,'trzy':3,'cztery':4,'pięć':5, 'piec':5}
print(key1.capitalize() +" w postaci liczby dziesiętnej to "+ str(to_dec[key1]))

#P47 zamiana rzymskiej na dziesiętną z wykorzystaniem kalkulatora powyżej wartośc 2 słownika jest kluczem do 1
to_rom= {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
print(key1.capitalize() +" w postaci liczby dziesiętnej to "+ str(to_dec[key1])+ ", a w postaci rzymskiej: "+ to_rom[to_dec[key1]])
"""
'''
#P48 ilość cena brutto, netto 
nazwa = input("Czego potrzebujesz? (chleb, bułka, ciasto): ")
ilość= int(input("Podaj ilość (szt) wybranego produktu: "))
             
nazwa_t = {"chleb" : 1, "bułka" : 2, "ciasto" : 3}
CenaNetto = {1 : 2.50, 2 : 0.90, 3 : 6.20}

print('Do zapłaty: '+ str(round(CenaNetto[nazwa_t[nazwa]]*ilość,2))+ "zł (" + str(round(CenaNetto[nazwa_t[nazwa]]*ilość*1.23,2))+"zł brutto.)")


#zbiory set
kształty = set (["koło", "kwadrat", "gwiazda"])
print(kształty)
kształty.add('elipsa')
kształty.discard('gwiazda')
print(kształty)

# zbiór podrzędny i nadrzędny
kształty2 =set(["koło"])
print(len(kształty2), len(kształty))
print(kształty.issubset(kształty2))
print(kształty.issuperset(kształty2))

# suma różnica (- lub ^)część wspólna (&)zbiorów połączenie(|),
kształty2.add('elipsa')
print(kształty | kształty2)
print(kształty & kształty2)
print(kształty ^ kształty2)
'''
# P 49 zwraca 6 losowych liczb od 1 do 49 + import random (ciągi losowe)
los1 = random.randint(1,49)
los2 = random.randint(1,49)
los3 = random.randint(1,49)
los4 = random.randint(1,49)
los5 = random.randint(1,49)
los6 = random.randint(1,49)
print(los1)
print(los1, los2, los3, los4, los5, los6)

#2 sposób
s=set()
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
L=list(s)
print(L[:6])
"""
# instrukcja warunkowa if
a=int(input('podaj liczbę: '))
if(a%2==0):
    print("liczba "+ str(a)+ ' jest parzysta')
else:
    print("liczba "+ str(a)+ ' jest nieparzysta')
    print("nieparzysta")
    
print('jestem za instrukcją if')
"""
# instrukcja warunkowa if
"""
a=int(input('podaj liczbę: '))
if(a%2==0):
    print("liczba "+ str(a)+ ' jest parzysta')
    if(a>10):
        print("liczba "+ str(a)+ ' jest parzysta i większa od 10')
    else:
            print("liczba "+ str(a)+ ' jest parzysta i mniejsza od 10')
else:
    print("liczba "+ str(a)+ ' jest nieparzysta')
    print("nieparzysta")
    
print('jestem za instrukcją if')
"""
"""
# instrukcja warunkowa if/ elif /else

a=int(input('podaj liczbę: '))
if(a%2==0 and a >=10 ):
    print("liczba "+ str(a)+ ' jest parzysta i większa/równa 10')
elif(a%2==0 and a <10 ):
            print("liczba "+ str(a)+ ' jest parzysta i mniejsza od 10')
else:
    print("liczba "+ str(a)+ ' jest nieparzysta')
    print("nieparzysta")
    
print('jestem za instrukcją if') 
"""
'''
# 54 czy liczby mieszczą sie w przedziale od 0 do 9
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index= int(input("podaj element który chcesz zweryfikować: "))

if (index >=0 and index <=(len(lista)-1)):
    print ("liczba znajduje się w wybranym przedziale")
    print (lista[index])
else:
    print("liczba poza ciągiem")
 ''' 
# P 55 czy 2 pierwsze elementy są dodatnie
'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index= int(input("podaj element który chcesz zweryfikować: "))
if (lista[0]>0 and lista[1]>0):
    print ("oba te elementy są większe od 0")
elif (lista[0]<=0 and lista[1]>0):
    print ("pierwsza mniejsza/ równa zeru druga większa ")
elif (lista[0]<=0 and lista[1]<0):
    print ("oba te elementy są mniejsze od 0")    
else:
    print ("pierwsza większa/ równa zeru druga mniejsza ")
'''
# czy zbiór A jest podzbiorem B
'''
A= set([1,2,3,4,5])
B=set ([2,3,4])

print(A<=B)
#lub
if A>=B:
    print("B jest podzbiorem A")
else:
    print("A jest podzbiorem B")
'''
#pętla
"""
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
while(i<= len(lista)-1):
    print("index: "+str(i)+"\wartość: "+str(lista[i]))
    i+=1
print ("poza linią")
"""
#pętla po nieparzystych
"""lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
while(i<= len(lista)-1):
    print("index: "+str(i)+"\wartość: "+str(lista[i]))
    i+=2
        
print ("poza linią")"""

#pętla po parzystych
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
while(i<= len(lista)-1):
    if(lista[i]%2 ==0):
        print("index: "+str(i)+"\wartość: "+str(lista[i]))
    i+=1
        
print ("poza linią")
#pętla 
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
while(i<= len(lista)-1):
    if(lista[i]%2 ==0):
        print("index: "+str(i)+"\wartość: "+str(lista[i]))
    i+=1
else:
    print ("jestem w elsie")
print ("poza linią")
# która z liczb jest większa 3 argumenty podaj o ile
a=14
b=12
print("a jest większe niż b o:"+ str(a-b)) if (a>=b) else print("b jest większe niż a od b o:"+str(b-a))
