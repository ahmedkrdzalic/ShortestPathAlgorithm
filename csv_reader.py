import csv

with open('cityName.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        print(line['Name'])