import os

students = {}

if os.path.exists("students.txt"):
    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            name = data[0]
            notes = list(map(float, data[1:]))
            students[name] = notes
    print("Données chargées depuis 'students.txt'.\n")
else:
    print("Aucun fichier de données trouvé.\n")

while True:
    print("1. Ajouter un élève et ses notes")
    print("2. voir les notes d'un élèves")
    print("3. Modifier les note d'un élèves")
    print("4. Calculer la moyenne d'un student")
    print("5. Afficher la liste des students avec leurs moyennes")
    print("6. sortir")

    choice = input("met ton choix : ")

    if choice == '1':
        nom = input("met ton nom : ")
        notes = list(map(float, input("mettez les notes de l'élève (séparées par des espaces) : ").split()))
        students[nom] = notes
        print(f"{nom} a été ajouté avec les notes {notes}.\n")
        
        with open("students.txt", "w") as file:
            for nom, notes in students.items():
                notes_str = " ".join(map(str, notes))
                file.write(f"{name} {notes_str}\n")
        print("Données sauvegardées dans 'students.txt'.\n")

    elif choice == '2':
        nom = input("Entrez le nom de l'étudiant : ")
        if nom in students:
            print(f"Notes de {nom}: {students[nom]}")
        else:
            print(f"{nom} n'existe pas dans la liste.\n")

    elif choice == '3':
        nom = input("Entrez le nom de l'étudiant : ")
        if nom in students:
            print(f"Notes actuelles de {nom}: {students[nom]}")
            index = int(input("Entrez l'indice de la note à modifier (0 pour la première note) : "))
            if 0 <= index < len(students[nom]):
                new_note = float(input(f"Entrez la nouvelle note pour {nom}: "))
                students[nom][index] = new_note
                print(f"Note modifiée. Nouvelles notes de {nom}: {students[nom]}\n")
                
                with open("students.txt", "w") as file:
                    for nom, notes in students.items():
                        notes_str = " ".join(map(str, notes))
                        file.write(f"{nom} {notes_str}\n")
                print("Données sauvegardées dans 'students.txt'.\n")
            else:
                print("Indice de note invalide.")
        else:
            print(f"{nom} n'existe pas dans la liste.\n")

    elif choice == '4':
        name = input("Entrez le nom de l'étudiant : ")
        if nom in students:
            average = sum(students[nom]) / len(students[nom])
            print(f"Moyenne des notes de {nom}: {average:.2f}\n")
        else:
            print(f"{nom} n'existe pas dans la liste.\n")

   
    elif choice == '5':
        if not students:
            print("Aucun étudiant enregistré.\n")
        else:
            print("Liste des étudiants avec leurs moyennes :")
            for nom, notes in students.items():
                average = sum(notes) / len(notes)
                print(f"{nom}: {average:.2f}")
            print()

   
    elif choice == '6':
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.\n")
