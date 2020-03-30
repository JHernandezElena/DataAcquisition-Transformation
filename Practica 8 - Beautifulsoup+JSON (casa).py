import requests
from bs4 import BeautifulSoup

#Load HTML into soup
url = "https://en.wikipedia.org/wiki/World_population"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#Locate target table with useful info
target_table = soup.find_all("table", class_ = "wikitable sortable")
print(len(target_table)) #hacemos find_all y print length para ver si solo hay una tabla con este nombre
target_table = target_table[0]
#print(target_table) #comprobamos que esta es la tabla que queremos "Population by continent (2016 estimates)"


#Cogemos los datos de la tabla que nos intersan
continent_list = target_table.find_all("tr")

#Extraemos los headers de la tabla
headers_tag=continent_list[0]
headers_text = headers_tag.get_text()
headers_list = headers_text.split('\n')
headers = []
for p in range(3, len(headers_list), 2):
    headers.append(headers_list[p])

#CREAMOS EL DICCIONATIO (KEYS=CONTINENTE, VALUES=SUB-DICCIONARIO CON LA INFO DEL CONTINENTE)
keys=[]
values =  []

for i in range(1, len(continent_list)):
    x = continent_list[i].get_text() #cogemos el texto dentro de cada linea de continente
    y = x.split('\n') #dividimos la info
    keys.append(y[1]) #añadimos el país a la lista de keys de nuestro diccionario

    #extraemos la informacion de cada continente
    continent_info = []
    for j in range (3, len(y),2):
        continent_info.append(y[j])
    sub_dic = dict(zip(headers, continent_info)) #creamos el subdiccionario con los valores de cada continente
    values.append(sub_dic)

#Juntamos keys con values
Diccionario = dict(zip(keys,values))
print(Diccionario)


#Creamos el json
import json
def print_json(dic, file_path):
    with open(file_path, "w") as output_file:
        json.dump(dic, output_file)


print_json(Diccionario, "archivos_generados/continentes_wiki.json" )


