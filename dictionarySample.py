import csv


with open('cityName.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    dictOfCities = {}
    for city in csv_reader:
        dictOfCities[city['Name']] = city['City_ID']

    print(dictOfCities['Jajce'] + '  ' + str(len(dictOfCities)))
