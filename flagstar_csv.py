import csv

with open('export.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    with open('result.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Payee', 'Memo', 'Amount'])
        for row in reader:
            writer.writerow([row['Date'], row['Description'], 'Total Amount', row['Total Amount']])
            if row['Payment Interest']:
                writer.writerow([row['Date'], 'Interest', 'Interest Payment', -float(row['Payment Interest'])])
            if row['Payment Escrow']:
                writer.writerow([row['Date'], 'Escrow', 'Escrow Payment', -float(row['Payment Escrow'])])
