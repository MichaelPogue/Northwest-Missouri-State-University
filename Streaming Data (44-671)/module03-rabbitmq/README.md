# streaming-03-rabbitmq

Get started with RabbitMQ, a message broker, that enables multiple processes to communicate reliably through an intermediary 

## Before You Begin

1. Fork this starter repo into your GitHub. :heavy_check_mark:
1. Clone your repo down to your machine. :heavy_check_mark:
1. In VS Code with Python extension, click on emit_message_v1.py to get VS Code in Python mode. :heavy_check_mark:
1. View / Command Palette - then Python: Select Interpreter :heavy_check_mark:
1. Select your conda environment. See the references below for more. :heavy_check_mark:
1. Use the terminal to install pika into your active environment. :heavy_check_mark:

`conda install -c conda-forge pika`

## Read

1. Read the [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) :heavy_check_mark:
1. Read the code and comments in this repo. :heavy_check_mark:

## Execute about,py

1. Run about.py.:heavy_check_mark:
1. Read about.txt. :heavy_check_mark:
1. Verfiy you have exactly one active, one None env. :heavy_check_mark:

- ***I have one. TODO does base count as active?***
      
## Version 1 - Execute the Producer/Sender

1. Read v1_emit_message.py (and the tutorial) :heavy_check_mark:
1. Run the file. :heavy_check_mark:

You'll need to fix an error in the program to get it to run. 
Once it runs and finishes, we can reuse the terminal. 

- ***Fixed errors in spacing. Added message to send in two places.***

## Version 1 - Execute the Consumer/Listener

1. Read v1_listen_for_messages.py (and the tutorial):heavy_check_mark:
1. Run the file. :heavy_check_mark:

You'll need to fix an error in the program to get it to run.
Once it runs successfully, will it terminate on its own? How do you know?
As long as the process is running, we cannot use this terminal for other commands.

***It will not terminate as it is listening for commands. I know this because I couldn't
input any commands once the program was running.***

## Version 1 - Open a New Terminal / Emit More Messages

1. Open a new terminal window. :heavy_check_mark:
1. Use this new window to emit more messages :heavy_check_mark:
1. In v1_emit_message.py, modify the message. :heavy_check_mark:
1. Execute the script. :heavy_check_mark:
1. Watch what happens in the listening window. :heavy_check_mark:
1. Do this several times to emit at least 3 different messages. :heavy_check_mark:

## Version 1: Don't Repeat Yourself (DRY)

1. Did you notice you had to change the message in two places? :heavy_check_mark:
   1. You update the actual message sent. :heavy_check_mark:
   1. You also update what is displayed to the user. :heavy_check_mark:
1. Fix this by introducting a variable to hold the message. :heavy_check_mark:
   1. Use your variable when sending. :heavy_check_mark:
   1. Use the variable again when displaying to the user. :heavy_check_mark:

To send a new message, you'll only make one change.
Updating and improving code is called 'refactoring'.
Use your skills to keep coding enjoyable. :heavy_check_mark:

## Version 2

Now look at the second version of each file.
These include more graceful error handling,
and a consistent, reusable approach to building code. :heavy_check_mark:

Each of the version 2 programs include an error as well.

1. Find the error and fix it. :heavy_check_mark:
1. Compare the structure of the version 2 files. :heavy_check_mark:
1. Modify the docstrings on all your files. :heavy_check_mark:
1. Include your name and the date. :heavy_check_mark:
1. Imports always go at the top, just after the file docstring. :heavy_check_mark:
1. Imports should be one per line - why?

***It's easier to process and understand. It's a quality of life improvement as nobody likes spaghetti code.***

1. Then, define your functions. :x: - ***No need, the function description***
1. Functions are reuable logic blocks. :heavy_check_mark:
1. Everything the function needs comes in through the arguments. :heavy_check_mark:
1. A function may - or may not - return a value. :heavy_check_mark:
1. When we open a connection, we should close the connection. :heavy_check_mark:
1. Which of the 4 files will always close() the connection? ***The two with the ```.close()``` command.***
3. Search GitHub for if **name** == "**main**": :heavy_check_mark: 
4. How many hits did you get? :heavy_check_mark:  ***TOO MANY. I got 390 million examples of use in code.***
5. Learn and understand this common Python idiom. :heavy_check_mark: ***I've tried using it in my side project, but it made things worse. THough that's probably because I didn't have a ```def main():``` for it to be based off of.***

## Reference

- [RabbitMQ Tutorial - Hello, World!](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) :heavy_check_mark: 
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

## Multiple Terminals

![Mac Example](screenshot.png)
