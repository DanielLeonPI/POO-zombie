from persona import Persona
from zombie import Zombie
import os

os.system("cls")
print()
print(" La ciudad se ha llenado de zombis.")
print(" Estas en la calle 1 y has de llegar")
print(" a la calle 40 para poder salvarte.")
print(" Los zombis avanzan 1, 2 ó 3 calles.")
print(" Tú puedes avanzar 1, 2 o 3 calles.")
print()
nombre = input(" ¿Estás preparado? Cuál es tu nombre: ").capitalize()

jugador = Persona(nombre)

horda = []

for i in range(10):
    z = Zombie()
    horda.append(z)

while True:
    os.system("cls")
    print(jugador.situacion())
    calles = []
    for zombi in horda:
        calles.append(zombi.calle)
    calles.sort()
    print("Hay zombis en las calles:")
    for elemento in calles:
        print(elemento, end=" ")
