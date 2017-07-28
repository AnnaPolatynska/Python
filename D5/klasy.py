# -*- coding: utf-8 -*-
import random
# self oznaca odwołanie do biektu print jest w metodzie 
'''
a=1
b= "Witaj"
class PierwszaKlasa:
    def witaj(self):
        print ("Witaj w metodzie")
    def dodaj(self, x, y):
        print("dodawanie")
        self.x=x
        self.y=y
        return self.x + self.y
    def odejmowanie(self):
        print("odejmowanie")
        return self.x - self.y

   
obiekt1= PierwszaKlasa()
obiekt1.witaj()
print(obiekt1.dodaj(4,5))
print(obiekt1.odejmowanie())
obiekt2 = PierwszaKlasa()
obiekt2.witaj()
print(obiekt2.dodaj(2,3))

'''

'''

####
class Pierwszaklasa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dodaj()
    def dodaj(self):
        self.wynik_d= self.x+self.y
        return self.wynik_d
    def odejmowanie(self):
        self.wynik_o= self.x+self.y
        return self.wynik_o
    def __ge__(self,other):


  
      
obiekt1= Pierwszaklasa(4,6)
print(obiekt1)
obiekt2= Pierwszaklasa(1,2)
#rzutowanie z __str__
print(obiekt2)
#rzutowanie z __ad__d
print(obiekt1+ obiekt2)

'''
#P75 BMI zawodnika self by doste self.nazwisko = nazwiskone dla obiektu
'''
class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.obliczBMI()
    def obliczBMI(self):
        self.bmi = round(self.waga / ((self.wzrost/100)**2))
    def __str__(self):
        return "BMI dla "+ self.imie +" "+ self.nazwisko + "wynosi: "+str(self.bmi)
    
z1 = BMI("Michał", "Kruczkowski", 75, 182)
print(z1)
'''
'''
# konstruktor def init domyślny = def __init__(self):
#===============================
class Sklep:
    
    
    
    def __init__(self,towar,cena,ilosc):
        self.towar_klasa = towar
        self.cena_klasa= cena
        self.ilosc_klasa= ilosc
       # self.zaplata_cal=self.zaplata()*1.23
 #zmienna lokalna z self ogólnie jej nie widzi wydruk returna nie zadziała
    def zaplata(self):
        self.do_zaplaty=self.cena_klasa*self.ilosc_klasa
      #  return do_zaplaty
        
#===============================
#wywołanie konstruktora
zakup1 = Sklep("Chleb", 3.99, 4)
print(zakup1.towar_klasa)
print(zakup1.ilosc_klasa)
print(zakup1.cena_klasa)
# nadpisanie danych zakup1.ilosc_klasa=5, zmienia dane
#print(zakup1.ilosc_klasa)

print(zakup1.zaplata())
#print(self.zaplata_cal())
'''
# jest jeszcze destruktor def __del__(self):
#    del self.Tab


