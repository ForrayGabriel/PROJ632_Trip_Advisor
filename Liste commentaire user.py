import requests #requests is use to get an URL
from bs4 import BeautifulSoup


def liste_Com_User(username): #we need the username of the user, the goal is to print a list of all his comments
    

    com =[]
    comF = []
    listeCom = []
    
    reqUti = requests.get('https://www.tripadvisor.fr/Profile/'+username) #we get the profile URL for an user
        
    if reqUti.status_code == 404: #if the page doesn't exist
        
        print('Utilisateur introuvable')
        return 0
        
    soupUti = BeautifulSoup(reqUti.text, "lxml")
    
    for a in soupUti.find(id='content')("a"): #we search in the div "content" every link for the reviews
            
        urlCom = a.get('href')
        if 'ShowUserReviews' in str(urlCom):
            com.append(urlCom) #we add them in a list
            
    unSurDeux = True
    
    for i in com: #every links are present two times in the list
        
        if unSurDeux:
            
            comF.append(i) #we add to a new list, one in two of the URL
        
        unSurDeux = not unSurDeux 
            
    
    for i in range(len(comF)):
        
        reqCom = requests.get('https://www.tripadvisor.fr/'+comF[i]) #we reach these URLs
        soupCom = BeautifulSoup(reqCom.text, "lxml")
    
        #Contenu des commentaires
    
        for p in soupCom.find("div", {"class": "entry"})('p'):
        
            listeCom.append(p.text) #add the comment's text in a list
            
    return listeCom


#main

print(liste_Com_User('fabrice163'))












"""
reqUti = requests.get('https://www.tripadvisor.fr/Profile/fabrice163')
soupUti = BeautifulSoup(reqUti.text, "lxml")

#print(soup.title)
# <title>Python (programming language) - Wikipedia</title>
 
soupUti.title.name
# 'title'
 
#print(soup.title.string)
# 'Python (programming language) - Wikipedia'

com =[]
    
for a in soupUti.find(id='content')("a"):
        
    urlCom = a.get('href')
    if 'ShowUserReviews' in str(urlCom):
        com.append(urlCom)
        #print(urlCom)
        
comF = []
fini = True

for i in com:
    
    if fini:
        
        comF.append(i)
    
    fini = not fini 
    
#print(comF)
        

for i in range(len(comF)):
    
    reqCom = requests.get('https://www.tripadvisor.fr/'+comF[i])
    soupCom = BeautifulSoup(reqCom.text, "lxml")

    #Contenu des commentaires

    for p in soupCom.find("div", {"class": "entry"})('p'):
    
        print(p.text)
        print('\n\n')

    #print(soupCom.find(id='content'))
"""
