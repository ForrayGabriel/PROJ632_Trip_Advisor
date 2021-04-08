import trip_asvisor as ta 

url = input("Url du restaurant : \n")

name = url.split("Reviews-")[1][:-5]

f = open(name+".txt", "w")

infos = ta.getUsernames(url)

for i in infos:
	try :
		f.write("L'utilisateur " + i[0]+ " a écrit la review :\n" + str(i[1]) + "\n\n")
		f.write("Ainsi que les reviews suivantes pour d'autres établissements :\n")
		f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	except :
		f.write("L'utilisateur a saisie un caractère interdit")

f.close()