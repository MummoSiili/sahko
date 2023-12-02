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

def add_data(db_collection):
    while True:
        print('### Nykyinen tietokannan sisältö')
        read_db(db_collection)
        print('''
    (1) Lisää dataa
    (2) Muokkaa dataa
    (3) Palaa
    Mitä haluat tehdä? ''', end='')

        valinta = int(input())

        if valinta == 1:
            add_entry_to_db(db_collection)
        elif valinta == 2:
            modify_db_entry(db_collection)
        elif valinta == 3:
            break

def add_entry_to_db(db_collection):
   db_size = db_collection.count_documents({})
   id = db_size + 1

   month = input('Anna kuukausi muodossa "KK-VVVV": ')
   consumption = input('Anna kWh kulutus muodossa "xxx.xx": ')
   price = input('Anna laskun summa muodoss "xxx.xx": ')

   db_collection.insert_one({'_id': id, 'month': month, 'consumption': consumption, 'price': price})

def write_csv_to_file(usage_list):
    with open('data.csv', 'w') as file:
        writer_obj = csv.writer(file, delimiter=';')

        for row in usage_list:
            writer_obj.writerow(row)

    print('data saved!')

def modify_db_entry(db_collection):
    read_db_with_id(db_collection)
    id = input('Valitse ID mitä haluat muokata: ')
    query = {"_id": id }

    print('### Valitse uudet arvot:')
    month = input('Anna kuukausi muodossa "KK-VVVV": ')
    consumption = input('Anna kWh kulutus muodossa "xxx.xx": ')
    price = input('Anna laskun summa muodoss "xxx.xx": ')

    new_values = {"$set": {'month': month, 'consumption': consumption, 'price': price}}
    print(f'ID #{id} päivitetty!')

def read_db_with_id(db_collection):
    print('#ID\tMonth\tkWh\t\tCost')
    for x in db_collection.find().sort(('_id')):
        print(f'{x["_id"]}\t{x["month"]}\t{x["consumption"]}\t{x["price"]}')

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

def read_db(db_collection):
    print('\n### Sähkönkulutus kuukausitasolla')
    print('\n\tMonth\tkWh\t\tCost')
    for x in db_collection.find().sort(('_id')):
        print(f'\t{x["month"]}\t{x["consumption"]}\t{x["price"]}')

def main():

    # create and use db
    db_client = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = db_client['power_db'] # define db
    db_collection = mydb['month'] # collection

    # Run until 'Lopeta'
    while True:
        print('''
(1) Tuo CSV data (data.csv) - Tämä pyyhkii tietokannan ja importtaa kaiken .csv -tiedostosta
(2) Lisää dataa
(3) Lue tietokanta
(4) Lopeta

Mitä haluat tehdä? ''', end='')

        valinta = int(input())

        if valinta == 1:
            usage_list = read_csv_file()
            add_to_db(usage_list, db_collection)
        elif valinta == 2:
            add_data(db_collection)
        elif valinta == 3:
            read_db(db_collection)
        elif valinta == 4:
            sys.exit(0)

if __name__ == "__main__":
    main()
