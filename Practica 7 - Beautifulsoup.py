import requests
from bs4 import BeautifulSoup

#Load HTML into soup
url = "https://en.wikipedia.org/wiki/Comillas_Pontifical_University"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#Locate target table with useful info
target_tables = soup.find_all("table", class_="infobox vcard")
#print(len(target_tables)) #hacemos find_all y print length para ver si solo hay una tabla con este nombre
target_tables = target_tables[0] ##find_all devuelve un array de elementos en este caso con un solo elemento

#URL del seal
seal = target_tables.find("a")["href"]
print("Seal: https://en.wikipedia.org/" + seal)

#Motto en latin
motto_latin = target_tables.find("td", class_ ="nickname")
print("Motto_latin: " + motto_latin.get_text())

#Extraemos los headers
headers_list = target_tables.find_all("th", style="padding-right:0.65em;")
headers=[]
for i in headers_list:
    headers.append(i.get_text())

#Extraemos los textos asociados a los headers
textos=[]
for i in range(3,len(headers)+3):
    textos.append(target_tables.find_all("td")[i].get_text())

#Hacemos un print de header y texto
for header, texto in zip(headers, textos):
    print(header + ": " + texto)

#URL del logo
logo = target_tables.find("a", class_="image")["href"]
print("Logo: https://en.wikipedia.org/" + logo)

#Creo un diccionario para tenerlo
Diccionario = dict(zip(headers,textos))
Diccionario["logo"] = logo
Diccionario["seal"] = seal
Diccionario["motto_latin"] = motto_latin.get_text()


import json
def print_json(dic, file_path):
    with open(file_path, "w") as output_file:
        json.dump(dic, output_file)


print_json(Diccionario, "archivos_generados/comillas_wiki.json" )




















