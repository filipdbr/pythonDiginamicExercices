from contact import Contact
from groupe import Groupe

contact1 = Contact(nom = "dabrowski", prenom = "filip", mail = "filipdabrowski@gmail.com", telephone = "000111222")
contact2 = Contact(nom = "west", prenom = "KANYE", mail = "kw@outlook.fr", telephone = "012345678910")
contact3 = Contact(nom = "west", prenom = "KANYE", mail = "kw@outlook.fr", telephone = "012345678910")
contact4 = Contact(nom = "duszczyk", prenom = "damian", mail = "dd@gmail.com", telephone = "023049204320")
contact5 = Contact(nom = "duszczyk", prenom = "paweł", mail = "dd@gmail.com", telephone = "023049204320")

print(contact1)
print(contact2)

group1 = Groupe("Favourites")
group1.ajouter_contact(contact1)
group1.ajouter_contact(contact2)
group1.ajouter_contact(contact3)
group1.ajouter_contact(contact4)
group1.ajouter_contact(contact5)

print(group1.lister_contacts())

print(group1)

print(group1.rechercher_contact("west"))

group1.export_contacts(r"C:\Users\filip\OneDrive\Pulpit\test\mytest")

