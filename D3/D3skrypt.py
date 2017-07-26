# -*- coding: utf-8 -*-
import random
# dzień 2
#słownik nawiasy{}
'''
literki = {'a' : 'A', 'b' : 'B','c' : 'C','d' : 'D'}
print(literki)
print(len(literki))
print (literki["a"], literki["b"])
literki['c'] = "napis"
print(literki['c'])
'''
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
'''
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

'''
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
"""
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
"""

# NIC NIE WYCHODZI :-(
'''
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
for var in lista:
    print("wartość: "str(var))
    lista.append(15)
for index, var in enumerate(lista):
    print("Index: "+ str(index)+" \twartość" +str(var))
'''
#  
'''
s1= range(100)
print(s1)
for i in s1:
    print(i)
for j in range(15,25):
    print(j)
for k in range (0,50,2):
    print(k)
    
# kwadraty liczb parzystych
for k in range (0,50,2):
    print(k, k**2)
# odległośći w ciągach
for k in range (0,50,2):
    print("wynik uporządkowany: %4i%6i%8i" % (k, k**2, k**3))
# odległości w ułamkach

for l in range(0,10):   
    print("Pierwiastkiem liczby %2i jest %5.3f" % (1,1**0.7)) 

# P57 zamówienie i produkty -NICZEGO NIE MA
'''
"""
zamówienie = input("wybierz towar")
zamówienie_ilość = int(input("Podaj ilość zamawianego produktu"))
sklep_produkty= {"monitor 16": 1, "klawiatura":2, "mysz":3}
produkty_cena={1:1500, 2:400, 3:200}
produkty_dostępność = {1:5, 2:5, 3:15}
for k in sklep_produkty:
    if(zamówienie == k and produkty_dostępność[sklep_produkty[k]]>= zamówienie_ilość):
        print("produkt dostępny: "+ k)
        print("zamawiasz: " + str(zamówienie_ilość) + "szt")
    elif(zamówienie == k and produkty_dostępność[sklep_produkty[k]]< zamówienie_ilość):
        print("produkt dostępny: "+ k)
        print("jest dostępne tylko: " + str(produkty_dostępność[sklep_produkty[k]]) + "szt")
    else:
        print("produkt niedostępny")
#
"""
    
