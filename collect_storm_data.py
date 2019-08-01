import io
from urllib import request
import csv

url_string = "https://dq-content.s3.amazonaws.com/251/storm_data.csv"

response = request.urlopen(url_string)
reader = csv.reader(io.TextIOWrapper(response))

columns = next(reader)
print(columns)

with open("storm-data.csv", "w") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(columns)
    for index, line in enumerate(reader):
        writer.writerow(line)
        print(index,'\n')

writeFile.close()
print("File was created!")
