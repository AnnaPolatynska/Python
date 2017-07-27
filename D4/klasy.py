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
# program lotto w oparciu o random
class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))
#sample (sekwencja, ilość powtórzeń = n)        
        
los1= Lotto()
los2= Lotto()
los3= Lotto()
los4= Lotto()

#destruktor def __del__(self):
#    del self.Tab
