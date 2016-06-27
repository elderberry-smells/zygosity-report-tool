import sqlite3

conn = sqlite3.connect('zygodb.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute('''CREATE TABLE zygosity (
            qcid TEXT UNIQUE PRIMARY KEY,
            rfo_homo_avg REAL,
            rfo_hemi_avg REAL,
            rfo_null_avg REAL,
            f2a_homo_avg REAL,
            f2a_hemi_avg REAL,
            f2a_null_avg REAL,
            f3a_homo_avg REAL,
            f3a_hemi_avg REAL,
            f3a_null_avg REAL,
            f3c_homo_avg REAL,
            f3c_hemi_avg REAL,
            f3c_null_avg REAL,
            acyto REAL,
            bcyto REAL,
            gt73_homo_avg REAL,
            gt73_hemi_avg REAL,
            gt73_null_avg REAL,
            pm1_homo_avg REAL,
            pm1_hemi_avg REAL,
            pm1_null_avg REAL,
            pm2_homo_avg REAL,
            pm2_hemi_avg REAL,
            pm2_null_avg REAL,
            bar_homo_avg REAL,
            bar_hemi_avg REAL,
            bar_null_avg REAL
)''')


cur.execute('''CREATE TABLE raw_data (
            qcid TEXT UNIQUE PRIMARY KEY,
            rfo_homo INTEGER,
            rfo_hemi INTEGER,
            rfo_null INTEGER,
            f2a_homo INTEGER,
            f2a_hemi INTEGER,
            f2a_null INTEGER,
            f3a_homo INTEGER,
            f3a_hemi INTEGER,
            f3a_null INTEGER,
            f3c_homo INTEGER,
            f3c_hemi INTEGER,
            f3c_null INTEGER,
            cyto_homo INTEGER,
            cyto_null INTEGER,
            gt73_homo INTEGER,
            gt73_hemi INTEGER,
            gt73_null INTEGER,
            pm1_homo INTEGER,
            pm1_hemi INTEGER,
            pm1_null INTEGER,
            pm2_homo INTEGER,
            pm2_hemi INTEGER,
            pm2_null INTEGER,
            bar_homo INTEGER,
            bar_hemi INTEGER,
            bar_null INTEGER

)''')

