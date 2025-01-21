print("Vous etes:")
print("1-Un homme?")
print("2-Une femme?")
print("3-Un enfant?")
print("4-Pour quitter le programme")
print("5- afficher tous les enregistrements")
homme={}
while True:
    reponse=int(input("votre choix pour l'enregistrement:"))
    if reponse==1:
        h=open("hommes.tkt","a")
        noms=str(input("Entrez le nom: ")).lower()
        prenoms=str(input("Entrez le prénom: ")).lower()
        ages=int(input("Entrez l'âge: "))
        tailles=float(input("Entrez la taille (en cm): "))
        h.write("Nom: "+str(noms) +" ,Prenom: "+str(prenoms) +" ,Age: "+str(ages) +" ,Taille ( en cm ): "+str(tailles)+"\n")
        h.close()
        nom_cle=f"{noms}"
        homme[noms]={"Nom: ": noms,"Prénom: ":prenoms,"Âge: ":ages,"Taille :": tailles}
    elif reponse==4:
        print(" MERCI!!! et à la prochaine")
        break
    femme={}
	if reponse==2:
	fichfam=open("femme.txt","a")
	no=input("entrez votre nom:").lower()
	pr=input("entrez votre prenom:").lower()
	ag=input("entre votre age:")
	ta=float(input("entrez votre taille en centimètre:"))
	fichfam.write(str(no)+" "+str(pr)+" "+str(ag)+" "+str(ta)+"\n")
	print("vous etes bien enregistré")
	fichfam.close()
	recherche=f"{no}"
	femme[no]={"nom: ":no,"prenom: ":pr, "age: ":ag, "taille: ":ta}
enfant={}
	if reponse==3:
	e=open("enfant.txt","a")
	n=input("Entrez votre nom").lower()
	p=input("Entrez votre prénom").lower()
	a=int(input("Entrez votre age?"))
	t=input("Entrez votre taille (en cm bien-sur)")
	g=input("Tu es un petit garçon ou une petite fille?").lower()
	e.write("Nom:"+str(n)+" Prenom:"+str(p)+" Age:"+str(a)+" Taille:"+str(t)+" Genre:"+str(g))
	e.close()
	enfant_recherche=f"{n}"
	enfant[n]={"Nom ":n,"Prénom ":p," Age ":a,"Taille ":t,"Genre ":g}
	else:
	restart=input("votre choix est incorrecte réessayez:")
	ensemble_genre={[homme],[femme],[enfant]}
	tableau=open("ensemble.txt","w")
	tableau.write(h,fichfam,e)
	if reponse==5:
	print("A- pour les hommes")
	print("B-pour les femmes")
	print("C-pour les enfants")
	affiche=input("votre decision:")
	
		
	

