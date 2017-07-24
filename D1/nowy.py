# -*- coding: utf-8 -*-

# komentarz jednowierszowy
zmienna1 = 5        
zmienna2 = 5.3  
'''
komentarz
text = "to jest tekst"  
literki = "a"
'''
tekst2 = 'inny tekst'
witaj = "I'm Anna"
Zmienna3 = 'liczba'
zmienna3 = 2+5
print(zmienna1)
print(zmienna3, zmienna2, Zmienna3)
print(witaj)
nowa_zmienna = zmienna3 + 5
print(nowa_zmienna)
print("HI "+ witaj)
tekst3 = 'uwielbiam_kawę'
print("Hi "+ witaj +" "+ tekst3)

print('przed_zmiana', zmienna1)
zmienna1= 3.14
print('po_zmianie', zmienna1)
del zmienna1
#print (zmienna1)

#P1
zmienna_1 = 1
zmienna_2 = 2.4
zmienna_3 = 'w1.'
print(zmienna_1, zmienna_2, zmienna_3)

#P2
zmienna_1 = (2.1)
zmienna_2 = ('abc')
zmienna_3 = (0)
print("po zmianie", zmienna_1, zmienna_2, zmienna_3)

#P5
Imię = "Anna"
Nazwisko = "Połatyńska"
Rok_urodzenia = '1849'
Stanowisko = "specjalista_ds_cudów"
Płaca = "bimbalion zł"
print(Imię, Nazwisko, Rok_urodzenia, Stanowisko, Płaca)

#P4
"""
pi= 3.14
promień= int(input("podaj_liczbę"))
pole_kola= pi*promień*promień
print(pole_kola)

#P5a
Imię = input("podaj_imię")
Nazwisko = input("podaj_nazwisko")
Rok_urodzenia = input("podaj_rok_ur.")
Stanowisko = input("podaj_stanowisko")
Płaca = int(input("podaj_pensję"))
print(Imię, Nazwisko, Rok_urodzenia, Stanowisko, Płaca)
"""
#type() zwraca typ wartości zmiennej
print(type(21j))
# liczby długie - nie dziąła
dluga = 366225548977552222
print(type(dluga))
"""dluga2= 32L
print(type(dluga2))"""
#dzielenie zwykłe a dzielenie z zaokrągleniem
dzielenie = 3/2
dzielenie2= 3//2
print (dzielenie)
print (dzielenie2)
# zaokrąglanie round(liczba, precyzja)
print(round(1.3), int(1.5), int(1.6))
print(round(-1.3), round(-1.8))
print(int(1.3), int(1.5), int(1.9))
# P10 wylicz VAT
"""
kwota= int(input("kwota_netto"))
vat=int(input ("podaj_stawkę_vat_(3%, 5%,8%, 23%): "))
kwota_brutto= kwota_netto + (kwota_netto*(vat/100))
Print("kwota_netto" + (str(vat+ "vat_wynosi": str("kwota_brutto"))+' zł')
"""
# metka cenowa
"""
nazwa_p1="chleb"
nazwa_p2= "mleko"
nazwa_p3= "cukierki"
cena_P_1 = 1.99
cena_P_2 = 4.15
cena_P_3 = 15.99
zamówienie_p1= int(input("Liczba_chlebow: "))
zamówienie_p2= float(input("Litry_mleka: "))
zamówienie_p3= float(input("Waga_cukierków (g): "))
suma= (cena_P_1* zamówienie_p1) + (cena_P_2* zamówienie_p2) + ((cena_P_3/1000)* zamówienie_p3)
print("twoje_zamówienie")
print("================")
print("Liczba_chlebów", zamówienie_p1, " szt.")
print("Litry_mleka", zamówienie_p2, " l")
print("Waga_cukierków", zamówienie_p3, " gr")
print("================")
print(round(suma,2)," zł")
"""
# znajdz błąd(-1j) a nie (-1)j po liczbie nie może być znak
a = 12
b = 1+(-1j)
print(a*b)

#logiczne klasa bool
log1 = True
print(type(log1))

a= """
autor:
wersja:
znak:
"""
"""
print (a)
#backslashend \ znak przejścia do nowej linii
b= "autor:\wersja:\znak:"
print (b)

txt = "napis "
print (txt*3)

# podaj ile razy powórz imię po przecinku a ostatnie z kropką
Imię = input("podaj_imię")
Imię1 = Imię + ", "
Imię2 = Imię + "."
n = int(input("ilość_powt: "))
print (Imię1 * (n-1)+ Imię2)

#P22
Imię = input("podaj_imię")
Nazwisko = input("podaj_nazwisko")
Wiek = input("podaj wiek")
Stanowisko = input("podaj_stanowisko")
Płaca = int(input("podaj_pensję"))
n= int(input("ilość_powt: "))
print(("Pan"+ Imię+ Nazwisko + "(Wiek: " + Wiek +")" + "pracuje na stanowisku: " +Stanowisko + " (pensja: "+ str(Płaca)+ " )\n")*n)
"""
# liczba na napis bool(), float(), int(), str()
a=1
napis = str(a)
print (type(napis))
print (type(a))

# stawka godzinowa pracownika 

kwota_netto_h = 550/168
print ("kwota netto / h", round(kwota_netto_h,2), "zł")
print ("kwota brutto / h", round(kwota_netto_h*1.23,2), "zł")
"""
# prawo Morgana
p= True
q= False
dM1 = not (p and q)
dM2 = (not p) or (not q)
print(dM1, dM2)
print(dM1 == dM2)
"""
#
"""
a=False
b=False
c=True

P1= (not a) and (not b) and (not c)
P2= (not a) and (not b) and c
P3= (not a) and  b and (not c)
P4= a and (not b) and (not c)
print(P1,P2,P3,P4)
res= P1 or P2 or P3 or P4
print(res)
"""
# które imie cięższe
"""
print('ala' > "alan")
# pierwiastek 2 stopnia z 17
liczba= round(17**(1/2),2)
urojona= 1j
reszta =str (liczba * urojona)
print(liczba* urojona)
print("liczba zespolona: 0 + "+ reszta )
"""
# reszts z dzielenia
Z = 17 %  7
print(Z**2 + 3*Z)

# 20 krotnie 
print((str(1.2e+3+34.5)+"-")*20)
#P38 stan konta za n lat na danym %
"""
SPK = int(input("podaj SPK "))
P = float(input("Podaj oprocentowanie "))
N = int (input("Podaj Liczbę lat "))

res = round(SPK*(1+(P/100))**N,2)
print("Kwota po "+str(N)+ " latach wynosi: " +str(res) +" zł")
"""
#
