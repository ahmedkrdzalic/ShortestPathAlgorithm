import csv

list_names = ["name", "ahmed", "sara", "amer", "jusuf"]
list_surnames = ["surname", "krdzalic", "sivic", "heldic", "koric"]

f = open("simple_data.csv", "a", newline="")

for i in range(len(list_surnames)):
    pairs = (list_names[i], list_surnames[i])
    writer = csv.writer(f)
    writer.writerow(pairs)

f.close()