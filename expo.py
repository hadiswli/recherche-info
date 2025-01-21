def enregistrer_personne(type_personne):
    if type_personne == "homme":
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = input("Âge: ")
        taille = input("Taille (cm): ")
        with open("hommes.txt", "a") as file:
            file.write(f"{nom}_{prenom}_{age}_{taille}\n")
    elif type_personne == "femme":
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = input("Âge: ")
        taille = input("Taille (cm): ")
        with open("femmes.txt", "a") as file:
            file.write(f"{nom}_{prenom}_{age}_{taille}\n")
    elif type_personne == "enfant":
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = input("Âge: ")
        with open("enfants.txt", "a") as file:
            file.write(f"{nom}_{prenom}_{age}\n")

def afficher_liste(type_personne):
    filename = {"homme": "hommes.txt", "femme": "femmes.txt", "enfant": "enfants.txt"}
    try:
        with open(filename[type_personne], "r") as file:
            print(f"Liste des {type_personne}s :")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Aucune donnée trouvée pour {type_personne}s.")

def rechercher_par_nom(nom):
    for file_name in ["hommes.txt", "femmes.txt", "enfants.txt"]:
        try:
            with open(file_name, "r") as file:
                for line in file:
                    if nom.lower() in line.lower():
                        print(f"Trouvé dans {file_name}: {line.strip()}")
        except FileNotFoundError:
            continue

def compter_personnes():
    totals = {"hommes": 0, "femmes": 0, "enfants": 0}
    for type_personne in totals.keys():
        try:
            with open(f"{type_personne}.txt", "r") as file:
                totals[type_personne] = sum(1 for line in file)
        except FileNotFoundError:
            continue
    total_global = sum(totals.values())
    print(f"Total Hommes: {totals['hommes']}")
    print(f"Total Femmes: {totals['femmes']}")
    print(f"Total Enfants: {totals['enfants']}")
    print(f"Total Général: {total_global}")

def main():
    while True:
        print("\nMenu:")
        print("1. Enregistrer un Homme")
        print("2. Enregistrer une Femme")
        print("3. Enregistrer un Enfant")
        print("4. Afficher la liste des Hommes")
        print("5. Afficher la liste des Femmes")
        print("6. Afficher la liste des Enfants")
        print("7. Rechercher une personne par nom")
        print("8. Afficher le nombre total de personnes")
        print("9. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            enregistrer_personne("homme")
        elif choix == "2":
            enregistrer_personne("femme")
        elif choix == "3":
            enregistrer_personne("enfant")
        elif choix == "4":
            afficher_liste("homme")
        elif choix == "5":
            afficher_liste("femme")
        elif choix == "6":
            afficher_liste("enfant")
        elif choix == "7":
            nom = input("Entrez le nom à rechercher: ")
            rechercher_par_nom(nom)
        elif choix == "8":
            compter_personnes()
        elif choix == "9":
            print("Merci d'avoir utilisé l'application!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()