#P57
'''
zamówienie = input("wybierz towar")
zamówienie_ilość = int(input("Podaj ilość zamawianego produktu"))
sklep_produkty= {"monitor": 1, "klawiatura":2, "mysz":3}
produkty_cena={1:1500, 2:400, 3:200}
produkty_dostępność = {1:5, 2:5, 3:15}
for k in sklep_produkty:
    if(zamówienie == k and produkty_dostępność[sklep_produkty[k]]>= zamówienie_ilość):
        print("produkt dostępny: "+ k)
        print("zamawiasz: " + str(zamówienie_ilość) + "szt")
    elif(zamówienie == k and produkty_dostępność[sklep_produkty[k]]< zamówienie_ilość):
            print("produkt dostępny: "+ k)
            print("jest dostępne tylko: " + str(produkty_dostępność[sklep_produkty[k]]) + "szt")    
'''
#P58 kilka zamówień??????????????????????????????????????
"""zamówienie = input("wybierz towar")
zamówienie_ilość = int(input("Podaj ilość zamawianego produktu"))
sklep_produkty= {"monitor": 1, "klawiatura":2, "mysz":3}
produkty_cena={1:1500, 2:400, 3:200}
produkty_dostępność = {1:5, 2:5, 3:15}

while produkty_dostępność[sklep_produkty[k]]>= zamówienie_ilość:
    for k in sklep_produkty:
        if(zamówienie == k and produkty_dostępność[sklep_produkty[k]]>= zamówienie_ilość):
            print("produkt dostępny: "+ k)
            print("zamawiasz: " + str(zamówienie_ilość) + "szt")
else:
    print("produkt niedostępny: "+ k)
    brake
"""         
# konwertujemy cyfry na słowa
"""
slownie = {'1': "jeden", '2': "dwa", '3':"trzy", "4":"cztery", "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewieć"}
i="t"
res=[]
while (i == "t"):
    dig = input("wprowadz liczbę (1-9): ")
    if(dig.isdigit()):
        res.append(slownie[dig])
    else:
        print("podana wartość nie jest cyfrą")
    i = input("czy chcesz wprowadzać dalej? (t/n) ")
print (i,end='')
print (res)
"""
"""
# tabliczka mnożenia 5 na 5
line = range(1,6)
n = 1

while(n<=5):
    print(str(n)+ "|", end="")
    print("%3i%3i%3i%3i%3i" % (n*line[0], n*line[1], n*line[2], n*line[3], n*line[4]))
    n+=1
# wyświetl kwadraty liczb nieparzystych od 9 do 1
line= range (1,10,2)

np = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
i=len(np) -1
while(i==0 len(np)-1):
    print(str(i)+", "+str(lista[i]))
    i-=1
"""
'''
# X do potęgi y 
x= int(input("podaj liczbę x: "))
y= int(input("podaj liczbę y: "))
i=1
res=1
while(i <= y):
    res*=x
    i = i+1
print(res)

# suma ciągu geometrycznego i wartość elementu itego (S to wynik) a*q^n

n =int(input("podaj n: "))
a1 =float(input("podaj a1: "))
q=float(input("podaj q :"))
l=[]            
i=0
S=0
while(i<n):
    S+=a1*(q**i)
    l.append(a1*(q**i))
    i+=1
#2f miejsca po przecinku (-) to wyjustowanie do lewej s=string i= int f=float
#end="" znak zakoczenia procedury

#  %15.2f to 12miejsc , 2 po 

print ("%10s %15.2f" % ("Suma: ",S))
print ("%10s %10s" % ("składowe: ",""), end="" )
#print (a1 *(q**(n-1)))
for v in l:
    print ("%5.2f" % (v), end=" ")
# przez listę zwraca indeksy i oraz wartości v



#ile razy i na której pozycji występuje w ciągu litera ciąg wprowadzany przez użytkownika
txt=input ("podaj napis: ")
szukaj = input("szukaj znaku: ")
i=0
licznik=0
while (i<=len(txt)-1):
    if (txt [i]== szukaj):
        print ("znaleziono", szukaj, "na pozycji", i+1)
        licznik+=1
    i +=1
print ("podaną frazę znaleziono: ",licznik ," razy")

#ile razy i na której pozycji występuje w ciągu inny literowy ciąg wprowadzany przez użytkownika
txt=input ("podaj napis: ")
szukaj = input("szukaj znaki: ")
ilosc= len(txt) - len(szukaj) +1
licznik=0
i=0
while (i < len(txt)):
    tab = txt [i:i+len (szukaj)]
    print(tab)
    if (tab == szukaj):
        print ("znaleziono", szukaj, "na pozycji", i+1)
        licznik+=1
    i +=1
print ("podaną frazę znaleziono: ",licznik ," razy")

#
#ile razy i na której pozycji występuje w ciągu inny literowy ciąg wprowadzany przez użytkownika w trzech znakach ma 2 znaki znajdować raz (nie ma zliczać 2 razy)
txt=input ("podaj napis: ")
szukaj = input("szukaj znaki: ")
ilosc= len(txt) - len(szukaj) +1
licznik=0
i=0
while (i < len(txt)):
    tab = txt [i:i+len (szukaj)]
    print(tab)
    if (tab == szukaj):
        print ("znaleziono", szukaj, "na pozycji", i+1)
        licznik+=1
        i=i +len(szukaj)
    else:
        i +=1
print ("podaną frazę znaleziono: ",licznik ," razy")

#Przelicz F na celciusze F=(C+1.8)+32 co 5 stopni
#Far=(C+1.8)+32
C=range(-20, 40, 5)
i= len(C)-1
print("%5s  |  %5s" % ("C", "F"))
while(i >= 0):
    print("%5i  |  %5.1f" % (C[i], (C[i]*1.8)+32))
    i = i- 1
'''
'''
#Przelicz F na celciusze F=(C+1.8)+32 oraz + przy dodatnich a nie przy zerze, użytkownik sam wpisuje wartości
start = int(input("start: "))
stop = int(input("stop: "))
step = int(input("step: "))

if((stop-start) % step==0):
   C=range(start, stop+step, + step)
else:
   C=range(start, stop, +step)
i= len(C)-1
print("--------------")
print("%5s  |  %5s" % ("C", "F"))
print("--------------")
while(i >= 0):
   if(C[i] == 0):
      print("%5i  |  %5.1f" % (C[i], (C[i]*1.8)+32))
   else: 
      print("%+5i  |  %+5.1f" % (C[i], (C[i]*1.8)+32))
   i = i- 1
   '''
'''
# lista ocen 
Dop=["3","3,5","4","5"]
i="x"
O=[2,5,4,3]
print ("wprowadz oceny: ")
while(i in Dop):
    i=int(input(" "))
    if(ocena in Dop):
        O.append(i)
    elif(i == ""):
        print("wprowadzanie ocen zakończone")
    else:
        print("ocena niepoprawna")
print(0)
'''
# lista ocen + średnie
Dop=["3","3,5","4","5"]
i="x"
Oc=[]
print ("wprowadz oceny: ")
while(i != ""):
    i=(input(" "))
    if(i in Dop):
        Oc.append(float(i))
    elif(i == ""):
        print("wprowadzanie ocen zakończone")
    else:
        print("ocena niepoprawna")
sr=0
for i in Oc:
    sr += i
print("Średnia ocen: ", round(sr/len(Oc),2))