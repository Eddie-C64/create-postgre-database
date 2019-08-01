import psycopg2
import csv

conn = psycopg2.connect(dbname="postgres", user="postgres")
cursor = conn.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS storms;
    CREATE TABLE storms (id integer PRIMARY KEY,
                        year integer,
                        month integer,
                        day integer,
                        ad_time text,
                        btid integer,
                        name text,
                        lat text,
                        long text,
                        wind_kts integer,
                        pressure integer,
                        cat text,
                        basin text,
                        shape_leng text);
    """)

conn.commit()
print("Table created!")

with open('storm-data.csv', 'r') as readFile:
    next(readFile) # Skip the header of the csv
    reader = csv.reader(readFile)

    for row in reader:
        cursor.execute("INSERT INTO storms VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)", row)
        conn.commit()
# TODO: Connect to database
print("Testing Data in storms table!, \n")
print(cursor.execute("SELECT * FROM storms LIMIT 10"))
print("Database creation a success.")
