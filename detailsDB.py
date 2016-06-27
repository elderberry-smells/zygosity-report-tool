import csv, sqlite3

con = sqlite3.connect('zygodb.sqlite')
con.text_factory = str
cur = con.cursor()

cur.execute('CREATE TABLE Details (qcid TEXT UNIQUE PRIMARY KEY, batch TEXT, inspection TEXT, details TEXT, plant TEXT, material TEXT, recieved DATE, reported DATE)')

with open('sharepoint.csv','rb') as share:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(share) # comma is default delimiter
    to_db = [(i['QC_ID'], i['Batch'], i['Inspection Lot'], i['Inspection Object'], i['Plant'], i['Material'], i['Date Recieved'], i['Date Data Return']) for i in dr]

cur.executemany("INSERT OR IGNORE INTO Details (qcid, batch, inspection, details, plant, material, recieved, reported) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
