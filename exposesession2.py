femme={}
print("bienvenue à l'enregistrement")
while True:
	print("vous etes:")
	print("1-un homme?")
	print("2-une femme?")
	print("3-un enfant?")
	print("4- pour quitter")
	reponse=int(input("votre choix:"))
	if reponse==2:
		fichfam=open("femme.txt","a")
		a=input("entrez votre nom:").lower()
		b=input("entrez votre prenom:").lower()
		c=input("entre votre age:")
		d=float(input("entrez votre taille en centimètre:"))
		fichfam.write(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+"\n")
		print("vous etes bien enregistré")
		fichfam.close()
		recherche=f"{a}"
		femme[a]={"nom: ":a,"prenom: ":b, "age: ":c, "taille: ":d}
	elif reponse!= "1" and reponse!= "2" and reponse!="3" and reponse!="4":
		restart=input("votre choix est incorrecte réessayez:")
	elif reponse==2:
		fichfam=open("femme.txt","a")
		a=input("entrez votre nom:").lower()
		b=input("entrez votre prenom:").lower()
		c=input("entre votre age:")
		d=float(input("entrez votre taille en centimètre:"))
		fichfam.write(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+"\n")
		print("vous etes bien enregistré")
		fichfam.close()
		recherche=f"{a}"
		femme[a]={"nom: ":a,"prenom: ":b, "age: ":c, "taille: ":d}
	else:
		print(" MERCI!!! et à la prochaine")
		break
