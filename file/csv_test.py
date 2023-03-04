import csv

# csvファイル書き込み
with open('file/csv_test.csv', 'w') as f:
    header = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerow({'name': 'Taro', 'age': 20})
    writer.writerow({'name': 'Hanako', 'age': 18})

# csvファイル読み込み
with open('file/csv_test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
