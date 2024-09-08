# créez une nouvelle dataclass "Groupe" avec les attributs `nom_groupe` et une `liste_contacts`.
from dataclasses import dataclass, field
from contact import Contact
import csv

@dataclass
class Groupe:
    nom_groupe: str
    liste_contacts: list[Contact] = field(default_factory=list)

    def ajouter_contact(self, contact: Contact):
        # Empêchez l'ajout d'un contact s'il existe déjà un contact avec le même nom ou la même adresse e-mail
        if any(c.mail == contact.mail or c.nom == contact.nom for c in self.liste_contacts):
            print(f"Le contact existe déjà dans le groupe.")
        else:
            self.liste_contacts.append(contact)
            print(f"Le contact {contact.nom} a été ajouté au groupe {self.nom_groupe}.")

    def supprimer_contact(self, mail: str):
        for contact in self.liste_contacts:
            if contact.mail == mail:
                self.liste_contacts.remove(contact)
                print(f"Le contact {contact.nom} a été supprimé du groupe {self.nom_groupe}.")
                return
        print(f"Aucun contact avec l'email {mail} trouvé dans le groupe {self.nom_groupe}.")

    def lister_contacts(self):
        if not self.liste_contacts:
            return f"Le groupe {self.nom_groupe} est vide."
        else:
            contacts_info = [f"{contact}" for contact in self.liste_contacts]
            return f"Liste des contacts du groupe {self.nom_groupe} :\n" + "\n".join(contacts_info)

    # Ajoutez une fonction pour rechercher un contact par son nom ou son adresse
    # e-mail dans la liste et afficher les informations du contact trouvé.
    def rechercher_contact(self, nom_ou_mail: str):
        for contact in self.liste_contacts:
            if contact.nom.lower() == nom_ou_mail.lower() or contact.mail.lower() == nom_ou_mail.lower():
                print(f"Contact trouvé: {contact}")
                return contact
        print(f"Aucun contact trouvé pour '{nom_ou_mail}'.")
        return None

    # - (Optionnel) Ajoutez des fonctions pour exporter la liste de contacts dans un fichier CSV et importer des contacts à partir de ce fichier.
    def export_contacts(self, nom_de_fichier : str):
        with open (nom_de_fichier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['nom', 'prenom', 'mail', 'telephone']) # headers
            for contact in self.liste_contacts:
                writer.writerow([contact.nom, contact.prenom, contact.mail, contact.telephone])
            print("Contacts have been exported")

    def import_contacts(self, nom_de_fichier : str):
        with open(nom_de_fichier, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for line in reader:
                nom, prenom, mail, telephone = line
                contact = Contact(nom=nom, prenom=prenom, mail=mail, telephone=telephone)
                self.ajouter_contact(contact)
            print(f"Contacts importés depuis le fichier {fichier}.")


