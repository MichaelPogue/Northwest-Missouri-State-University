'''
Author: Michael Pogue
Date:   January 29th, 2023

Purpose: The purpose for this code will be to recieve video game release dates out of orbit
from RabbitMQ, then write them to a new file. This code works in tadem with code_producer.py.

Code inspired by Dr. Denise Case
'''
# Import modules.
import pika
import sys
import csv

# Setup for output file.
output_file_name = 'vidjagame.csv'
output_file = open(output_file_name, 'w', newline='')
writer = csv.writer(output_file, delimiter=',')

# Define how to handle incoming messages, and write them to an output file.
def process_message(ch, method, properties, body):
    print('  %r' % body.decode())
    # Write data from body to output file.
    writer.writerow([body])

# Connect to RabbitMQ with failsafes in the event of an error.
def main(hn: str = 'localhost'):
    # Connect to RabbitMQ.
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=hn))
    except Exception as e: # Failure to connect to RabbitMQ handling. 
        print()
        print('ERROR: connection to RabbitMQ server failed.')
        print(f'Verify host server={hn}.')
        print(f'Error: {e}')
        print()
        connection.close()
        output_file.close()
        sys.exit(1)

    # Create connection and process incoming data. 
    try: 
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(
            queue='hello', on_message_callback=process_message, auto_ack=True)
        # Surfce pro doesn't have a BREAK KEY! =O
        print(' \U0001f600 Channels open and waiting for message. To exit, pretend CTRL+C works or CTRL+BREAK.')
        channel.start_consuming()

    # Error processing and closure of connection and/or files.
    except Exception as e:
        print()
        print('ERROR: You dun screwed up.')
        print(f'Error: {e}')
        connection.close()
        output_file.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print('Connection terminated via user input.')
        connection.close()
        output_file.close()
        sys.exit(0)
    finally:
        print('\nLater gater.\n')
        connection.close()
        output_file.close()

# Launch script to begin message gathering.
if __name__ == '__main__':
    main('localhost')
