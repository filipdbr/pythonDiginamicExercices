from biblio.bibliotheque import Bibliotheque
from biblio.livre_empruntable import LivreEmpruntable

# Create the library
biblio = Bibliotheque("Bibliothèque Municipale")

# Add borrowable books
livre1 = LivreEmpruntable("L'Étranger", "Albert Camus", 1942)
livre2 = LivreEmpruntable("1984", "George Orwell", 1949)
livre3 = LivreEmpruntable("L'insoutenable légèreté de l'être", "Milan Kundera", 1984)
livre4 = LivreEmpruntable("La Peste", "Albert Camus", 1947)
livre5 = LivreEmpruntable("Anna Karénine", "Léon Tolstoï", 1877)
livre6 = LivreEmpruntable("Les Frères Karamazov", "Fiodor Dostoïevski", 1880)
livre7 = LivreEmpruntable("Le Maître et Marguerite", "Mikhaïl Boulgakov", 1967)

# Adding books to my bibliotheque
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)
biblio.ajouter_livre(livre4)
biblio.ajouter_livre(livre5)
biblio.ajouter_livre(livre6)
biblio.ajouter_livre(livre7)

# List the books in the library
biblio.lister_livres()

# Borrow a book
biblio.emprunter_livre("1984")
biblio.emprunter_livre("La Peste")


# List the books after borrowing
biblio.lister_livres()

# Return the borrowed book
biblio.retourner_livre("1984")

# List the books after returning
biblio.lister_livres()

biblio.dump_data(r"C:\Users\filip\OneDrive\Pulpit\test\bibliotheque.json")

biblio2 = Bibliotheque(nom="Bibliotheque de Montpellier")

biblio2.load_data(r"C:\Users\filip\OneDrive\Pulpit\test\bibliotheque_test_source.json")

biblio2.lister_livres()