# program lotto w oparciu o random
'''

class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))
#sample (sekwencja, ilość powtórzeń = n)        
        
los1= Lotto()
los2= Lotto()
los3= Lotto()
los4= Lotto()
'''
# uporządkowania funkcja sorted 
'''
class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sort()
    def sort(self):
        print(sorted(self.Tab))
        
los1= Lotto()
los2= Lotto()
los3= Lotto()
los4= Lotto()
'''
# uporządkowania funkcja sorted ma wyświetlać bez [] i bez przecinka na końcu
'''
class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sort()
    def sort(self):
        self.Tab_s = sorted (self.Tab)
    def __str__(self):
        self.res = ""
        for i, v in enumerate(self.Tab_s):
            if(i == len(self.Tab_s)-1):
                self.res += str(v)
            else:
                self.res += str(v) +", "
        return "wynik losowania: " + self.res
los1= Lotto()
print(los1)
'''
# P79 dziedziczenie f-cja super umożliwia korzystanie z wielu klas jednocześnie
'''
class Szkolenia():
    def __init__(self, nazwa, termin, cena_n, il_os):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_os = il_os
    def obliczCalk(self):
        self.Suma_b = (self.cena_n* self.il_os)*1.23
        return self.Suma_b

#klasa podrzędna (zawiera nazwę nadrzędnej) dodaj (self, nazwa, termin, cena_n, il_os z Szkoleń)
class Technologie(Szkolenia):
    def __init__(self, nazwa, termin, cena_n, il_os, technologia, poziom):
        super().__init__(nazwa, termin, cena_n, il_os)
        self.technologia = technologia
        self.poziom = poziom

#obiekt1
s1 = Technologie("Kurs dla dzieci", "2000-02-20", 5000, 20, "Python", "podstawowy")
print(s1.obliczCalk())
'''
#z 3 klasami ???
'''
class Szkolenia():
    def __init__(self, nazwa, termin, cena_n, il_os):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_os = il_os
    def obliczCalk(self):
        self.Suma_b = (self.cena_n* self.il_os)*1.23
       

#klasa podrzędna (zawiera nazwę nadrzędnej) dodaj (self, nazwa, termin, cena_n, il_os z Szkoleń)
class Technologie(Szkolenia):
    def __init__(self, nazwa, termin, cena_n, il_os, self, technologia, poziom):
        super().__init__(nazwa, termin, cena_n, il_os)
        self.technologia = technologia
        self.poziom = poziom


class Trenerzy(Technologie):
    def __int__(self, nazwa, termin, cena_n, il_os, self, technologia, poziom, imię, nazwisko, pensja):
        self.imię=imię
        self.nazwisko = nazwisko
        self.pensja = pensja
        def obliczCalkTrener(self):
            return self.obliczCalk(), (self.pensja *1.23)
        
        
        
#obiekt1
s1 = Technologie("Kurs dla dzieci", 2000-02-20, 5000, '20', "Python", "podstawowy")
print(s1.obliczCalk())

s2 = Technologie("Kurs dla dzieci", 2000-02-20, 5000, '20', "Python", "podstawowy", "zygmunt", "Kowalski", 5000)
print(s2.obliczCalkTrener())
'''
# P 80 ok
'''
class Produkt():
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return 'Produkt' + self.nazwa + " " + str(self.cena)

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__( nazwa, cena)
        self.jezyk = jezyk
        self.system = system
        
    def __str__(self):
        return super(). __str__() + self.jezyk + self.system

class Szkolenie(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        
        super().__init__( nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):    
        return super(). __str__() + " " + self.termin
    


szk1 = Szkolenie("Kurs dla dzieci", 5000, "Python", "sys 56", '2017-05-06')
print(szk1)
'''
# P 80 kolory użycie __add__(self, other) ok
'''
class Kolory():
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
    def __str__(self):
        return "kolor to:" + str(self.R)+ " "+str(self.G)+ " "+str(self.B)
    def __add__(self, other):
        return (self.R + other.R)/2, (self.G + other.G)/2, (self.B + other.B)/2
    
kolor1 = Kolory(100,100,100)
print(kolor1)
kolor2 = Kolory(100,150,50)
print(kolor2)
kolor3 = kolor1 + kolor2
print(kolor3)
'''
# 
class Pracownik():
    def __init__(self, imie, nazwisko, etat="staz", pensja=500):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.pensja = pensja
    def przelicz(self):
        self.pensja_b= self.pensja*1.23
        return self.pensja_b, self.pensja
       #nowa pensja po zmianach     
class Kontrakt(Pracownik):
    def zmienKontrakt(self, etat, pensja):
        self.etat = etat
        self.pensja = pensja
    def dodajNadgodziny(self, liczba):
        self.liczba = liczba
        self.pensja = self.pensja + ((self.pensja /(20*8)) * self.liczba)
    def __str__(self):
        return "pensja brutto z nadgodzinami: " + self.imie + self.nazwisko+ " z nadgodzinami" + str(self.pensja*1.23) + "w zł brutto"



p1= Kontrakt ("Piotr", "Wisniewski",)
print(p1.przelicz())
p1.zmienKontrakt("Dev", 5000)
print(p1.przelicz())
p1.dodajNadgodziny(50)
print(p1.przelicz())
print(p1)

#