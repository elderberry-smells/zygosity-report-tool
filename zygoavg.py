import csv
import os
import sqlite3

finput = raw_input('Input File Name:')
fhand = finput + '.csv'


# make a list of the rows that are not in use, are NTC's or are controls
def remove_wells():
    remove = list()
    ntc_wells = [str(ntc) for ntc in range(1, 3)] + [str("%02d" % ntc) for ntc in range(1, 3)]
    control_wells = [str(cont) for cont in range(7, 13)] + [str("%02d" % cont) for cont in range(7, 13)]

    for well in ntc_wells:
        remove.append('A' + well)
    for well in control_wells:
        remove.append('H' + well)
    return remove


# equation to calculate the % homozygosity of the sample
def homo_avg(zygo_dict):
    homo = float(zygo_dict.get('Homo', 0))
    hemi = float(zygo_dict.get('Hemi', 0))
    null = float(zygo_dict.get('Null', 0))
    total = homo + hemi + null
    if total > 0:
        avg = (homo / total) * 100
        return "%.2f" % avg
    else:
        return 'N/A'


# equation to calculate the % heterozygosity of the sample
def hemi_avg(zygo_dict):
    homo = float(zygo_dict.get('Homo', 0))
    hemi = float(zygo_dict.get('Hemi', 0))
    null = float(zygo_dict.get('Null', 0))
    total = homo + hemi + null
    if total > 0:
        avg = (hemi / total) * 100
        return "%.2f" % avg
    else:
        return 'N/A'


# equation to calculate the % wild type of the sample
def null_avg(zygo_dict):
    homo = float(zygo_dict.get('Homo', 0))
    hemi = float(zygo_dict.get('Hemi', 0))
    null = float(zygo_dict.get('Null', 0))
    total = homo + hemi + null
    if total > 0:
        avg = (null / total) * 100
        return "%.2f" % avg
    else:
        return 'N/A'


# open the csv file, and make a dictionary for each column with zygosity data, counting the homo/hemi/null
with open(fhand) as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames

    f2a_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    f3a_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    f3c_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    rfo_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    cyto_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    gt73_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    pm1_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    pm2_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}
    bar_counts = {'Homo': 0, 'Hemi': 0, 'Null': 0}

    # for each row in the csv file, read each row if the row is not supposed to be removed
    for row in reader:

        if row['Well'] in remove_wells():
            continue
        # if the csv file has the specific header stated below, make the counts of each unique word(homo/hemi/null etc.)
        # and append it to the correct dictionary.
        else:
            if 'FAD 2 Zygosity Call' in headers:
                word = row['FAD 2 Zygosity Call']
                if word != 'Empty':
                    f2a_counts[word] = f2a_counts.get(word, 0) + 1

            if 'FAD 3A Zygosity Call' in headers:
                word = row['FAD 3A Zygosity Call']
                if word != 'Empty':
                    f3a_counts[word] = f3a_counts.get(word, 0) + 1

            if 'FAD 3C Zygosity Call' in headers:
                word = row['FAD 3C Zygosity Call']
                if word != 'Empty':
                    f3c_counts[word] = f3c_counts.get(word, 0) + 1

            if 'RFO Zygosity Call' in headers:
                word = row['RFO Zygosity Call']
                if word != 'Empty':
                    rfo_counts[word] = rfo_counts.get(word, 0) + 1

            if 'Cyto A Zygosity Call' in headers:
                word = row['Cyto A Zygosity Call']
                if word != 'Empty':
                    cyto_counts[word] = cyto_counts.get(word, 0) + 1

            if 'GT73 Zygosity Call' in headers:
                word = row['GT73 Zygosity Call']
                if word != 'Empty':
                    gt73_counts[word] = gt73_counts.get(word, 0) + 1

            if 'PM1 Zygosity Call' in headers:
                word = row['PM1 Zygosity Call']
                if word != 'Empty':
                    pm1_counts[word] = pm1_counts.get(word, 0) + 1

            if 'PM2 Zygosity Call' in headers:
                word = row['PM2 Zygosity Call']
                if word != 'Empty':
                    pm2_counts[word] = pm2_counts.get(word, 0) + 1

            if 'Sask BAR Zygosity Call' in headers:
                word = row['Sask BAR Zygosity Call']
                if word != 'Empty':
                    bar_counts[word] = bar_counts.get(word, 0) + 1

            else:
                continue

