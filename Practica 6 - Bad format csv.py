import csv

def load_csv(path):
    with open(path, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ";")
        matrix = [row for row in reader]
    return matrix

load_path = "data_sets/bad_format.csv"
matrix = load_csv(load_path)

print(matrix)

##falta hacer la media
