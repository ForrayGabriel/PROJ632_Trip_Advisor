import restaurant_finder as rf
import user_com_finder as ucf

# Asking the user for the url
url = input("Url du restaurant : \n")

# Name of the restaurant
name = url.split("Reviews-")[1][:-5]

# Creating a new text file for the restaurant
f = open(name + ".txt", "w")

# Getting all the usernames and reviews for the restaurant
infos = rf.getUsernames(url)

# For every reviews
for i in infos:
	try:
		# Write the user name and its review
		f.write("L'utilisateur " + i[0] + " a écrit la review :\n" + str(i[1]) + "\n\n")

		# Get the other reviews from the user
		other_reviews = ucf.liste_Com_User(i[0])
		print(i[0])

		# Get and write all the other reviews
		if other_reviews:
			f.write("Ainsi que les reviews suivantes pour d'autres établissements :\n")
			for rev in other_reviews:
				f.write(rev + "\n\n")
		f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	except:
		f.write("L'utilisateur a saisie un caractère interdit\n")

f.close()
