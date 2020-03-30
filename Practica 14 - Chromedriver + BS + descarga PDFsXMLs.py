import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



################################################
##FUNCION FECHA-SECCION DEL REGISTRO MERCANTIL##
################################################

#Funcion que nos lleva a la url del boletin del registro mercantil para una fecha y seccion determinada:

def Boletin_Registro_Mercantil(fecha, driver, seccion):
    # Cargamos el url del boe y lanzamos el chromedriver
    url = "https://www.boe.es/diario_borme/"
    driver.get(url)
    time.sleep(2)

    #Buscamos el input de la fecha
    fecha_input = driver.find_element_by_id("fechaBORME")
    #Ponemos la fecha
    fecha_input.send_keys(fecha)

    #Hacemos click en buscar
    buscar_boton = driver.find_element_by_name("acc")
    buscar_boton.click()
    time.sleep(2)

    #Chequeamos que la fecha es correcta y no un fin de semana
    try:
        error = driver.find_element_by_xpath("//p[@class='caja gris error']").text
        if error == "No está disponible en este momento el sumario del boletín solicitado.":
            print("La fecha no puede ser un fin de semana, pruebe con otra")
            #Imprimimos un error si la fecha no es correcta
    except:
        pass


    #Abrimos el dropdown
    dropdown = driver.find_element_by_xpath("//div[@class='dropdown']")
    dropdown.click()
    time.sleep(2)

    #Extraemos el link de la Seccion determinada
    link = dropdown.find_element_by_partial_link_text(seccion.upper())
    return link.get_attribute("href")


#Parametros
driver = webdriver.Chrome("../data_sets_y_exe/chromedriver.exe")
fecha = "11192019"
seccion = "segunda"

#Lanzamos la funcion
url = Boletin_Registro_Mercantil(fecha, driver, seccion)



###################################################################
##EXTRACCION DE LAS WEBS QUE CONTIENEN LOS LINKS DE LOS ARCHIVOS###
###################################################################

#Parseamos la web del boletin del registro mercantil para la fecha y seccion determinada con BS
response = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(response.content, "html.parser")

#Locate useful info
target = soup.find("div", class_ = "sumario")
urls = target.find_all("a")

#Get the links of "Otros formatos" where both the pdf and thw xml are contained
links = ["https://www.boe.es" + url["href"] for url in urls if url.get_text() == "Otros formatos"]



#########################
##DESCARGA DE PDF Y XML##
#########################

names = []
XMLs = []
PDFs = []

#Parseamos cada link de "Otros formatos" para extraer la url del PDF y el XML
for link in links:
    response = requests.get(link)
    time.sleep(2)
    soup = BeautifulSoup(response.content, "html.parser")

    # Get title
    container = soup.find("div", id = "barraSep")
    title = container.find("h3", class_ ="documento-tit").get_text()
    #Cogemos solo el nombre principal de la compania (antes de la primera coma)
    title = title.split(',')[0]
    if title in names:
        title = title + "(2)" #por si el nombre esta duplicado
    names.append(title)

    #Get PDF y XML links
    urls = soup.find_all("a")
    for url in urls:
        if url.get_text() == "XML":
            XMLs.append("https://www.boe.es" + url["href"])
        if url.get_text() == "PDF":
            PDFs.append("https://www.boe.es" + url["href"])



###################################
##GUARDAMOS LOS ARCHIVOS EN LOCAL##
###################################

#Guardamos los xmls en el local
for xml, name in zip(XMLs,names):
    r = requests.get(xml)
    with open("archivos_generados/borme/XMLs/" + name + ".xml", "wb") as f:
        f.write(r.content)
#Guardamos los pdfs en el local
for pdf, name in zip(PDFs,names):
    r = requests.get(pdf)
    with open("archivos_generados/borme/PDFs/" + name + ".pdf", "wb") as f:
        f.write(r.content)



