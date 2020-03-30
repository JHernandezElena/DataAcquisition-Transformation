###################################
### PRACTICA 10 - SCRAPER #########
###################################
#Grab established year from a list of links

import time
import requests
from bs4 import BeautifulSoup

# CSV to List of Lists
import csv
def load_csv(file_path):
    with open(file_path, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ";")
        matrix = [row for row in reader]
    return matrix

#Load the CSV with the universities of Germany
file_path = "archivos_generados/universities2.csv"
German_universities = load_csv(file_path)

def grab_established_year(url):
    response = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        target_tables = soup.find_all("table", class_="infobox vcard")
        target_table = target_tables[0]

        couples = target_table.find_all("tr")
        for couple in couples:
            header = couple.find("th")
            try:
                if header.get_text() == "Established":
                    year = couple.find("td").get_text()
                    return year
            except:
                pass
    except:
        pass


#Loop to get establish year per university and generate the matrix university-year
universities_year = []
for university in German_universities:
    year = grab_established_year("http://en.wikipedia.org" + university[3])
    university_year = [university[2], year]
    if university_year not in universities_year and year != "":
        universities_year.append(university_year)


#List of Lists to CSV
def print_csv(matrix, file_path):
    with open(file_path, "w", newline="") as output_file:
        writer = csv.writer(output_file, delimiter = ";")
        for row in matrix:
            writer.writerow(row)

file_path = "archivos_generados/establishment2.csv"
print_csv(universities_year, file_path)
