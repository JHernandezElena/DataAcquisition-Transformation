import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("data_sets_y_exe/chromedriver.exe")

#Cargamos el url y lanzamos el chromedriver
url = "https://comparadorofertasenergia.cnmc.es/comparador/resultados_ficha.cfm?id=2516&cad=0000000045122802803.3000030000003.3000000000000030000000000000000000000010N2100&tipof=1"
driver.get(url)
time.sleep(4)

# key = driver.find_element_by_xpath("//td[@align='left']")
# value = key.find_element_by_xpath("/following-sibling::td")
# key.text
# value.text
#
# #o
# keys = driver.find_elements_by_xpath("//td[@align='left']")
# keys2 = []
# values = []
# for key in keys:
#     value = key.find_element_by_xpath("/following-sibling::td")
#     key.text.append(keys2)
#     value.text.append(values)




