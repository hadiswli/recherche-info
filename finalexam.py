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
    print("1. Ajouter un étudiant et ses notes")
    print("2. Afficher les notes d'un étudiant")
    print("3. Modifier une note d'un étudiant")
    print("4. Calculer la moyenne des notes d'un étudiant")
    print("5. Afficher la liste des étudiants avec leurs moyennes")
    print("6. Quitter")

    choice = input("Entrez votre choix : ")

    if choice == '1':
        name = input("Entrez le nom de l'étudiant : ")
        notes = list(map(float, input("Entrez les notes de l'étudiant (séparées par des espaces) : ").split()))
        students[name] = notes
        print(f"{name} a été ajouté avec les notes {notes}.\n")
        
        with open("students.txt", "w") as file:
            for name, notes in students.items():
                notes_str = " ".join(map(str, notes))
                file.write(f"{name} {notes_str}\n")
        print("Données sauvegardées dans 'students.txt'.\n")

    elif choice == '2':
        name = input("Entrez le nom de l'étudiant : ")
        if name in students:
            print(f"Notes de {name}: {students[name]}")
        else:
            print(f"{name} n'existe pas dans la liste.\n")

    elif choice == '3':
        name = input("Entrez le nom de l'étudiant : ")
        if name in students:
            print(f"Notes actuelles de {name}: {students[name]}")
            index = int(input("Entrez l'indice de la note à modifier (0 pour la première note) : "))
            if 0 <= index < len(students[name]):
                new_note = float(input(f"Entrez la nouvelle note pour {name}: "))
                students[name][index] = new_note
                print(f"Note modifiée. Nouvelles notes de {name}: {students[name]}\n")
                
                with open("students.txt", "w") as file:
                    for name, notes in students.items():
                        notes_str = " ".join(map(str, notes))
                        file.write(f"{name} {notes_str}\n")
                print("Données sauvegardées dans 'students.txt'.\n")
            else:
                print("Indice de note invalide.")
        else:
            print(f"{name} n'existe pas dans la liste.\n")

    elif choice == '4':
        name = input("Entrez le nom de l'étudiant : ")
        if name in students:
            average = sum(students[name]) / len(students[name])
            print(f"Moyenne des notes de {name}: {average:.2f}\n")
        else:
            print(f"{name} n'existe pas dans la liste.\n")

   
    elif choice == '5':
        if not students:
            print("Aucun étudiant enregistré.\n")
        else:
            print("Liste des étudiants avec leurs moyennes :")
            for name, notes in students.items():
                average = sum(notes) / len(notes)
                print(f"{name}: {average:.2f}")
            print()

   
    elif choice == '6':
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.\n")