# print the totals from the counts
print 'FAD2:', f2a_counts
print 'FAD3A:', f3a_counts
print 'FAD3C:', f3c_counts
print 'RFO:', rfo_counts
print 'CYTO:', cyto_counts
print 'GT73:', gt73_counts
print 'PM1:', pm1_counts
print 'PM2:', pm2_counts
print 'BAR:', bar_counts

f2ahomo = f2a_counts.get('Homo', 0)
f2ahemi = f2a_counts.get('Hemi', 0)
f2anull = f2a_counts.get('Null', 0)
f2acall = f2a_counts.get('No Call', 0)
f2afail = f2a_counts.get('No Data', 0)
f2a_homo_avg = homo_avg(f2a_counts)
f2a_hemi_avg = hemi_avg(f2a_counts)
f2a_null_avg = null_avg(f2a_counts)

f3ahomo = f3a_counts.get('Homo', 0)
f3ahemi = f3a_counts.get('Hemi', 0)
f3anull = f3a_counts.get('Null', 0)
f3acall = f3a_counts.get('No Call', 0)
f3afail = f3a_counts.get('No Data', 0)
f3a_homo_avg = homo_avg(f3a_counts)
f3a_hemi_avg = hemi_avg(f3a_counts)
f3a_null_avg = null_avg(f3a_counts)

f3chomo = f3c_counts.get('Homo', 0)
f3chemi = f3c_counts.get('Hemi', 0)
f3cnull = f3c_counts.get('Null', 0)
f3ccall = f3c_counts.get('No Call', 0)
f3cfail = f3c_counts.get('No Data', 0)
f3c_homo_avg = homo_avg(f3c_counts)
f3c_hemi_avg = hemi_avg(f3c_counts)
f3c_null_avg = null_avg(f3c_counts)

rfohomo = rfo_counts.get('Homo', 0)
rfohemi = rfo_counts.get('Hemi', 0)
rfonull = rfo_counts.get('Null', 0)
rfocall = rfo_counts.get('No Call', 0)
rfofail = rfo_counts.get('No Data', 0)
rfo_homo_avg = homo_avg(rfo_counts)
rfo_hemi_avg = hemi_avg(rfo_counts)
rfo_null_avg = null_avg(rfo_counts)

cytohomo = cyto_counts.get('Homo', 0)
cytonull = cyto_counts.get('Null', 0)
cytocall = cyto_counts.get('No Call', 0)
cytofail = cyto_counts.get('No Data', 0)
acyto = homo_avg(cyto_counts)
bcyto = null_avg(cyto_counts)

gthomo = gt73_counts.get('Homo', 0)
gthemi = gt73_counts.get('Hemi', 0)
gtnull = gt73_counts.get('Null', 0)
gtcall = gt73_counts.get('No Call', 0)
gtfail = gt73_counts.get('No Data', 0)
gt73_homo_avg = homo_avg(gt73_counts)
gt73_hemi_avg = hemi_avg(gt73_counts)
gt73_null_avg = null_avg(gt73_counts)

pm1homo = pm1_counts.get('Homo', 0)
pm1hemi = pm1_counts.get('Hemi', 0)
pm1null = pm1_counts.get('Null', 0)
pm1call = pm1_counts.get('No Call', 0)
pm1fail = pm1_counts.get('No Data', 0)
pm1_homo_avg = homo_avg(pm1_counts)
pm1_hemi_avg = hemi_avg(pm1_counts)
pm1_null_avg = null_avg(pm1_counts)

pm2homo = pm2_counts.get('Homo', 0)
pm2hemi = pm2_counts.get('Hemi', 0)
pm2null = pm2_counts.get('Null', 0)
pm2call = pm2_counts.get('No Call', 0)
pm2fail = pm2_counts.get('No Data', 0)
pm2_homo_avg = homo_avg(pm2_counts)
pm2_hemi_avg = hemi_avg(pm2_counts)
pm2_null_avg = null_avg(pm2_counts)

