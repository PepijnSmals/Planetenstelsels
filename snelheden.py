import math as mt
from scipy.interpolate import interp1d
import numpy as np

Mz = 1.989e30
AU = 1.496e11
G = 6.674e-11
#Opdracht 2
#1
#Formule die de ontsnappingsnelheid berekent voor een gegeven massa en afstand 
def Vesc(M, R):
    Vesc =  mt.sqrt((2*G*M)/R)
    return Vesc

#2
#De komeet P67 is aan de zon gebonden. De maximale snelheid die deze dus kan 
#hebben is de ontsnapingssnelheid geboden aan de zon. Gegeven is de minimale
#van de komeet (1.24 AU). Dus de maximale snelheid is:

print(Vesc(Mz, 1.24*AU))

#3a
#De tabel overnemen als array met r de straal en v de snelheid
r = [1.3*AU, 2.5*AU, 3.3*AU, 4.3*AU, 5.4*AU]
v = [33.3e3, 21.3e3, 16.8e3, 12.5e3, 8.5e3]

#Hier voeren we de interpolatie uit. We maken een functie die lineair loopt en
#de snelheid uitrekent tussen 1.3AU en 5.4AU in 100 stappen.
f = interp1d(r, v, kind = "lineair")
#met de np.linspace wordt het opgedeeld in 100 stappen.
R = np.linspace(1.3*AU, 5.4*AU, 100)
V = f(R)
print(V)