from animal import Animal

# Créez une sous-classe `Chien` de la classe `Animal`.
class Chien(Animal):

    # constructeur
    def __init__(self, nom : str, age : int ):
        super().__init__(nom, age)

    # surchargez la méthode `crier`. La méthode `crier` de la classe `Chien` doit renvoyer "Woof!".
    def crier(self) -> str:
        return "Woof!"

    # overwrite toString
    def __str__(self) -> str:
        return f"Chien[nom : {self.nom}, age : {self.age} ans]"