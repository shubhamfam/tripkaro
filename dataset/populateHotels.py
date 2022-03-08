import psycopg2, csv

rows = []
with open("dataset/hotels.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    ['additional_info', 'address', 'area', 'city', 'hotel_description', 'hotel_facilities', 'hotel_star_rating', 'point_of_interest', 'property_name', 'property_type', 'state']

    data = []
    for row in csvreader:
        name = row[8].replace("'","")
        type = row[9].replace("'","")
        desc = row[4].replace("'","")
        addr = row[1].replace("'","")
        city = row[3].replace("'","")
        facilities = row[5].replace("'","")
        star_rating = row[6].replace("'","")
        additional_info = row[0].replace("'","")
        
        if city not in ['Jaipur', 'Pune', 'Mumbai']:
            continue

        record = (str(name), str(type), str(desc), str(addr), str(city), str(facilities), int(star_rating), str(additional_info))

        data.append(str(record))

data = (',').join(data)



with open('hotwl_inserts.txt', 'w') as f:
    f.write("INSERT INTO core_hotel(name, type, description, address,city,facilities, star_rating, additional_info) VALUES "+data)