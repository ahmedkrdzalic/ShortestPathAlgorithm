import csv

numOfRows = None
adjMTX = None
# with open('sampleFromTo.csv', 'r', encoding='utf8') as file:
#     numOfRows = sum(1 for row in file)
#     adjMTX = [[0] * (numOfRows-1) for i in range(numOfRows-1)]

#1174 is the number of cities
adjMTX = [[0] * (6) for i in range(6)]

with open('sampleFromTo.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    current = None
    for line in csv_reader:
        if (current != line['from_ID']):
            current = line['from_ID']
        #TODO: kad nije nijedan edge poceo sa nekim brojem
        valFrom = int(line['from_ID'])
        valTo = int(line['to_ID'])

        try:
            adjMTX[valFrom-1][valTo-1] = 1
            adjMTX[valTo - 1][valFrom - 1] = 1
        except:
            continue

        # print(str(valFrom) + " - " + str(valTo))

for row in adjMTX:
    print(row)