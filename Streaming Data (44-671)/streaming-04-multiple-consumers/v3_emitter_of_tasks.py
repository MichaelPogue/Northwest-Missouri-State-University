"""
    This program sends a message to a queue on the RabbitMQ server.
    Make tasks harder/longer-running by adding dots at the end of the message.

    Author:    Dr. Denise Case
    Edits by:  Michael Pogue
    Date:      Feburary 07, 2023

"""

import pika
import sys
import webbrowser
import csv # File support.
import time # Slow process down to better manage input/output times.
from time import strftime # Importing time module to track production and consumption times.

"""  
File Input / RabbitMQ Monitoring

Gather input data from user to determine which file they want to look at and whether or 
not they want to track its progress on Rabbit MQ.
------------------------------------------------------------------------------------------ """
def file_input():
    file = input('What is the name of the file you want to read (leave out CSV)?') + '.csv'
    return file

def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()


"""  
    Reads csv file as a message to the queue each execution.
    This process runs and finishes.
    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        user_requested_file: File as defined by user.
        current_time: Current time of code execution.
------------------------------------------------------------------------------------------ """
def send_message(host: str, queue_name: str, user_requested_file, current_time):
    # Open the file as dictated by user.
    with open(user_requested_file, 'r') as read:
        reader = csv.reader(read, delimiter= '\n')
        # Read said file line by line.
        for row in reader:
            time.sleep(1) # Delay set to send code at a reasonable speed.
            row_text = f"{row}"
            message = row_text.encode()

            try:
                # create a blocking connection to the RabbitMQ server
                conn = pika.BlockingConnection(pika.ConnectionParameters(host))
                # use the connection to create a communication channel
                ch = conn.channel()
                # use the channel to declare a durable queue
                # a durable queue will survive a RabbitMQ server restart
                # and help ensure messages are processed in order
                # messages will not be deleted until the consumer acknowledges
                ch.queue_declare(queue=queue_name, durable=True)
                # use the channel to publish a message to the queue
                # every message passes through an exchange
                ch.basic_publish(exchange="", routing_key=queue_name, body=message)
                # print a message to the console for the user
                print(f" [x] Sent {message} at {current_time}")
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Error: Connection to RabbitMQ server failed: {e}")
                sys.exit(1)
            finally:
                # close the connection to the server
                conn.close()


"""  
Launch Code!
------------------------------------------------------------------------------------------ """
# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    # Assign variables to be sent as a message.
    host = 'localhost'
    task_queue = 'task_queue3'
    user_requested_file = file_input()
    current_time = strftime('%H:%M:%S') # Time is for tracking purposes only.
    offer_rabbitmq_admin_site()
    # send the message to the queue
    send_message(host, task_queue, user_requested_file, current_time)
