import json

from biblio.livre import Livre
from biblio.livre_empruntable import LivreEmpruntable


class Bibliotheque:
    # Initialize the library with a name and an empty list of books
    def __init__(self, nom: str):
        self.nom = nom
        self.livres = []

    # Add a book to the library
    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la bibliothèque.")

    # Remove a book by its title
    def retirer_livre(self, titre: str):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                print(f"Le livre '{titre}' a été retiré de la bibliothèque.")
                return
        print(f"Le livre '{titre}' n'a pas été trouvé dans la bibliothèque.")

    # List all books in the library
    def lister_livres(self):
        if not self.livres:
            print("Aucun livre disponible dans la bibliothèque.")
        else:
            print("Livres disponibles dans la bibliothèque :")
            for livre in self.livres:
                print(livre.details())

    # Borrow a book by its title if available
    def emprunter_livre(self, titre: str):
        for livre in self.livres:
            if isinstance(livre, LivreEmpruntable) and livre.titre == titre:
                livre.emprunter()
                return
        print(f"Le livre '{titre}' n'est pas disponible pour emprunt ou n'existe pas.")

    # Return a book by its title
    def retourner_livre(self, titre: str):
        for livre in self.livres:
            if isinstance(livre, LivreEmpruntable) and livre.titre == titre:
                livre.retourner()
                return
        print(f"Le livre '{titre}' n'est pas disponible pour retour ou n'existe pas.")

    # Load data at the beginning of the session.
    def load_data(self):
        pass

    # Method to dump data to a JSON file
    def dump_data(self, file_name: str):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump([livre.to_dict() for livre in self.livres], file)
        print(f"Les données ont été enregistrées dans {file_name}.")

    # Method to load data from a JSON file
    def load_data(self, file_name: str):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.livres = []
                for item in data:
                    if item["type"] == "Livre":
                        self.livres.append(Livre.from_dict(item))
                    elif item["type"] == "LivreEmpruntable":
                        self.livres.append(LivreEmpruntable.from_dict(item))
            print(f"Les données ont été chargées depuis {file_name}.")
        except FileNotFoundError:
            print(f"Le fichier {file_name} n'existe pas.")