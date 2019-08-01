import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres")
cursor = conn.cursor()
query = cursor.execute("SELECT * FROM storms")
print(query)
print("Command executed!")
conn.close()
