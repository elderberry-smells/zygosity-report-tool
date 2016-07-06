import csv
import sqlite3

# prompting for which QC#'s the user would like to report
print "What QC#'s would you like to report?"
start = int(raw_input('Starting QC#: '))
finish = int(raw_input('End QC#: '))
samples = ['QC-2016-' + str("%03d" % i) for i in range(start, finish + 1)]

print 'Report Generated for:', samples[0], 'to', samples[-1]

report_len = len(samples)

if len(samples) > 1:
    report_name = samples[0] + ' to ' + samples[-1] + ' Report'
else:
    report_name = samples[0] + ' Report'

# grabbing the defined set of data from the database to write into a template file
con = sqlite3.connect('zygodb.sqlite')
con.text_factory = str
cur = con.cursor()
data = cur.execute("SELECT * FROM SP_details NATURAL JOIN zygosity")

# writing the data to the temporary file and renaming it something other than 'template'

with open(report_name + '.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['QC ID#', 'BATCH #', 'INSPECTION LOT', 'DETAILS', 'PLANT #', 'MATERIAL', 'RECEIVED', 'REPORTED', 'RFO HOMO', 'RFO HEMI', 'RFO NULL', 'FAD2A HOMO', 'FAD2A HEMI', 'FAD2A NULL', 'FAD3A HOMO', 'FAD3A HEMI', 'FAD3A NULL', 'FAD3C HOMO', 'FAD3C HEMI', 'FAD3C NULL', 'ACYTO(%)', 'BCYTO(%)', 'RFO IN A LINE (BULK)', 'RFO IN B LINE (BULK)'])
    for line in data:
        if line[0] in samples:
            writer.writerow(line[:22])
