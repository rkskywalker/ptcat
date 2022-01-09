#!/usr/bin/python
import sys
#importing libraries

arguments = sys.argv # reading system arguments with file name

fileName = "" #file name variable default value declaration
opt = "" #options varaiable default value declaration
help = False #default value for help
version = False #version default value declaration
Lines = "" #Lines default value declaration

# Passing values to options and file name vaiables
if len(arguments) == 2: # if there are 2 indexes/arguments
	fileName = arguments[1] # file name will be 1st index
	if fileName == "-h"or fileName == "--help":
		help = True
	elif fileName == "-v"or fileName == "--version":
		version = True				
elif len(arguments) == 3: # if the are 3 ndexes/arguments
	opt = arguments[1] # option name will be 1st index
	fileName = arguments[2] # file name will be 2nd index
elif len(arguments) == 4: # if there are 4 indexes/arguments
	opt = arguments[1] + " " + arguments[2] # options will be 1st and 2nd indexes
	fileName = arguments[3] #file name will be 3rd index

#help attribute output
if help == True:
	print ("""
Usage: ptcat [OPTION]... [FILE]...
Concatenate FILE(s) to standard output.

With no FILE, or when FILE is -, read standard input.

  -E, --show-ends          display $ at end of each line
  -n, --number             number all output lines
 
  -h, --help     display this help and exit
  -v, --version  output version information and exit

Examples:
  ptcat f - g  Output f's contents, then standard input, then g's contents.
  ptcat        Copy standard input to standard output.
""")
	quit()
	
#version attribute output
elif version == True:
	print ("""
ptcat 1.00
Developed for Computer System Tools Coursework 2
UNIVERSITY OF WESTMINSTER - UK
Module		:		7COSC002C.1
Student Name	:		W Randika Rukshan
UOW ID		:		W1868398
IIT NO		:		20210824

This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
""")
	quit()	
	
#checking options with filename and printing output	
elif fileName != "": #if file name is not empty
	try:
		with open(fileName, 'r') as file1 : #read line by line 'r' means readable		 
			Lines = file1.readlines() # read lines value passing to Lines variable
	except Exception:
			print("\n File you entered is not found on directory. \n Please enter correct file. \n Use ptcat --help for help.")
			quit()
	count = 0 
	# Strips the newline character
	for line in Lines: 
		count += 1
		if opt == "": #read file without any option
			print(line.strip()) #printing line by line of input file
		elif opt == "-n" or opt == "--number": #checking if option is "-n"or "--number"
			print("{} {} {}".format("     ", count, line.strip())) #adding line number to each new line
		elif opt == "-E"or opt == "--show-ends": #checking if option if "-E" or "--show-ends"  
			print("{}$".format(line.strip())) #adding $ to ending of each line
		elif opt == "-n -E" or opt == "-E -n" or opt == "-number --show-ends" or opt == "--show-ends -number" :
		#checking if multiple options entered
			print("{} {} {}$".format("     ",count, line.strip())) #printing with multiple options
		elif opt != "": #checking if correct option is entered
			print("\n The option you entered is incorrect. \n Use ptcat --help for more details.") 	#print this if entered option is incorrect
			quit()
#if file name is empty							
else:
	#statement to print when there's no input file 
	print("\n Please provide input file. ex: python3.9 ptcat.py {filename or filepath} \n Use ptcat --help for help.")
	quit()
