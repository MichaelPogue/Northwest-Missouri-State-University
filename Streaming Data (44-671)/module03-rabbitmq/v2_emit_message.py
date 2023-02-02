"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023


Module 3:      Homework V2
Authored by:   Dr. Denise Case
Edited By:     Michael Pogue
Supervised By: Boogers the Cat
Date:          29Jan23
Function:      Create a message in list form and broadcast entire list.

"""

# add imports at the beginning of the file
import pika
import sys


def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue

    """

    list = ["Early one morn, I rose for work,", "Little I knew, of Booger's quirk,",
            "From her nose did boogers dripped,", "Which caused me sorrow as I tripped,",
            "Writhing on the floor, did I proclaim,", "Henceforth Boogers shall be your name!"]

    for n in range(len(list)):
        message = list[n]
        try:
            # create a blocking connection to the RabbitMQ server
            conn = pika.BlockingConnection(pika.ConnectionParameters(host))
            # use the connection to create a communication channel
            ch = conn.channel()
            # use the channel to declare a queue
            ch.queue_declare(queue=queue_name)
            # use the channel to publish a message to the queue
            ch.basic_publish(exchange="", routing_key=queue_name, body=message)
            # print a message to the console for the user
            print(f" [x] Sent {message}")
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error: Connection to RabbitMQ server failed: {e}")
            sys.exit(1)
        finally:
            # close the connection to the server
            conn.close()


# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    send_message("localhost", "hello", "Hello World!")
