# sumowanie wszystkiego >5 z tablicy ma zwraca� warto�� suma
#ile razy i na kt�rej pozycji wyst�puje w ci�gu inny literowy ci�g wprowadzany przez u�ytkownika ???? 
# p�tla kr�ci si� a� do zg�oszenia b��du napisy zamienia na liczby Operacje wej�cia =imput, zawsze w niego wed� bo ma  while True:
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
                    print("B��d! Podaj liczb�")
                    i = input(" ")
            Tab.append(i)
        elif(i ==""):
            print("Wprowadzanie zako�czone")
            print(Tab)
            return Tab
def wypisz5(limit,lista):    
    print("filtruje elementy wi�ksze od "+ str(limit))
    suma = 0
    for v in lista:
        if (v >= limit):
            print(v, end=" ")
            suma += v
    print("Suma: ", suma)
wypisz5(int(input("Podaj limit odci�cia: ")),wprowadz())


def wpisz5(lista):
    print("filtruje elementy > 5")
    for v in lista:
        if(v>=5):
            print (v, end = " ")


txt=input ("podaj liczb�: ")
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
print ("podan� fraz� znaleziono: ",licznik ," razy")



def suma(a,b): 
    while(t>5):
    print (a+b)


