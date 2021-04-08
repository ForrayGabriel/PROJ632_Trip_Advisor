import requests
from bs4 import BeautifulSoup


def liste_Com_User(username):
    

    com =[]
    comF = []
    listeCom = []
    
    reqUti = requests.get('https://www.tripadvisor.fr/Profile/'+username)
        
    if reqUti.status_code == 404:
        
        print('Utilisateur introuvable')
        return 0
        
    soupUti = BeautifulSoup(reqUti.text, "lxml")
    
    for a in soupUti.find(id='content')("a"):
            
        urlCom = a.get('href')
        if 'ShowUserReviews' in str(urlCom):
            com.append(urlCom)
            
    comF = []
    unSurDeux = True
    
    for i in com:
        
        if unSurDeux:
            
            comF.append(i)
        
        unSurDeux = not unSurDeux 
        
    #print(comF)
            
    
    for i in range(len(comF)):
        
        reqCom = requests.get('https://www.tripadvisor.fr/'+comF[i])
        soupCom = BeautifulSoup(reqCom.text, "lxml")
    
        #Contenu des commentaires
    
        for p in soupCom.find("div", {"class": "entry"})('p'):
        
            listeCom.append(p.text)
            
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