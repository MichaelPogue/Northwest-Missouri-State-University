"""
Batch Process - second transformation

Reads from a file, transform, write to a new file.

In this case, covert degree C to degree K.

"""

import csv

input_file_name = "batchfile_1_celcius.csv"
output_file_name = "batchfile_2_kelvin.csv"

input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ["Year","Month","Day","Time","TempK"]
writer.writerow(header_list)

for row in reader:
    Year, Month, Day, Time, TempC = row
    TempK = round(float(TempC) + 273.15, 2)
    writer.writerow([Year, Month, Day, Time, TempK])

output_file.close()
input_file.close()
