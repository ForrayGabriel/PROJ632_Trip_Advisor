import trip_asvisor as ta 
import Liste_commentaire_user as liste_com



url = input("Url du restaurant : \n")

name = url.split("Reviews-")[1][:-5]

f = open(name+".txt", "w")

infos = ta.getUsernames(url)

for i in infos:
	try :
		f.write("L'utilisateur " + i[0]+ " a écrit la review :\n" + str(i[1]) + "\n\n")
		other_reviews = liste_com.liste_Com_User(i[0])
		print(i[0])
		if other_reviews:
			f.write("Ainsi que les reviews suivantes pour d'autres établissements :\n")
			for rev in other_reviews:
				f.write(rev+"\n\n")

		f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	except :
		f.write("L'utilisateur a saisie un caractère interdit")

f.close()

