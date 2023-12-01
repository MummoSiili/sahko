'''
Sähkön hinta
'''

import sys, csv
import pymongo

# Read 'data.csv' file and return a list
def read_csv_file():

    list_return = []

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            list_return.append(row)
        return list_return

def print_csv_file(usage_list):
    row = 0
    print('\n### Sähkönkulutus kuukausitasolla')
    print('\n\tMonth\tkWh')
    for value in usage_list:
        if row == 0:
            row += 1
        else:
            print(f'#{row}\t{value[0]}\t{value[1]}')
            row += 1

def add_data(usage_list):
    month = input("Anna kuukausi muodossa 'MM-YYYY' esim. '01-2012': ")
    kwh = input("Anna sähkönkulutus muodossa 'xxx.xx' esim. '123.57': ")
    buffer = [month, kwh]
    usage_list.append(buffer)

def write_csv_to_file(usage_list):
    with open('data.csv', 'w') as file:
        writer_obj = csv.writer(file, delimiter=';')

        for row in usage_list:
            writer_obj.writerow(row)

    print('data saved!')

def add_to_db(usage_list, db_collection):
    # delete existing db first to insert new one from csv
    db_collection.delete_many({})

    # create new db from csv
    db_list = []
    id = 1
    for i in range(1, len(usage_list)):
        db_list.append({'_id': id, 'month': usage_list[i][0], 'consumption': usage_list[i][1], 'price': usage_list[i][2]})
        id += 1

    db_collection.insert_many(db_list)

def main():

    # create and use db
    db_client = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = db_client['power_db'] # define db
    db_collection = mydb['month'] # collection

    # Run until 'Lopeta'
    while True:
        print('''
(1) Tuo CSV data (data.csv)
(2) Lisää data
(4) Lopeta

Mitä haluat tehdä? ''', end='')

        valinta = int(input())

        if valinta == 1:
            usage_list = read_csv_file()
            add_to_db(usage_list, db_collection)
        elif valinta == 2:
            add_data(usage_list)
        elif valinta == 3:
            print_csv_file(usage_list)
        elif valinta == 4:
            write_csv_to_file(usage_list)
            sys.exit(0)

if __name__ == "__main__":
    main()
