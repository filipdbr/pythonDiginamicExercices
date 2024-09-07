from abc import ABC, abstractmethod

#Création de la classe Animal
class Animal(ABC):

    population : int = 0 # joutez une propriété statique `population` à la classe `Animal`

    # constructeur
    def __init__(self, nom : str, age : int ):
        self.nom = nom
        self.age = age
        Animal.population += 1 ## incremente le nombre d'animaux

    # getters and setters
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, nouveau_age):
        self._age = nouveau_age

    # méthodes

    # Ajoutez une méthode appelée `crier` à la classe `Animal`.
    def crier(self):
        pass

    # Ajoutez une méthode de classe appelée `esperance_vie` à la classe `Animal`.
    # Cette méthode doit renvoyer une espérance de vie moyenne (par exemple, 10 ans).
    def esperance_vie(self, type_animal : str) -> float:
        if type_animal == 'chien':
            return 10
        if type_animal == 'chat':
            return 8.5

    # Ajoutez la méthode magique `__str__` à la classe `Animal`.
    def __str__(self):
        return f"Animal[nom : {self.nom}, age : {self.age} ans.]"

    # Ajoutez une méthode statique appelée `nombre_animaux` à la classe `Animal`.
    @staticmethod
    def nombre_animaux():
        return Animal.population