import csv
import os
import sys

from decimal import Decimal
from dotenv import load_dotenv
from re import sub

load_dotenv()

if len(sys.argv) < 2:
    sys.exit('Must enter the csv filename as first argument')

csv_filename = sys.argv[1]

with open(csv_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    with open('roundpoint_results.csv', 'w', newline='') as outfile:
        parse = lambda s : Decimal(sub(r'[^\d\-.]', '', s))

        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Payee', 'Memo', 'Amount'])
        for row in reader:
            # skip invalid rows or anything on init date
            if not row['Effective Date'] or row['Effective Date'] == os.getenv('ROUNDPOINT_INIT_DATE'):
                continue

            writer.writerow([row['Effective Date'], row['Description'], 'Amount Paid', parse(row['Amount Paid'])])
            if row['Interest']:
                interest = parse(row['Interest'])
                writer.writerow([row['Effective Date'], 'Interest', 'Interest Payment', -interest])
            if row['Escrow']:
                escrow = parse(row['Escrow'])
                writer.writerow([row['Effective Date'], 'Escrow', 'Escrow Payment', -escrow])
