import psycopg2, csv
from psycopg2.extras import execute_values

rows = []
with open("dataset/pune/Places.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        row = tuple(row)
        rows.append(str(row))

print(rows)
conn = psycopg2.connect(host="localhost",
                        database="tripkaro",
                        user="postgres",
                        password="root")

cur = conn.cursor()

data = (',').join(rows)


q = "INSERT INTO core_place (name, address, city, tag) VALUES"+ data

print(q)

cur.execute(q)
