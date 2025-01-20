homme={}
print("Enregistrement des Hommes")
while True:
    choix=int(input("Tapez 1 pour enregistrer ou 5 pour quittez l'enregistrement: "))
    if choix==1:
        h=open("hommes.tkt","a")
        noms=str(input("Entrez le nom: ")).lower()
        prenoms=str(input("Entrez le prénom: ")).lower()
        ages=int(input("Entrez l'âge: "))
        tailles=float(input("Entrez la taille (en cm): "))
        h.write("Nom: "+str(noms) +" ,Prenom: "+str(prenoms) +" ,Age: "+str(ages) +" ,Taille ( en cm ): "+str(tailles)+"\n")
        h.close()
        nom_cle=f"{noms}"
        homme[noms]={"Nom: ": noms,"Prénom: ":prenoms,"Âge: ":ages,"Taille :": tailles}
    elif choix==5:
        print("Fin du programme.")
        break
    else:
        print("Choix incorret, Réesayer: ")