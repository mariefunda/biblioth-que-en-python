
import livre


def menu_principal():
    print("1.ajouter un livre")
    print("2.rechercher un livre")
    print("3.suprimer un livre")
    print("4.afficher un livre")
    print("5.emprunter un livre")
    print("6.retourner un livre")
    print("7.quitter le programme")
    choix = int(input("selectionnez une option"))
    return choix
    
def main():
    while true:
       choix = menu_principal()
       if choix == 1:
            livre.ajouterLivre()
       elif choix == 2:
            print('')
       elif choix == 3:
            print('')
       elif choix == 4:
            print('')

       elif choix == 5:
            print('')
       elif choix == 6:
            print('') 
       elif choix == 7:
            print('')
       else:
            print('')
            break




            
            
            