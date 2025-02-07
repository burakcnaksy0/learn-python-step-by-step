import csv

data = [['Ad', 'Soyad', 'Yas'],
        ['Ahmet', 'Yilmaz', 25],
        ['Ayse', 'Kara', 30]]

with open('dosya.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)