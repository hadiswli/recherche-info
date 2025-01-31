import os

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\n--- Menu ---")
    print("1. Ajouter un étudiant")
    print("2. Afficher les notes d'un étudiant")
    print("3. Modifier la note d'un étudiant")
    print("4. Calculer la moyenne des notes d'un étudiant")
    print("5. Afficher la liste des étudiants avec leurs moyennes")
    print("6. Sauvegarder les données")
    print("7. Charger les données")
    print("8. Quitter")

# Fonction pour ajouter un étudiant et ses notes
def ajouter_etudiant(etudiants):
    nom = input("Entrez le nom de l'étudiant : ")
    notes = []
    while True:
        try:
            note = float(input("Entrez une note (ou -1 pour terminer) : "))
            if note == -1:
                break
            elif 0 <= note <= 20:  # Vérification que la note est valide
                notes.append(note)
            else:
                print("La note doit être entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer une valeur numérique.")
    etudiants[nom] = notes
    print(f"Étudiant {nom} ajouté avec succès.")

# Fonction pour afficher les notes d'un étudiant
def afficher_notes(etudiants):
    nom = input("Entrez le nom de l'étudiant : ")
    if nom in etudiants:
        print(f"Les notes de {nom} sont : {etudiants[nom]}")
    else:
        print("L'étudiant n'existe pas.")

# Fonction pour modifier la note d'un étudiant
def modifier_note(etudiants):
    nom = input("Entrez le nom de l'étudiant : ")
    if nom in etudiants:
        try:
            index = int(input("Entrez l'indice de la note à modifier (0 pour la première note, etc.) : "))
            nouvelle_note = float(input("Entrez la nouvelle note : "))
            if 0 <= nouvelle_note <= 20:
                etudiants[nom][index] = nouvelle_note
                print(f"La note de {nom} a été modifiée.")
            else:
                print("La note doit être entre 0 et 20.")
        except (ValueError, IndexError):
            print("Indice ou note invalide.")
    else:
        print("L'étudiant n'existe pas.")

# Fonction pour calculer la moyenne des notes d'un étudiant
def calculer_moyenne(etudiants):
    nom = input("Entrez le nom de l'étudiant : ")
    if nom in etudiants:
        notes = etudiants[nom]
        if notes:
            moyenne = sum(notes) / len(notes)
            print(f"La moyenne des notes de {nom} est : {moyenne:.2f}")
        else:
            print("L'étudiant n'a pas de notes.")
    else:
        print("L'étudiant n'existe pas.")

# Fonction pour afficher la liste des étudiants avec leurs moyennes
def afficher_etudiants(etudiants):
    if etudiants:
        print("\nListe des étudiants et leurs moyennes :")
        for nom, notes in etudiants.items():
            if notes:
                moyenne = sum(notes) / len(notes)
                print(f"{nom} : {moyenne:.2f}")
            else:
                print(f"{nom} : Pas de notes disponibles")
    else:
        print("Aucun étudiant enregistré.")

# Fonction pour sauvegarder les données dans un fichier
def sauvegarder_donnees(etudiants):
    with open("students.txt", "w") as file:
        for nom, notes in etudiants.items():
            notes_str = ",".join(map(str, notes))  # Conversion des notes en chaîne
            file.write(f"{nom}:{notes_str}\n")
    print("Données sauvegardées avec succès.")

# Fonction pour charger les données depuis un fichier
def charger_donnees():
    etudiants = {}
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                nom, notes_str = line.strip().split(":")
                notes = list(map(float, notes_str.split(",")))
                etudiants[nom] = notes
        print("Données chargées avec succès.")
    else:
        print("Aucun fichier de données trouvé.")
    return etudiants

# Fonction principale du programme
def main():
    etudiants = {}
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-8) : ")

        if choix == "1":
            ajouter_etudiant(etudiants)
        elif choix == "2":
            afficher_notes(etudiants)
        elif choix == "3":
            modifier_note(etudiants)
        elif choix == "4":
            calculer_moyenne(etudiants)
        elif choix == "5":
            afficher_etudiants(etudiants)
        elif choix == "6":
            sauvegarder_donnees(etudiants)
        elif choix == "7":
            etudiants = charger_donnees()
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Essayez à nouveau.")

# Lancement du programme
if __name__ == "__main__":
    main()

