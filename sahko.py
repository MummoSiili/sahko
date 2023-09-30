'''
Sähkön hinta
'''

import sys, csv
import matplotlib.pyplot as plt

# Read 'data.csv' file and return a list
def read_csv_file():

    list_return = []

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            list_return.append(row)
        return list_return

# Draw graph
def draw_graph(usage_list):
    x = []
    y = []
    for i in usage_list:
        for month, kwh in i.items():
            x.append(month)
            y.append(float(kwh))

    plt.plot(x, y, color='green', linestyle='dashed', marker='o', \
    markerfacecolor='blue', markersize=6)
    plt.xlabel('Kuukausi')
    plt.ylabel('kWh')
    plt.title('Sähkönkulutus')
    plt.show()

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
    kwh = input("Anna sähkönkulutus muodoss 'xxx.xx' esim. '123.57': ")
    buffer_dict = {month : kwh}
    usage_list.append(buffer_dict)


def main():

    # Test if data.csv exists
    try:
        usage_list = read_csv_file()
    except Exception as e:
        print("Tiedosto 'data.csv' ei ole olemassa")
        sys.exit(0)

    # Run until 'Lopeta'
    while True:
        print('''
(1) Lue CSV data
(2) Lisää data
(3) Piirrä data
(4) Lopeta

Mitä haluat tehdä? ''', end='')

        valinta = int(input())

        if valinta == 1:
            print_csv_file(usage_list)
        elif valinta == 2:
            add_data(usage_list)
        elif valinta == 3:
            draw_graph(usage_list)
        elif valinta == 4:
            '''
            Write code that saves currenct usage list back to CSV file
            '''
            sys.exit(0)

if __name__ == "__main__":
    main()
