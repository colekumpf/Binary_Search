# Binary Search
## Overview
This repository provides code and tests that implements a Binary search algorithm to find words not in a sorted tuple of words in **O(N*log(N)) time**. 

## Returns
The program will return words not in word list. If all words given are in the sorted wordList the program will return an empty tuple.

## Stipulations
Any input of length one or two will return None.
Any non tuple input will return None.

## To run
Make sure you have python downloaded on your machine by running "python --version" in the terminal. Then run "python main.py (...)" with your desired input.

An example running statement would be "python main.py ('a','b','a')" to which the program would return: 

('a','a') 

## To Run Tests 
Run "python main_test.py".

*Note the first line in the test will return none unless you give it input for palindrome testing in which case it will return the same as main.py.

