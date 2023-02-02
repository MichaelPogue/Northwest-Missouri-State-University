'''
Author: Michael Pogue
Date:   January 29th, 2023

Purpose: The purpose for this code will be to blaste video game release dates into orbit
to be picked up by RabbitMQ. This code works in tadem with code_consumer.py.

Code inspired by Dr. Denise Case
'''

# Import modules
import os
import pika
import csv

# Setup file to be streamed
file_path = os.path.expanduser(
    '~/Documents/school/Northwest-Missouri-State-University/Streaming Data (44-671)/module02-multiple-processes-main/video-games-2022.csv')

input_file = open(file_path, 'r')
reader = csv.reader(input_file, delimiter=',')
header = next(reader)
header_list = ['Month', 'Title',
            'Platform(s)', 'Genre(s)', 'Developer(s)', 'Publisher(s)']

# Print information for users. 
print(f'File Directory: {os.getcwd()}')
print(f'Input File Path: {file_path}')

# Create a connection to RabbitMQ.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

# Use connection to stream data into RabbitMQ.
for row in reader:
    Month, Day, Title, Platform, Genre, Developer, Publisher = row
    fstring_message = f'[{Month}, {Day}, {Title}, {Platform}, {Genre}, {Developer}, {Publisher}]'
    channel.basic_publish(
        exchange='', routing_key='hello', body=fstring_message)

# Close channel and file. 
channel.close()
input_file.close()
