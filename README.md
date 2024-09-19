# Binary Search
## Overview
This repository provides code and tests that implements a Binary search algorithm to find words not in a sorted tuple of words in **O(N*log(N)) time**. 

## Returns
The program will return words not in word list. If all words given are in the sorted wordList the program will return an empty tuple.

## Stipulations
Inputs (words and wordlist) must be tuples. If they are not the program will return None.
An empty tuple given for words will return an empty tuple.
An empty tuple given for wordlist will return words.
Words are case insensitive. So aBc is treated the same as AbC.

## To run
Make sure you have python downloaded on your machine by running "python --version" in the terminal. Then run "python main_test.py (...)" to see all the tests pass.

To run with custom input comment out the tests in main_test.py and write a line like so "print(new_words((tuple_x), (tuple_y)))" to see the result of your calculation.

An example test statement would be "print(new_words(('aBC','123','456','a1b2c3','b2c3d4'),('456','Abc','B2C3D4')))" to which the program would return:  

('123', 'a1b2c3')

## To Run Tests 
Run "python main_test.py".
