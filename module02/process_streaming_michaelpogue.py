#####################################
# Module 02 - Code by Michael Pogue
#####################################
import csv
import socket
import time

#####################################
# Setup Port for Data Stream.
#####################################
HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)

socket_family = socket.AF_INET 
socket_type = socket.SOCK_DGRAM 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#####################################
# Setup file input and output.
#####################################
input_file = open("video-games-2022.csv", "r") # I had to swap from dice_com-job_us_sample due to certain entries breaking.
reader = csv.reader(input_file, delimiter=",")

output_file_name = "out9.txt"
output_file = open(output_file_name, "w", newline='')

writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ['Month', 'Title', 'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']
writer.writerow(header_list)

#####################################
# Code to read row by row and write.
#####################################
for row in reader:
    Month, Day, Title, Platform, Genre, Developer, Publisher = row
    fstring_message = f"[{Month}, {Day}, {Title}, {Platform}, {Genre}, {Developer}, {Publisher}]"
    MESSAGE = fstring_message.encode()
    sock.sendto(MESSAGE, ADDRESS_TUPLE)
    print (f"Sent: {MESSAGE} on port {PORT}.")
    writer.writerow([Month, Day, Title, Platform, Genre, Developer, Publisher])
    time.sleep(3)

output_file.close()
input_file.close()