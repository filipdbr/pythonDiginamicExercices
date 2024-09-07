from animal import Animal
from chien import Chien

funny = Animal("Funny",3)
fred = Animal("Fred",4)

print(Animal.population)
pluto = Animal("Pluto",5)
print(Animal.population)
print(funny.esperance_vie("chien"))
print(funny)

tola = Chien("Tola", 5.2)

print(tola)
print(tola.crier())
