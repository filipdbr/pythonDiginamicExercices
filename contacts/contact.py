# Créez une dataclass "Contact" avec les attributs suivants : `nom`, `prenom`, `mail` et `telephone`.
from dataclasses import dataclass
import re

@dataclass
class Contact:
    nom: str
    prenom: str
    mail: str = ""  # default value
    telephone: str = ""  # default value

    def __post_init__(self):
        # Validation de l'email
        if not self.valider_email(self.mail):
            raise ValueError(f"L'adresse e-mail '{self.mail}' n'est pas valide.")

        # Validation du numéro de téléphone
        if not self.valider_telephone(self.telephone):
            raise ValueError(f"Le numéro de téléphone '{self.telephone}' n'est pas valide.")

    # getters et setters (pour

    # Getter pour 'nom'
    @property
    def nom(self):
        return self._nom

    # Setter pour 'nom', convertit automatiquement en majuscules
    @nom.setter
    def nom(self, value: str):
        self._nom = value.upper()

    # Getter pour 'prenom'
    @property
    def prenom(self):
        return self._prenom

    # Setter pour 'prenom', convertit automatiquement en format 'capitalize'
    @prenom.setter
    def prenom(self, value: str):
        self._prenom = value.capitalize()

    # méthodes

    @staticmethod
    def valider_email(email: str) -> bool:
        # Expression régulière pour valider l'email
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    @staticmethod
    def valider_telephone(telephone: str) -> bool:
        # On vérifie si le téléphone contient uniquement des chiffres et a entre 8 et 12 caractères
        return telephone.isdigit() and 8 <= len(telephone) <= 12

    def __str__(self) -> str:
        return (f"Contact[nom : {self.nom.upper()}, "
                f"prenom : {self.prenom.capitalize()}, "
                f"email : {self.mail}, "
                f"telephone : {self.telephone}]")
