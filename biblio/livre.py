class Livre:
    # Initialize the book with title, author, and publication year
    def __init__(self, titre: str, auteur: str, annee: int):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    # Method to return the book details as a formatted string
    def details(self) -> str:
        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année de publication : {self.annee}"

    @classmethod
    def from_dict(cls, data):
        livre = cls(data["titre"], data["auteur"], data["annee"])
        livre.disponible = data["disponible"]
        return livre