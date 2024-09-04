import csv
with open('names.csv','r' ) as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('New_csv.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")
        
        for name in csv_reader:
            csv_writer.writerow(name)

with open('New_csv.csv', 'r') as files:
    noms = csv.reader(files)
    for nom in noms:
        print(nom)