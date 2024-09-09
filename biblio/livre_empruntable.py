from biblio.livre import Livre


class LivreEmpruntable(Livre):
    # Initialize with the inherited attributes and set 'disponible' to True
    def __init__(self, titre: str, auteur: str, annee: int):
        super().__init__(titre, auteur, annee)
        self.disponible = True

    # Override method to include availability status in the details
    def details(self) -> str:
        disponibilite = "Disponible" if self.disponible else "Emprunté"
        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année de publication : {self.annee}, Disponibilité : {disponibilite}"

    # Method to borrow a book if available
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' est déjà emprunté.")

    # Method to return a borrowed book
    def retourner(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre '{self.titre}' a été retourné.")
        else:
            print(f"Le livre '{self.titre}' n'est pas emprunté.")

    def to_dict(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "annee": self.annee,
            "disponible": self.disponible,
            "type": "LivreEmpruntable"
        }