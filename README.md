## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a simple parse for file exemple you have a file with this structure :
```
09:20-11:00 Introduction
11:00-11:15 Exercises
11:15-11:35 Break
11:35-12:30 Numbers and strings
12:30-13:30 Lunch Break
13:30-14:10 Exercises
14:10-14:30 Solutions
14:30-14:40 Break
14:40-15:40 Lists
15:40-17:00 Exercises
17:00-17:30 Solutions

09:30-10:30 Lists and Tuples
10:30-10:50 Break
10:50-12:00 Exercises
12:00-12:30 Solutions
12:30-12:45 Dictionaries
12:45-14:15 Lunch Break
14:15-16:00 Exercises
16:00-16:15 Solutions
16:15-16:30 Break
16:30-17:00 Functions
17:00-17:30 Exercises
```
The project return :

```
Break                  65 minutes       6 %
Dictionaries           15 minutes       1 %
Exercises             340 minutes      35 %
Functions              30 minutes       3 %
Introduction          100 minutes      10 %
Lists                 120 minutes      12 %
Lunch                 150 minutes      15 %
Numbers                55 minutes       5 %
Solutions              95 minutes       9 %
```


	
## Technologies
Project is created with:
- Python 3
- lib: datetime, sys, logging
- test : unittest
- doc : pdoc3
	
## Setup
To run this project, you just go on the directory and launch parle_log + your file :

```
for Linux :
$ cd ../parse_log
$ python3 parse_log.py <my_file>

for Windows:
> cd ../parse_log
> python parse_log.py <my_file>
```
