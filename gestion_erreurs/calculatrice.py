from gestion_erreurs.valeur_negative_exception import ValeurNegativeException


class Calculatrice:

    # 1. Créez une fonction appelée `calculatrice` qui prend trois arguments : `nombre1` (un nombre), `nombre2` (un nombre), et `operation`
    # (une chaîne de caractères représentant l'opération à effectuer, par exemple : "+", "-", "*", "/").
    def calculatrice(nombre1 : float | int, nombre2 : float | int, operation):
        try:
            if operation == "+":
                resultat = nombre1 + nombre2
            elif operation == "-":
                resultat = nombre1 - nombre2
            elif operation == "*":
                resultat = nombre1 * nombre2
            elif operation == "/":
                resultat = nombre1 / nombre2 # vulnerable to errors
            else:
                return "Opération non valide"
            return resultat

        except ZeroDivisionError:
            return "Erreur : Division par zéro n'est pas possible."
        except TypeError:
            return "Erreur : Les deux arguments doivent être des nombres."
        except Exception as e:
            return f"Une erreur s'est produite : {e}"

    # Testing
    a = 5
    b = 4.5
    c = 0

    print(calculatrice(a,b,"+")) # Résultat attendu : 9.5
    print(calculatrice(a, b, "-"))  # Résultat attendu : 0.5
    print(calculatrice(a, b, "*"))  # Résultat attendu : 22.5
    print(calculatrice(a, c, "/"))  # Résultat attendu : "Division par zéro impossible."

    # part 2: L'objectif de cet exercice est de créer une exception personnalisée
    # appelée `ValeurNegativeException` qui sera levée chaque fois qu'une valeur négative est rencontrée.
    def verifier_valeur(nombre: int | float):
        if nombre < 0:
            raise ValeurNegativeException() # raises the error if value is negative
        else:
            return f"La valeur de {nombre} est valide."

    # declaration of attributs for testing
    a = 2
    b = 0
    c = -2

    # testing
    try:
        print(verifier_valeur(a)) # Résultat attendu : La valeur est valide.
        print(verifier_valeur(b)) # Résultat attendu : La valeur est valide.
        print(verifier_valeur(c)) # Résultat attendu : La valeur ne peut pas être négative.
    # except catches the error if raised in the function and prints the proper message
    except ValeurNegativeException as e:
        print(e)

