"""
    Original Code:    Dr. Denise Case
    Author:           Michael Pogue
    Date:             Feburary 07, 2023
"""

import pika
import sys
import time
import csv
from time import strftime

"""  
------------------------------------------------------------------------------------------ """
def callback1(ch, method, properties, body):
    file = open(f'data-consume_1.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(body.decode())
    print(f" [x] Received {body.decode()} at {strftime('%H:%M:%S')}")

    time.sleep(body.count(b"."))
    print(" [x] Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def callback2(ch, method, properties, body):
    file = open(f'data-consume_2.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(body.decode())
    print(f" [x] Received {body.decode()} at {strftime('%H:%M:%S')}")

    time.sleep(body.count(b"."))
    print(" [x] Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)





"""  
------------------------------------------------------------------------------------------ """
def main(hn: str = "localhost", qn: str = "task_queue"):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hn))
    except Exception as e:
        print()
        print("ERROR: connection to RabbitMQ server failed.")
        print(f"Verify the server is running on host={hn}.")
        print(f"The error says: {e}")
        print()
        sys.exit(1)

    try:
        channel = connection.channel()
        channel.queue_declare(queue=qn, durable=True)
        channel.basic_qos(prefetch_count=1)
        if qn == 'first_choice':
            channel.basic_consume( queue=qn, on_message_callback=callback1)
        else: 
            channel.basic_consume( queue=qn, on_message_callback=callback2)
        print(" [*] Ready for work. To exit press CTRL+C")
        channel.start_consuming()

    except Exception as e:
        print()
        print("ERROR: something went wrong.")
        print(f"The error says: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print(" User interrupted continuous listening process.")
        sys.exit(0)
    finally:
        print("\nClosing connection. Goodbye.\n")
        connection.close()

"""  
------------------------------------------------------------------------------------------ """
if __name__ == "__main__":
    host = 'localhost'
    task_queue_1 = 'first_choice'
    task_queue_2 = 'second_choice'
    main(host, task_queue_1)
    main(host, task_queue_2)
