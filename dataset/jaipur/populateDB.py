import psycopg2, csv
from psycopg2.extras import execute_values
'''
rows = []
with open("Places.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        row = row[1:4]
        row.append('Jaipur')
        row = tuple(row)
        rows.append(str(row))

conn = psycopg2.connect(host="localhost",
                        database="tripkaro",
                        user="postgres",
                        password="root")

cur = conn.cursor()

data = (',').join(rows)


q = "INSERT INTO core_place (name, latitude, longitude, city) VALUES"+ data

print(q)

cur.execute(q)
'''

rows = []
with open("dataset/jaipur/Types.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        place, tag = row[1], row[2]
        q = f"UPDATE core_place SET tag = '{tag}' where name='{place}';"
        print(q)
