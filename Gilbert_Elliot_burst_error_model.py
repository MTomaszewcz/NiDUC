#Przyklad ze strony(.pdf): http://www.ohohlfeld.com/paper/hasslinger_hohlfeld-mmb_2008.pdf

# a to p-stwo wystapienia jedynki P(1)
# b to p-stwo  wystapienia jedynki pod warunkiem ze przeslano jedynke P(1|1)
# c to pstwo ze
#                c= P(111)/(P(101) + P(111))

# 1-r = (a*c-b*b)/(2*a*c - b(a+c))

# h = 1 - (b)/(1-r)

# p = (a*r)/(1-h-a)

#----------------------------------------------------------------

# ewentualnie do przyjecia: (tylko przy dużej obserwacji)

# h = 0.5

# 1-r = 2*b

#----------------------------------------------------------------
# ABEL - average burst error length

# r = 1/ABEL 

# p = (pE* r)/(h-pE)
#----------------------------------------------------------------
import random

p1=1/2
p0=1/2

was_error = None # zmienna was_error inforuje w jakim teraz jestesmy stanie 
tablica = []

for i in range(0, 101): # losujemy 100 bitow
   tablica.append(random.getrandbits(1))
   
print(tablica)

tab_ae = tablica #na innej tablicy "przyprawiamy ja o bledy"
#print(tab_ae)

for i in range(0, 101):
    if was_error == None :
        #zmien zgodnie z p-stwem
    else:
        #zmien zgodnie z p-stwem


