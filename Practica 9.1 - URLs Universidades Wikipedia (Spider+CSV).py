##################################
### PRACTICA 9 - PARTE 1 #########
##################################
#CSV con link de Universidades por pais

import time
import requests
from bs4 import BeautifulSoup

#Load HTML into soup
url = "https://en.wikipedia.org/wiki/Lists_of_universities_and_colleges_by_country"
response = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(response.content, "html.parser")

#Locate useful info
targets = soup.find_all("a")

#Extract the urls (algunas "a" no tienen "href" entre ellas la primera de ahi el try)
href = []
try:
    for i in range(1, len(targets)):
        href.append(targets[i]["href"])
except:
    pass

#De todos los links cogemos aquellos de las universidades de cada pais mediante un filter
countries_links = []
for line in href:
    if '/wiki/List' in line and line not in countries_links:
        countries_links.append(line)


#Con una regex extraemos los nombres de cada link
import re
countries_names = []
for link in countries_links:
    name = re.findall(r'^(?:[^_]+_){4}([^_].*)',link) #nos da una lista
    countries_names.append(name)
#Conver la lista de listas a una lista de strings
countries_names =[i[0] if len(i)!=0 else "" for i in countries_names ]


#Creamos una lista name-link, eliminando los 18 ultimas entradas ya que no son los que nos interesan
lista = list(zip(countries_names,countries_links))[:-18]

#Creamos un diccionario a partir de las entradas no vacias de la lista
dictionary={}
for name,link in lista:
    if len(name)!=0:
        dictionary[name]= "https://en.wikipedia.org" + link

#Creamos el CSV a partir del diccionario
with open('archivos_generados/countries.csv', 'w') as f:
    for key in dictionary.keys():
        f.write("%s;%s\n"%(key,dictionary[key]))



##SU FORMA DE COGER LOS LINKS Y TITULOS!!
#def grab_countries(url):

    #response = requests.get(url)
    #time.sleep(2)
    #soup = BeautifulSoup(response.content, "html.parser")

    #country_list = []
    #links = soup.find_all("a")
    #for link in links:
        #try:
            #if link["title"].startswith("List of universities"): ##Aqui es donde puede romper en un futuro
                #country = [link.get_text(), link["href"]}
                #country_list.append(country)
        #except: pass
    #return country_list








