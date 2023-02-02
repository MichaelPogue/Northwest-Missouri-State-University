# Module 3 - Bonus
Code by:    Michael Pogue

Created on: January 29th, 2023

Original Data: https://github.com/MichaelPogue/Northwest-Missouri-State-University/tree/main/Streaming%20Data%20(44-671)/module02-multiple-processes-main 

**Story Time:**
Inspired by my video game data from the previous lesson, as well as the code, I recreated the code from both locations and added 
them to this repo. Data is first read row by row with the following:
```for row in reader: Month, Day, Title, Platform, Genre, Developer, Publisher = row```

Once read, the connection established to RabbitMQ was used to stream the newfound data to its new home. From there, the data was unpacked and saved to a CSV file line by line.


### Optional Bonus

Use your skills to create a custom project. Earn up to an additional 10%.

1. Create  your own custom project. Create a new repo named streaming-03-bonus-yourname. (e.g., streaming-03-bonus-case)  :heavy_check_mark:
1. Create a new producer that reads from your earlier CSV file and writes messages to a new queue every 1-3 seconds. :heavy_check_mark:
1. Create a new consumer that reads your messages from this queue, and writes the messages to a new file as they are received. :heavy_check_mark:
1. Your README.md must include your name, the date. :heavy_check_mark:
1. Your README.md must provide a link to the original data.  :heavy_check_mark:
1. Your README.md must clearly describe what you did, telling the story of your data, your producer, and your consumer,:heavy_check_mark:
1. Your README.md must display a screenshot of the two windows running concurrently. :heavy_check_mark:
1. Add a .gitignore (telling which files and directories NOT to push up to GitHub).  Recommendation:  copy .gitignore from an earlier repo. :heavy_check_mark:
1. These are the important skills you want to demonstrate. Create unique streaming projects, using professional communication. I encourage you to give it a try. :heavy_check_mark::heavy_check_mark::heavy_check_mark:


![2023-01-29 (3)](https://user-images.githubusercontent.com/115908053/215368208-088b545c-90e4-4334-8975-e0e82794adae.png)
