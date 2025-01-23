homme={}
femme={}
enfant={}
print("Bienvenue dans le programme de gestion")
while True:
    choix=int(input("1. Pour passer a l'enregistrement\n2. Pour afficher la liste de chaque type de personnes\n3. Pour donner le nombre de chaque type de personnes enregistrer\n4. Pour quitter le programme\nVotre choix: "))
    if choix==1:
        while True: 
            choix1=int(input("1. Homme\n2. Femme\n3. Enfant\n4. Retour\n5. Supprimer un enregistrement\nVotre choix: "))
            if choix1==1:
                h=open("hommes.tkt","a")
                noms=str(input("Entrez le nom: ")).lower()
                prenoms=str(input("Entrez le prénom: ")).lower()
                ages=int(input("Entrez l'âge: "))
                tailles=float(input("Entrez la taille (en cm): "))
                h.write("Nom: "+str(noms) +" ,Prenom: "+str(prenoms) +" ,Age: "+str(ages) +" ,Taille ( en cm ): "+str(tailles)+"\n")
                h.close()
                nom_cle=f"{noms}"
                homme[noms]={"Nom: ": noms,"Prénom: ":prenoms,"Âge: ":ages,"Taille :": tailles}
                print("Enregistrement réussi")
            elif choix1==2:
                f=open("femmes.tkt","a")
                noms=str(input("Entrez le nom: ")).lower()
                prenoms=str(input("Entrez le prénom: ")).lower()
                ages=int(input("Entrez l'âge: "))
                tailles=float(input("Entrez la taille (en cm): "))
                f.write("Nom: "+str(noms) +" ,Prenom: "+str(prenoms) +" ,Age: "+str(ages) +" ,Taille ( en cm ): "+str(tailles)+"\n")
                f.close()
                nom_cle=f"{noms}"
                femme[noms]={"Nom: ": noms,"Prénom: ":prenoms,"Âge: ":ages,"Taille :": tailles}
                print("Enregistrement réussi")
            elif choix1==3:
                e=open("enfant.txt","a")
                n=input("Entrez votre nom: ").lower()
                p=input("Entrez votre prénom: ").lower()
                a=int(input("Entrez votre age: "))
                t=input("Entrez votre taille (en cm bien-sur): ")
                g=input("Tu es un petit garçon ou une petite fille: ").lower()
                e.write("Nom:"+str(n)+" Prenom:"+str(p)+" Age:"+str(a)+" Taille:"+str(t)+" Genre:"+str(g))
                e.close()
                enfant_recherche=f"{n}"
                enfant[n]={"Nom ":n,"Prénom ":p," Age ":a,"Taille ":t,"Genre ":g}
                print("Enregistrement réussi")
            elif choix1==4:
                break
            elif choix1==5:
                while True:
                    choix2 = int(input("1. Homme\n2. Femme\n3. Enfant\n4. Retour\nVotre choix: "))
                    if choix2 == 1:
                        with open("hommes.tkt", "r") as h:
                            lines = h.readlines()
                        nom_cle = str(input("Entrez le nom de la personne à supprimer: ")).lower()
                        with open("hommes.tkt", "w") as h:
                            for line in lines:
                                if nom_cle not in line.lower():
                                    h.write(line)
                        print(nom_cle, "a été supprimé.")
                    elif choix2 == 2:
                        with open("femmes.tkt", "r") as f:
                            lines = f.readlines()
                        nom_cle = str(input("Entrez le nom de la personne à supprimer: ")).lower()
                        with open("femmes.tkt", "w") as f:
                            for line in lines:
                                if nom_cle not in line.lower():
                                    f.write(line)
                        print(nom_cle, "a été supprimé.")
                    elif choix2 == 3:
                        with open("enfant.txt", "r") as e:
                            lines = e.readlines()
                        nom_cle = str(input("Entrez le nom de la personne à supprimer: ")).lower()
                        with open("enfant.txt", "w") as e:
                            for line in lines:
                                if nom_cle not in line.lower():
                                    e.write(line)
                        print(nom_cle, "a été supprimé.")
                    elif choix2 == 4:
                        break
            else:
                print("Choix incorrect, réesayer: ")
    elif choix==2:
        while True:
            choix3=int(input("1. Homme\n2. Femme\n3. Enfant\n4. Retour\nVotre choix: "))
            if choix3==1:
                h=open("hommes.tkt","r")
                print(h.read())
                h.close()
            elif choix3==2:
                f=open("femmes.tkt","r")
                print(f.read())
                f.close()
            elif choix3==3:
                e=open("enfant.txt","r")
                print(e.read())
                e.close()
            elif choix3==4:
                break
            else:
                print("Choix incorrect, Réesayer: ")
    elif choix==3:
        print("Hommes: ",len(homme))
        print("Femmes: ",len(femme))
        print("Enfants: ",len(enfant))
    elif choix==4:
        print("Merci d'avoir utiliser notre programme")
        break
    else:
        print("Choix incorrect, Réessayez: ")           