barhomo = bar_counts.get('Homo', 0)
barhemi = bar_counts.get('Hemi', 0)
barnull = bar_counts.get('Null', 0)
barcall = bar_counts.get('No Call', 0)
barfail = bar_counts.get('No Data', 0)
bar_homo_avg = homo_avg(bar_counts)
bar_hemi_avg = hemi_avg(bar_counts)
bar_null_avg = null_avg(bar_counts)

print 'rfo homo:', rfo_homo_avg
print 'rfo hemi:', rfo_hemi_avg
print 'rfo null:', rfo_null_avg

# upload all the information from the one sample here into the zygo database.

# get the following information into one line, and insert it into the 'raw_data' table

r = open(fhand, 'rb')
qcid = ""
for line in r:
    bits = line.split(',')
    for i in bits:
        if bits[0][:11] in qcid:
            continue
        elif bits[0] == "Box":
            continue
        else:
            qcid += bits[0][:11]

r.close()

print qcid

# write the raw data into the database

# write a temporary file of the homo/hemi/null counts

with open('temp1.csv', 'wb') as csvfile:
    headers = ['qcid', 'rfo_homo', 'rfo_hemi', 'rfo_null', 'f2a_homo', 'f2a_hemi',
               'f2a_null', 'f3a_homo', 'f3a_hemi', 'f3a_null', 'f3c_homo',
               'f3c_hemi', 'f3c_null', 'cyto_homo', 'cyto_null', 'gt73_homo', 'gt73_hemi',
               'gt73_null', 'pm1_homo', 'pm1_hemi', 'pm1_null', 'pm2_homo', 'pm2_hemi',
               'pm2_null', 'bar_homo', 'bar_hemi', 'bar_null']
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
    writer.writeheader()
    writer.writerow(
        {'qcid': qcid, 'rfo_homo': rfohomo, 'rfo_hemi': rfohemi, 'rfo_null': rfonull,
         'f2a_homo': f2ahomo, 'f2a_hemi': f2ahemi, 'f2a_null': f2anull,
         'f3a_homo': f3ahomo, 'f3a_hemi': f3ahemi, 'f3a_null': f3anull,
         'f3c_homo': f3chomo, 'f3c_hemi': f3chemi, 'f3c_null': f3cnull,
         'cyto_homo': cytohomo, 'cyto_null': cytonull,
         'gt73_homo': gthomo, 'gt73_hemi': gthemi, 'gt73_null': gtnull,
         'pm1_homo': pm1homo, 'pm1_hemi': pm1hemi, 'pm1_null': pm1null,
         'pm2_homo': pm2homo, 'pm2_hemi': pm2hemi, 'pm2_null': pm2null,
         'bar_homo': barhomo, 'bar_hemi': barhemi, 'bar_null': barnull})


# write into that file an item for each column
with open('temp1.csv', 'rb') as csv_file:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(csv_file)  # comma is default delimiter
    raw_db = [(i['qcid'], i['rfo_homo'], i['rfo_hemi'], i['rfo_null'], i['f2a_homo'], i['f2a_hemi'], i['f2a_null'], i['f3a_homo'], i['f3a_hemi'], i['f3a_null'], i['f3c_homo'], i['f3c_hemi'], i['f3c_null'], i['cyto_homo'], i['cyto_null'], i['gt73_homo'], i['gt73_hemi'], i['gt73_null'], i['pm1_homo'], i['pm1_hemi'], i['pm1_null'], i['pm2_homo'], i['pm2_hemi'], i['pm2_null'], i['bar_homo'], i['bar_hemi'], i['bar_null']) for i in dr]

con = sqlite3.connect('zygodb.sqlite')
con.text_factory = str
cur = con.cursor()

cur.executemany("INSERT OR REPLACE INTO raw_data (qcid, rfo_homo, rfo_hemi, rfo_null, f2a_homo, f2a_hemi, f2a_null, f3a_homo, f3a_hemi, f3a_null, f3c_homo, f3c_hemi, f3c_null, cyto_homo, cyto_null, gt73_homo, gt73_hemi, gt73_null, pm1_homo, pm1_hemi, pm1_null, pm2_homo, pm2_hemi, pm2_null, bar_homo, bar_hemi, bar_null) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", raw_db)
con.commit()

os.remove('temp1.csv')


