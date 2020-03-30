##################################
### PRACTICA 9 - PARTE 2 #########
##################################
#CSV con links de Universidades de Alemania

## FUNCTIONS-----------------------------------------------------------------
# CSV to List of Lists
import csv
def load_csv(file_path):
    with open(file_path, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ";")
        matrix = [row for row in reader]
    return matrix

#List of Lists to CSV
def print_csv(matrix, file_path):
    with open(file_path, "w", newline="") as output_file:
        writer = csv.writer(output_file, delimiter = ";")
        for row in matrix:
            writer.writerow(row)
##------------------------------------------------------------------------------------------------------------------

#Load the CSV with the universities links per Country
file_path = "archivos_generados/countries.csv"
country_matrix = load_csv(file_path)

#Locate Germany
for country in country_matrix:
    if "Germany" in country[0]:
        Germany_wiki_link = country[1]

import time
import requests
from bs4 import BeautifulSoup

#Load HTML of German Universities into soup
url = Germany_wiki_link
response = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(response.content, "html.parser")

#Locate useful info
targets = soup.find_all("a")
href = []
titles = []
for target in targets:
    try:
        title = (target["title"])
        if 'University' in title and title not in titles:
            titles.append(title)
            href.append(target["href"])
    except:
        pass


#Create the matrix
universities = []
for title, h in zip(titles, href):
    university = ["Germany", Germany_wiki_link, title, h]
    universities.append(university)


#Generate the CSV
file_path = "archivos_generados/universities2.csv"
print_csv(universities, file_path)





# LO HICE COGIENDO SOLO TABLA!!-USEFUL STUFF THO

# #Find the table with info of the German Universities
# target_table = soup.find_all("table", class_ = "wikitable sortable")
# target_table = target_table[0]
#
# #Locate useful info inside the table
# targets = target_table.find_all("a")
#
# #Extract the urls and titles (algunas "a" no tienen "href" de ahi el try)
# href = []
# titles =  []
# try:
#     for target in targets:
#         if "University" in target["href"]:
#             href.append(target["href"])
#             titles.append(target["title"])
# except:
#     pass


##SU FORMA DE COGER LOS LINKS Y TITULOS!!
#def grab_universities(url):

    #response = requests.get(url)
    #time.sleep(2)
    #soup = BeautifulSoup(response.content, "html.parser")

    #collected_links, university_list = [], []
    #links = soup.find_all("a")
    #for link in links:
        #try:
            #if link["title"].startswith("University of") and link["href"] not in collected_links: ##Aqui es donde puede romper en un futuro
                #collected_links.append(link["href")
                #university = [link.get_text(), link["href"]]
                #university_list.append(university)
        #except: pass
    #return university_list

