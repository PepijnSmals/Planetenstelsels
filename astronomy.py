#Importeren van module voor het inlezen van data van de planeten en voor het 
#gebruik van pi

from astropy.table import Table

#Natuurkundige constantes

G = 6.673e-11 #m3s-2kg-1
h = 6.626e-34 #m2kgs-1
c = 2.998e-11 #ms-1
AU = 1.496e11 #m
Mz = 1.9889e30 #kg
Rz = 6.9634e8 #m
Ma = 5.9722e24 #kg
Ra = 6.371e6 #m 
Mj = 1.898e27 #kg
pc = 3.08568e16 #m
Mm = 7.342e22 #kg
Dam = 384400e3 #m

#Formule zwaartekracht

def Fgrav(m1,m2,r):
    F = (m1 * m2)/(r**2) * G
    return F

#Versnellingen van het ISS door verschillende hemellichamen. Aangezien a = F/m
#valt de massa van het ISS(m2) weg, dus vullen we daarvoor 1 in.

a_ISS_aarde = Fgrav(Ma,1, Ra + 407000)
print(a_ISS_aarde)
a_ISS_zon = Fgrav(Mz, 1, AU)
print(a_ISS_zon)
a_ISS_maan = Fgrav(Mm, 1, Dam - 407000)
print(a_ISS_maan)

#Importeren van de gegevens van sommige planeten

planeten = Table.read("planeet-gegevens.txt", format='csv').to_pandas(index
                   ='name')

#De nodige modules importeren
from matplotlib import pyplot as plt

y = planeten["density"]
x = planeten["Rmean"]

plt.plot(x, y, "ro", label= "planeten")
plt.hlines(0.997,0,8e4, label= "dichtheid water")
plt.hlines(7.874,0,5e4, label= "dichtheid ijzer")
plt.hlines(1.5 , 0, 8e4, label= "dichtheid zand")
plt.title("Dichtheid tegen straal van 8 planeten")
plt.xlabel("Straal in km")
plt.ylabel("Dichtheid in g/cm3")
plt.legend(loc="upper right")