# write a temporary csv file for zygosity averages - complete with headers.
with open('temp.csv', 'wb') as csvfile:
    headers = ['qcid', 'rfo_homo_avg', 'rfo_hemi_avg', 'rfo_null_avg', 'f2a_homo_avg', 'f2a_hemi_avg',
               'f2a_null_avg', 'f3a_homo_avg', 'f3a_hemi_avg', 'f3a_null_avg', 'f3c_homo_avg',
               'f3c_hemi_avg', 'f3c_null_avg', 'acyto', 'bcyto', 'gt73_homo_avg', 'gt73_hemi_avg',
               'gt73_null_avg', 'pm1_homo_avg', 'pm1_hemi_avg', 'pm1_null_avg', 'pm2_homo_avg', 'pm2_hemi_avg',
               'pm2_null_avg', 'bar_homo_avg', 'bar_hemi_avg', 'bar_null_avg']
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
    writer.writeheader()
    writer.writerow(
        {'qcid': qcid, 'rfo_homo_avg': rfo_homo_avg, 'rfo_hemi_avg': rfo_hemi_avg, 'rfo_null_avg': rfo_null_avg,
         'f2a_homo_avg': f2a_homo_avg, 'f2a_hemi_avg': f2a_hemi_avg, 'f2a_null_avg': f2a_null_avg,
         'f3a_homo_avg': f3a_homo_avg, 'f3a_hemi_avg': f3a_hemi_avg, 'f3a_null_avg': f3a_null_avg,
         'f3c_homo_avg': f3c_homo_avg, 'f3c_hemi_avg': f3c_hemi_avg, 'f3c_null_avg': f3c_null_avg,
         'acyto': acyto, 'bcyto': bcyto,
         'gt73_homo_avg': gt73_homo_avg, 'gt73_hemi_avg': gt73_hemi_avg, 'gt73_null_avg': gt73_null_avg,
         'pm1_homo_avg': pm1_homo_avg, 'pm1_hemi_avg': pm1_hemi_avg, 'pm1_null_avg': pm1_null_avg,
         'pm2_homo_avg': pm2_homo_avg, 'pm2_hemi_avg': pm2_hemi_avg, 'pm2_null_avg': pm2_null_avg,
         'bar_homo_avg': bar_homo_avg, 'bar_hemi_avg': bar_hemi_avg, 'bar_null_avg': bar_null_avg})


# write into that file an item for each column
with open('temp.csv', 'rb') as csv_file:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(csv_file)  # comma is default delimiter
    to_db = [(i['qcid'], i['rfo_homo_avg'], i['rfo_hemi_avg'], i['rfo_null_avg'], i['f2a_homo_avg'], i['f2a_hemi_avg'], i['f2a_null_avg'], i['f3a_homo_avg'], i['f3a_hemi_avg'], i['f3a_null_avg'], i['f3c_homo_avg'], i['f3c_hemi_avg'], i['f3c_null_avg'], i['acyto'], i['bcyto'], i['gt73_homo_avg'], i['gt73_hemi_avg'], i['gt73_null_avg'], i['pm1_homo_avg'], i['pm1_hemi_avg'], i['pm1_null_avg'], i['pm2_homo_avg'], i['pm2_hemi_avg'], i['pm2_null_avg'], i['bar_homo_avg'], i['bar_hemi_avg'], i['bar_null_avg']) for i in dr]

print to_db


con = sqlite3.connect('zygodb.sqlite')
con.text_factory = str
cur = con.cursor()

cur.executemany("INSERT OR REPLACE INTO zygosity (qcid, rfo_homo_avg, rfo_hemi_avg, rfo_null_avg, f2a_homo_avg, f2a_hemi_avg, f2a_null_avg, f3a_homo_avg, f3a_hemi_avg, f3a_null_avg, f3c_homo_avg, f3c_hemi_avg, f3c_null_avg, acyto, bcyto, gt73_homo_avg, gt73_hemi_avg, gt73_null_avg, pm1_homo_avg, pm1_hemi_avg, pm1_null_avg, pm2_homo_avg, pm2_hemi_avg, pm2_null_avg, bar_homo_avg, bar_hemi_avg, bar_null_avg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()

os.remove('temp.csv')
