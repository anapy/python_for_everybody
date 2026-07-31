import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages ( name VARCHAR(128), age INTEGER)')

cur.executescript('''
INSERT INTO Ages (name, age) VALUES ('Marta', 35);
INSERT INTO Ages (name, age) VALUES ('Raman', 29);
INSERT INTO Ages (name, age) VALUES ('Mhirren', 32);
INSERT INTO Ages (name, age) VALUES ('Betheny', 25);
INSERT INTO Ages (name, age) VALUES ('Spencer', 36);
INSERT INTO Ages (name, age) VALUES ('Dharci', 34);''')


smth = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'
for row in cur.execute(smth):
    print(str(row))
conn.commit()
conn.close()