



import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver = webdriver.Chrome("data_sets_y_exe/chromedriver.exe")

#Cargamos el url y lanzamos el chromedriver
url = "https://comparadorofertasenergia.cnmc.es/comparador/index.cfm"
driver.get(url)
time.sleep(2)

def select_supply(supply_type):
    supply =  driver.find_element_by_id(supply_type)
    supply.click()
    boton_iniciar = driver.find_element_by_id("iniciar")
    boton_iniciar.click()

select_supply("electricidad")

##################################
# #Click en electricidad
# boton_electricidad = driver.find_element_by_id("electricidad")
# boton_electricidad.click()
#
# #Click en inicar
# boton_iniciar = driver.find_element_by_id("iniciar")
# boton_iniciar.click()
# time.sleep(2)
#####################################

#Rellenamos el formulario
input_zip = driver.find_element_by_id("cp")
postal_code = "28028"
input_zip.send_keys(postal_code)

boton_adicionales_no = driver.find_element_by_id("san")
boton_adicionales_no.click()

boton_seguir = driver.find_element_by_id("seguir")
boton_seguir.click()
time.sleep(2)

url = driver.current_url
print(url)





