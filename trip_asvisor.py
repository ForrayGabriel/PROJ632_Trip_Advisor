from bs4 import BeautifulSoup
import urllib.request as urllib2



def traitement(str):
	for i in range(6,len(str)):
		if str[i] == "<":
			return str[5:i]


def search(url):

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content, features="html.parser")

	for review in soup.find_all("div","review-container",):
		rew = str(review)
		test = rew.split('<div class="info_text pointer_cursor" onclick="widgetEvCall(\'handlers.usernameClick\', event, this);">')
		print(traitement(test[1]))
		test2 = rew.split('<p class="partial_en')
		print(traitement(test2[1]))

def getUrl(url, nbPages):
	res = []
	for i in range(len(url)):
		if url[i:i+8] == "Reviews-":
			part1 = url[:i+8]
			part2 = url[i+8:]
			print(part1)
			print(part2)

	for i in range(nbPages):
		res.append(part1+"or"+str(i)+"0-"+part2)
	print(res)


def getNbPages(url):

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content, features="html.parser")

	liens = soup.find_all("a")

	print(liens)


url = "https://www.tripadvisor.fr/Restaurant_Review-g8458929-d8680946-Reviews-La_Ferme_de_Lucien-Sallenoves_Haute_Savoie_Auvergne_Rhone_Alpes.html#REVIEWS"


getNbPages(url)


