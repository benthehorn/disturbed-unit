# Assignment 1 for Business Intelligence
#### By Disturbed Unit

1. We ran the file through Terminal. Initially firing up under the Virtual Machine, so we could access it using SSH.
  After navigating to the /synced_folder/assignments/assignment_1/ we were able to run the python file using the command
  `python assignment_1.py`.
  We were able to see using the `ls` command that there were only three files prior to running the python script. Afterwards,
  there were five, so it created two files in total:
    1. **price_list.csv**
    1. **prices.png**
    
    ![alt text](https://github.com/semester-groupies/disturbed-unit/blob/master/resources/files.png "Screenshot of generated files")

    
---
    
2. The aforementioned two files is a **comma separated values** file, and an **image** (portable networks graphics).

---

3. **3307228.119047619** (which is what?)

---

4. 
import os
> import os is a python modeul that enables us to use os dependent functionality. http://www.pythonforbeginners.com/os/pythons-os-module

import csv
> import csv enables us to read and write csv files, as well as many other functions

import requests
> import requests allows us to make easy http requests 

import platform
> import platform allows us to access the underlying platforms data, such as, hardware and os.

import statistics
> import statistics helps us to create statistics. Features include mean, median, mode, standard deviation and variance.

import matplotlib
> import matplotlib is a plotting library for python, for making graphs, for example. (prices.png)
> import matplotlib.pyplot as plt extends the functionality of the plotter.
