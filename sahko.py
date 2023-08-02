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
        row = 0

        for value in csv_reader:
            dict_return = {}
            if row == 0:
                row += 1 # skip first row
            else:
                dict_return[value[0]] = value[1]
                list_return.append(dict_return)

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
    row = 1
    print('\n### Sähkönkulutus kuukausitasolla')
    print('\n\tMonth\tkWh')
    for value in usage_list:
        for key, val in value.items():
            print(f'#{row}\t{key}\t{val}')
        row += 1

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
            pass
            '''
            Create feature here where you can add data to data.csv file via program
            '''
        elif valinta == 3:
            draw_graph(usage_list)
        elif valinta == 4:
            sys.exit(0)

if __name__ == "__main__":
    main()
