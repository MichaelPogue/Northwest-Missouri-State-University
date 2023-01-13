import os
import csv
import pandas as pd



BASE_FILE = 'batchfile_0_farenheit.csv'
input_file_name = 'batchfile_2_kelvin.csv'
output_file_name = 'batchfile_3_farenheit.csv'

input_file_name = "batchfile_0_farenheit.csv"
output_file_name = "batchfile_1_celcius.csv"
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

header = next(reader)

header_list = ["Year","Month","Day","Time","TempC"]
writer.writerow(header_list)

for row in reader:
    Year, Month, Day, Time, TempA = row
    TempB = round((float(TempA) - 32.0) * 5.0 / 9.0,2)
    writer.writerow([Year, Month, Day, Time, TempB])

output_file.close()
input_file.close()

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
    Year, Month, Day, Time, TempA = row
    TempB = round((float(TempA) +273.15),2)
    writer.writerow([Year, Month, Day, Time, TempB])

output_file.close()
input_file.close()

input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

header = next(reader)

header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

for row in reader:
    Year, Month, Day, Time, TempA = row
    TempB = round(((float(TempA)* 9/5) - 459.67),2)  
    writer.writerow([Year, Month, Day, Time, TempB])

output_file.close()
input_file.close()