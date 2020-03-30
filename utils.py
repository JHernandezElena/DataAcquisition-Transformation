#Utils.py

#Dictionary to JSON
def printdic_json(dic, file_path):
    import json
    with open(file_path, "w") as output_file:
        json.dump(dic, output_file)

#Dictionary to CSV
def printdic_CSV(dictionary, file_path):
    with open(file_path, 'w') as f:
        for key in dictionary.keys():
            f.write("%s;%s\n"%(key,dictionary[key]))

#CSV to List of Lists
def load_csv(file_path):
    import csv
    with open(file_path, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ";")
        matrix = [row for row in reader]
    return matrix

#List of Lists to CSV
def print_csv(matrix, file_path):
    import csv
    with open(file_path, "w", newline="") as output_file:
        writer = csv.writer(output_file, delimiter = ";")
        for row in matrix:
            writer.writerow(row)