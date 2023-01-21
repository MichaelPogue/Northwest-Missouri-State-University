"""

Streaming Process - port 9999

First we need a fake stream of data. 

We'll use the temperature data from the batch process.

But we need to reverse the order of the rows 
so we can read oldest data first.

Important! We'll stream forever - or until we 
           read the end of the file. 
           Use use Ctrl-C to stop.
           (Hit Control key and c key at the same time.)

Explore more at 
https://wiki.python.org/moin/UdpCommunication

"""

import csv
import socket
import time

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)

class infinity(HOST, PORT, ADDRESS_TUPLE):
    def __init__(self):
        self.HOST = HOST
        self.PORT = PORT
        self.ADDRESS_TUPLE = ADDRESS_TUPLE

    def test(self):
        socket_family = socket.AF_INET 
        socket_type = socket.SOCK_DGRAM 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        input_file = open("batchfile_0_farenheit.csv", "r")
        reversed = sorted(input_file)
        reader = csv.reader(reversed, delimiter=",")
        for row in reader:
            Year, Month, Day, Time, TempF = row
            fstring_message = f"[{Year}, {Month}, {Day}, {Time}, {TempF}]"
            MESSAGE = fstring_message.encode()
            sock.sendto(MESSAGE, ADDRESS_TUPLE)
            print (f"Sent: {MESSAGE} on port {PORT}.")
            time.sleep(3)

inf = infinity
inf.test()


