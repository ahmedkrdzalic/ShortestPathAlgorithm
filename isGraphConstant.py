import csv

with open('cityName.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    current = 0
    counter = 0
    for line in csv_reader:
        if (current != int(line['City_ID'])):
            current = int(line['City_ID'])
            counter += 1
            if counter != current:
                print("Not constant" + " " + str(counter) + " " + str(current))
                counter = current