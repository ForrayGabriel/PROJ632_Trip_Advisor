from bs4 import BeautifulSoup
import urllib.request as urllib2


# Function that find and extract an user name or a commentary by searching the end of the html beacon
def traitement(text):
    for i in range(6, len(text)):
        if text[i] == "<":
            return text[5:i]


# Function that takes an url and return a list of user with their review
def search(url):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content, features="html.parser")

    infos = []

    for review in soup.find_all("div", "review-container", ):
        rew = str(review)
        usr = rew.split(
            '<div class="info_text pointer_cursor" onclick="widgetEvCall(\'handlers.usernameClick\', event, this);">')
        com = rew.split('<p class="partial_en')
        infos.append([traitement(usr[1]), traitement(com[1])])

    return infos


# Function that takes the url of a restaurant and return a list of all the reviews pages urls
# based on the number of pages
def getUrls(url, nbPages):
    res = []
    for i in range(len(url)):
        if url[i:i + 8] == "Reviews-":
            part1 = url[:i + 8]
            part2 = url[i + 8:]

    for i in range(nbPages):
        res.append(part1 + "or" + str(i) + "0-" + part2)
    return res


# Function that takes an url and return the number of pages of reviews based on the number of reviews
def getNbPages(url):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content, features="html.parser")

    res = str(soup).split("avis")

    return int(res[1][-3:]) // 10 + 1


# Function that takes an url and search for usernames and reviews for all the reviews pages
def getUsernames(url):
    usernames = []
    urls = getUrls(url, getNbPages(url))
    for url in urls:
        names = search(url)
        for name in names:
            usernames.append([name[0], name[1]])
    return usernames
