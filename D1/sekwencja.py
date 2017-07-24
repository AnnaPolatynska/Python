# -*- coding: utf-8 -*-
#formatowanie tekstu
napis = "to jest długi napis"
print(napis.capitalize())
print(napis.count("i"))
print(napis.index("i"))
print(napis.replace("jest","był"))
#listy
"""Tab =[]
Tab.append = [1]
Tab.append = ["abc"]
Tab.append = ["A"]
print(Tab[0],Tab[1],Tab[2])
print(Tab[3])
"""
#deklaracje i przypisanie wartości
"""
oceny = []
a=input("Podaj_ocenę")
oceny.append(a)
oceny.append(input("podaj_2 ocenę"))
print(oceny[0], oceny[1])
"""
#tablica 2 sposób
oceny2= [4, 2, 5, 5, 4, 6, 1, 3, 2, 5]
print(oceny2)
#piąta ocena
print(oceny2[5])
#od 3 elementu do koń♠ca
print(oceny2[3::])
# Listalist
listlist=[[1,2,3], ["dzienny"], ["nocny"]]
print(listlist[1][0])
"""
#napis na listę zamiana liter
text = "jakiśnapistujest"
lista= list(text)
print(lista)
lista[2]= "w"
print(lista)
"""
# 5 elementów wypisz 1 i ostatni
artyk=[["orzechy", "rodzynki", "brzoskwinie"], [2.75, 3.20, 8.30]]
print(artyk)
print("nazwa\t\tcena")

print(artyk[0][0]+ " \ " + str(artyk[1][0]))
print(artyk[0][1]+ " \ " + str(artyk[1][1]))
print(artyk[0][2]+ " \ " + str(artyk[1][2]))
# krotki- typy sekwencyjne = zabezpiecza dane
krotka=("a", 2, 13.5)
krotka2= "a", "b", "c"
print(krotka)
print(krotka2)
# 43 zrób krotkę
data= ("dzień", "miesiąc", "rok")
data=[("28", "15", "17"), (2, 3, 8),(2017 , 2018, 2019)]
print("data ważności artykułu ")
print(data[0][0]+ "\t\t" + str(data[1][0])+ "\t\t "+ str(data[2][0]))
print(data[0][1]+ "\t\t " + str(data[1][1])+ "\t\t" +str(data[2][1]))
print(data[0][2]+ "\t\t" + str(data[1][2])+ "\t\t " +str(data[2][2]))

tabelka=[("Kowal", ("Nowak", "-coś")),("1987-02-15", "1985-03-25"),["dev","dev"]]
tabelka[2][0] = "admin"
print(tabelka[0][0]+ "\t"+ tabelka[1][0]+ "\t" + tabelka[2][0])

