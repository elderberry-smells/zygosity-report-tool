import string
import csv
import os


# open your csv file, and get the project names included in the file from the "Project" column
# def get_qc(filename):
fname = raw_input('File Name:')


r = open(fname + '.csv', 'rb')
qcid = ""
for line in r:
    bits = line.split(',')
    for i in bits:
        if bits[2] in qcid:
            continue
        elif bits[2] == "Project":
            continue
        else:
            qcid += bits[2]

r.close()

# using the value found in the "Project Column" of the csv file, split that into seperate QC Id's in a list

qc_split = qcid.split()
qc_list_int = []
qc_list_id = []
qc_list_letter = []
# if project only consists of 1 sample
if len(qc_split) == 1:
    qc_list_id.append(qc_split[0])
# if project consists of 2 or more samples
else:
    for i in qc_split:
        if i == "TO":
            continue
        else:
            inti = (int(i[8:]))
            qc_list_int.append(inti)

    start = qc_list_int[0]
    finish = qc_list_int[1]
    qc_list_id = [qcid[:8] + str("%03d" % i) for i in range(start, finish + 1)]

pone = ['Project 1A'] + ['PROJECT 1' + i for i in string.uppercase[:26]]
ptwo = ['PROJECT 2' + i for i in string.uppercase[:26]]
pthree = ['PROJECT 3' + i for i in string.uppercase[:26]]
pfour = ['PROJECT 4' + i for i in string.uppercase[:26]]
pfive = ['PROJECT 5' + i for i in string.uppercase[:26]]
psix = ['PROJECT 6' + i for i in string.uppercase[:26]]
pseven = ['PROJECT 7' + i for i in string.uppercase[:26]]
peight = ['PROJECT 8' + i for i in string.uppercase[:26]]
pnine = ['PROJECT 9' + i for i in string.uppercase[:26]]
pten = ['PROJECT 10' + i for i in string.uppercase[:26]]

# using the QC ID list we made above, change the "Project X" to the correct QC ID and letter

with open(fname + '.csv', 'r') as f:
    assay_list = []
    # read the top line of the csv file as the headers
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

# write a csv file for each QC# in the qc_id_list and write the corresponding lines in the multiple project csv file.
for qc_number in qc_list_id:
    with open(qc_number + '.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
        writer.writeheader()

        r = open(fname + '.csv', 'rb')

        for line in r:
            bits = line.split(',')

            if bits[0] in pone and qc_number == qc_list_id[0]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[0])
                csvfile.write(','.join(bits))
            elif bits[0] in ptwo and qc_number == qc_list_id[1]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[1])
                csvfile.write(','.join(bits))
            elif bits[0] in pthree and qc_number == qc_list_id[2]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[2])
                csvfile.write(','.join(bits))
            elif bits[0] in pfour and qc_number == qc_list_id[3]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[3])
                csvfile.write(','.join(bits))
            elif bits[0] in pfive and qc_number == qc_list_id[4]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[4])
                csvfile.write(','.join(bits))
            elif bits[0] in psix and qc_number == qc_list_id[5]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[5])
                csvfile.write(','.join(bits))
            elif bits[0] in pseven and qc_number == qc_list_id[6]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[6])
                csvfile.write(','.join(bits))
            elif bits[0] in peight and qc_number == qc_list_id[7]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[7])
                csvfile.write(','.join(bits))
            elif bits[0] in pnine and qc_number == qc_list_id[8]:
                bits[0] = bits[0].replace(bits[0][:9], qc_list_id[8])
                csvfile.write(','.join(bits))
            elif bits[0] == "Box":
                continue
            else:
                if bits[0] in pten and qc_number == qc_list_id[9]:
                    bits[0] = bits[0].replace(bits[0][:10], qc_list_id[9])
                    csvfile.write(','.join(bits))

r.close()
os.remove(fname + '.csv')
