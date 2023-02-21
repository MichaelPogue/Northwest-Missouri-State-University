# streaming-04-multiple-consumers

> Use RabbitMQ to distribute tasks to multiple workers

One process will create task messages. Multiple worker processes will share the work. 


## Before You Begin

1. Fork this starter repo into your GitHub. :heavy_check_mark:
1. Clone your repo down to your machine. :heavy_check_mark:
1. View / Command Palette - then Python: Select Interpreter :heavy_check_mark:
1. Select your conda environment. :heavy_check_mark:

## Read

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html) :heavy_check_mark:
1. Read the code and comments in this repo. :heavy_check_mark:

## RabbitMQ Admin 

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

## Execute the Producer

1. Run emitter_of_tasks.py (say y to monitor RabbitMQ queues)  :heavy_check_mark:

Explore the RabbitMQ website.

## Execute a Consumer / Worker

1. Run listening_worker.py :heavy_check_mark:

Will it terminate on its own? How do you know? 

## Ready for Work

1. Use your emitter_of_tasks to produce more task messages.:heavy_check_mark:

## Start Another Listening Worker 

1. Use your listening_worker.py script to launch a second worker. :heavy_check_mark:

Follow the tutorial. 
Add multiple tasks (e.g. First message, Second message, etc.) :heavy_check_mark:
***Task completed in a Jupyter Notebook file, for ease of testing.***
How are tasks distributed?
***Tasks appear to be given in order, one at a time.***
Monitor the windows with at least two workers. :heavy_check_mark:
Which worker gets which tasks?
***As mentioned above, the work is completed in order. I didn't really read a set method to who sees what.***


## Your Project - Version 3 - Automating the Tasks
In this part, you'll build a Version 3 much like Version 2, except - instead of getting messages from the console the producer will read from tasks.csv. Much easier for the human! Multiple workers will retrieve the messages as they do in version 2. 

1. As you code, follow conventions, show professionalism and good communication. :heavy_check_mark:
1. Copy the Version 2 files to start your version 3. :heavy_check_mark:
1. Keep the formal code comments - and as many as you need for understanding.:heavy_check_mark:
1. You'll be writing apps on your own (following a specification) for the rest of the course - you'll want good notes/a good understanding of how to implement streaming systems that use RabbitMQ.
1. Use docstrings at the top of the file and the start of each function.:heavy_check_mark:
1. Modify your producer to slowly read tasks from tasks.csv instead of the console.  Hint: Go back examples from earlier modules.:heavy_check_mark:
1. Use what you know about functions to make getting a message as reusable as possible!  :heavy_check_mark:
1. Should you hardcode the data filename? Or would it be helpful to assign the filename to a variable? ***Variable. I made it a variable as it's easier to adjust and manipulate should changes be necessary.***
1. Do you like having the app open the RabbitMQ webpage? If so, modify it so it does it without asking - or so you can turn off the question as needed. 
        *** I commented it out while coding as it was a nuisance. I applied it at the end as it does provide helpful information.***
        To turn off the question, introduce a variable "show_offer" and set it to False. :x:
        Only offer to show the Admin webpage if show_offer is True. :x:
1. Add more records to tasks.csv to make some longer running tasks (use more dots - periods - at the end of each task).  :heavy_check_mark:
1. Update the README to include your name, the date, instructions for anyone who forks your repo and wants to try your project. :heavy_check_mark:
1. Display your screenshot in the README.md showing at least 3 terminals (one emitting, two or more listening).:heavy_check_mark:
1. Use comments in the code and the README.md to explain your version 3 RabbitMQ project. :heavy_check_mark:
1. Using VS Code or the command line, git add /commit (with a message!) and push / sync your code to your GitHub repo. :heavy_check_mark:


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


## Screenshot

See a running example with at least 3 concurrent process windows here:
![Module 4 - Homework 1](https://user-images.githubusercontent.com/115908053/217397207-5ea8ccc3-d187-46f0-9387-661161595223.jpg)

