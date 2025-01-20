enfant={}
print("Enregistrement des enfants")
while True:
	choix=int(input("Tapez 3 pour enregistrer ou 5 pour quittez l'enregistrement"))
	if choix==3:
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
		print("enregistrement terminé")
		break







