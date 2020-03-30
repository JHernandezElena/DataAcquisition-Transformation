import time
import requests
from bs4 import BeautifulSoup

#Load HTML into soup
#url de la practica 12a
url = "https://comparadorofertasenergia.cnmc.es/comparador/res.cfm?cad=0000000045122802803.3000030000003.3000000000000030000000000000000000000010N2100&CFID=5739&CFTOKEN=10106398"
response = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(response.content, "html.parser")

#Locate useful info
targets = soup.find_all("td", class_ = "ver")
# urls= []
# for target in targets:
#     urls.append(target.find("a")["href"])

urls = ["https://comparadorofertasenergia.cnmc.es/comparador/" + target.find("a")["href"] for target in targets]
print(urls)




