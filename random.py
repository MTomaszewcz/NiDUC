import random
import math
from random import randint
#dec to bin
def to_bin(x):
    return int(bin(x)[2:])
####################################################
#    do dzielenia modulo
def fun(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = fun(b % a, a)
        return (g, x - (b // a) * y, y)

def mod(a, m):
    g, x, y = fun(a, m)
    return x % m
####################################################
    
#wczytywanie pliku jpg
with open("jsos.jpg", "rb") as imageFile:
  f = imageFile.read()  
  b = bytearray(f)
  
  
size =len(b)
tablica =[]   #w tej tablicy przechowujemy bajty
wieksza_tablica=[] #w tej tablic bede przechowywal bity
tab =[]

################################################################################
for i in range(0,size):
    tablica.append(b[i])

for j in range(0,size):
    tablica[j]=to_bin(tablica[j])
    
print(tablica[0])
print(tablica[1])
print(tablica[2])


for i in range(0, len(tablica)):
    for j in range(0, 8):
        element = mod(tablica[i], 10)       
        tablica[i]=tablica[i]/10;
        tablica[i]=math.floor(tablica[i])
        wieksza_tablica.append(element)
        
    for z in range(0, len(wieksza_tablica)):
        tab.append(wieksza_tablica[len(wieksza_tablica)-1-z])
        
    del wieksza_tablica [:]
    

print(tab) #otrzymalismy nasze zdjecie .jpg w formie w dobrej kolekjnosci


tab_kopia = []
tab_kopia = tab
##################################################################################################################


pstwo_g_b = 1/100 #pstwo, ze ze stanu dobrego w zly

pstwo_b_g = 60/100      #pstwo, ze ze zlego w dobry

pstwo_g_g = 1-pstwo_g_b#z dobrego w dobry

pstwo_b_b = 1-pstwo_b_g# ze zlego w zly
    

was_error = False # zmienna was_error inforuje w jakim teraz jestesmy stanie true w Good; false w Bad

random.seed(42)

counter=0;

#domylnie mamy stan Good

for i in range(0, len(tab)):
    if was_error:#gdy jestesmy w Bad
        tab[i] = mod(tab[i]+1, 2)
        counter+=1;
        
        if randint(1, 100)<=60:
            was_error  = None  
            
    
    else:# gdy jestesmy w Good
        if randint(1,100)==56:
            was_error = None
            
print("\ntyle bylo bledow " + str(counter)+ "\n")

        #mam watpliwosc co do tej zmiennej "bool"

















#tablica1 =[]

#tablica1.append(random.getrandbits(1))

#print(tablica1[0])

#for i in range(0, 11):
 #  tablica1.append(random.getrandbits(1))

#print(tablica1)


