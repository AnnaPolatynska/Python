# sumowanie wszystkiego >5 z tablicy ma zwracaæ wartoœæ suma
#ile razy i na której pozycji wystêpuje w ci¹gu inny literowy ci¹g wprowadzany przez u¿ytkownika ???? 
# pêtla krêci siê a¿ do zg³oszenia b³êdu napisy zamienia na liczby Operacje wejœcia =imput, zawsze w niego wedê bo ma  while True:
i=t
def wprowadz():
    Tab = []
    i = "t"
    print("Wprowadz elementy (enter)-koniec wporwadzania")
    while(i != ""):
        i = input(" ")
        if(i != ""):
            while True:
                try:
                    i = float(i)
                    break
                except ValueError:
                    print("B³¹d! Podaj liczbê")
                    i = input(" ")
            Tab.append(i)
        elif(i ==""):
            print("Wprowadzanie zakoñczone")
            print(Tab)
            return Tab
def wypisz5(limit,lista):    
    print("filtruje elementy wiêksze od "+ str(limit))
    suma = 0
    for v in lista:
        if (v >= limit):
            print(v, end=" ")
            suma += v
    print("Suma: ", suma)
wypisz5(int(input("Podaj limit odciêcia: ")),wprowadz())


def wpisz5(lista):
    print("filtruje elementy > 5")
    for v in lista:
        if(v>=5):
            print (v, end = " ")


txt=input ("podaj liczbê: ")
szukaj = input("szukaj : ")
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
print ("podan¹ frazê znaleziono: ",licznik ," razy")



def suma(a,b): 
    while(t>5):
    print (a+b)


