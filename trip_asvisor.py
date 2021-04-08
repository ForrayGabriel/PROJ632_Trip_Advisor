from bs4 import BeautifulSoup
import urllib.request as urllib2



def traitement(str):
	for i in range(6,len(str)):
		if str[i] == "<":
			return str[5:i]


def search(url):

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content, features="html.parser")

	infos = []

	for review in soup.find_all("div","review-container",):
		rew = str(review)
		usr = rew.split('<div class="info_text pointer_cursor" onclick="widgetEvCall(\'handlers.usernameClick\', event, this);">')
		com = rew.split('<p class="partial_en')
		infos.append([traitement(usr[1]),traitement(com[1])])

	return infos

def getUrls(url, nbPages):
	res = []
	for i in range(len(url)):
		if url[i:i+8] == "Reviews-":
			part1 = url[:i+8]
			part2 = url[i+8:]
			

	for i in range(nbPages):
		res.append(part1+"or"+str(i)+"0-"+part2)
	return res


def getNbPages(url):

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content, features="html.parser")

	res = str(soup).split("avis")

	return int(res[1][-3:])//10+1
	
def getUsernames(url):
	usernames = []
	urls = getUrls(url, getNbPages(url))
	for url in urls:
		names = search(url)
		for name in names:
			usernames.append([name[0], name[1]])
	return usernames


url = "https://www.tripadvisor.fr/Restaurant_Review-g8458929-d8680946-Reviews-La_Ferme_de_Lucien-Sallenoves_Haute_Savoie_Auvergne_Rhone_Alpes.html#REVIEWS"
url2 = "https://www.tripadvisor.fr/Restaurant_Review-g8017085-d7852031-Reviews-Les_3_Bouchons-Chavannes_sur_Suran_Ain_Auvergne_Rhone_Alpes.html"
