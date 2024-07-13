livres = []

def validerTitre(titre) :
    if titre.strip() ==  "":
        print("le titre n'est peut pas etre vide.")
        return False
    if titre.isdigit():
        print("le titre ne peut pas etre un chiffre.")
        return False
    for char in titres:
        if not char.isalnum() and not char.isspace():
            print("le titre ne doit pas contenir de caracteres speciaux.")
            return False
        return True

        
def validerAuteur(auteur) :
    if auteur.strip() == "" :
        print("le no, de l'auteur ne peut pas etre vide.")
        return False
    if auteur.isdigit():
        print("le nom de l'auteurne peut pas etre un chiffre .")
        return False
    for char in auteur:
        if not char. isalpha() and not char.isspace():
            print("le nom del'auteur ne doit pas contenir des caracteres speciaux.")
            return False
    return True
def validerGenre(genre):
    genre_valides = ["Fiction","science-Fiction","Fantaisie","Bibliographie","Histoire","Aventure"]
    if genre.strip() == "":
        print("le genre ne peut pas etre vide.")
        return False
    return True

def validerLivre(titre,auteur,genre):
    titre_valide = valider_titre (titre)
    auteur_valide = valider_auteur(auteur)
    genre_valide =valider_genre(genre)
    return titre_valide and auteur_valide and genre_valide
        
def ajouterlivre() :
    disponibleLivre = true
    try:
        idlivre = int(input("saisir l'ID du livre :) "))
    except valueError:
        print("l'ID du livre doit etre un nombre entier.")

titreLivre = input("saisirle titre du livre:")
auteurLivre = input("saisir le nom de l'auteur :")



     
