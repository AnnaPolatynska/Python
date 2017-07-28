# -*- coding: utf-8 -*-
'''
#zaimportowany mod1
import mod1

print(mod1.a)
mod1.info()

a= mod1.Nowa()
a.witaj()
'''
'''
# bez aliasu 2 metoda importu
from mod1 import *

print(a)
info()

a= Nowa()
a.witaj()

# klasy w oddzielnychplikach
# py cash dane przejściowe w kaatlogu auto
'''

'''
import Pakiet.mod1
#lub 2 sposób ale u mnie nie dziala
#from Pakiet.mod1 import *

#plik w tej samej kokalizacji co plik python "w" to tryb

print(Pakiet.mod1)

'''


#utworzenie pliku
F= open("plik.txt", "w")
# print wywołuje czy zamknięto ścieżkę dostępu =print(F.close, F.mode, F.name)
print(F.close, F.mode, F.name)
#zapisanie do pliku
F.write("początek pliku")
F.write("kolejny napis")


#F.writelines(["\n3 linia","\n4 linia","\n5 linia"]) - przejście do nowej linii
F.writelines(["\n3 linia","\n4 linia","\n5 linia"])

F.close
print(F.close, F.mode, F.name)

print
# odczyt z pliku do pythona

G = open("plik.txt", "r")
print (G.read(10))
print(G.tell())
#print(G.tell(5))
