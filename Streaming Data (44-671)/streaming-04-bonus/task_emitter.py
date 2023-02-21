"""
    Original Code:    Dr. Denise Case
    Author:           Michael Pogue
    Date:             Feburary 07, 2023
"""

import pika
import sys
import webbrowser
import csv 
import time 
import pandas as pd
from time import strftime 

"""  
------------------------------------------------------------------------------------------ """
def user_pick_columns():
    # column_1 = input('Choose your first column:')
    # column_2 = input('Choose your second column:')
    column_1 = 2
    column_2 = 3
    return column_1, column_2

"""  
------------------------------------------------------------------------------------------ """
def send_message_1(host: str, queue_name: str, file: csv, choice: int):
    with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for val in reader:
                try:
                    conn = pika.BlockingConnection(pika.ConnectionParameters(host))
                    ch = conn.channel()
                    ch.queue_declare(queue=queue_name, durable=True)
                    ch.basic_publish(exchange="", routing_key=queue_name, body=val[choice])
                    print(f" [x] Sent {val[choice]}")
                except pika.exceptions.AMQPConnectionError as e:
                    print(f"Error: Connection to RabbitMQ server failed: {e}")
                    sys.exit(1)
                finally:
                    conn.close()

def send_message_2(host: str, queue_name: str, file: csv, choice: int):
    with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for val in reader:
                try:
                    conn = pika.BlockingConnection(pika.ConnectionParameters(host))
                    ch = conn.channel()
                    ch.queue_declare(queue=queue_name, durable=True)
                    ch.basic_publish(exchange="", routing_key=queue_name, body=val[choice])
                    print(f" [x] Sent: {val[choice]}")
                except pika.exceptions.AMQPConnectionError as e:
                    print(f"Error: Connection to RabbitMQ server failed: {e}")
                    sys.exit(1)
                finally:
                    conn.close()

"""  
------------------------------------------------------------------------------------------ """
if __name__ == "__main__":
    host = 'localhost'
    choice_1, choice_2 = user_pick_columns()
    task_queue_1 = 'first_choice'
    task_queue_2 = 'second_choice'
    file = 'data-video-games-2022.csv'
    send_message_1(host, task_queue_1, file, choice_1)
    # send_message_2(host, task_queue_2, file, choice_2)
