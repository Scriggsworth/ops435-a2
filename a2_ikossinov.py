#!/usr/bin/env python3
 
'''
authorship declaration
__author__ Igor Kossinov
__date__ March 2019
__version__ 1.0
 
OPS435 Assignment 2 - Summer 2019
Program: ur_ikossinov.py
Author: "Igor Kossinov"
The python code in this file ur_ikossinov.py is original work written by
"Igor Kossinov". No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''
 

import os 
import sys
import argparse
import time

#arg.parse info and options


def list(option, filename):
		'''
		Reads specified file, line by line, if it is an ip or a user, return the list
		'''
		if option =="user":
			k = open(filename, "r")
			print ("List of users for: " + filename)
			readlines = k.readlines()

			mylist=[]
			userlist=[]
			finl=[]

			for line in readlines:
				newline = line.split()
				mylist.append(newline)

			for listuser in mylist[0:31]:
				userlist.append(listuser[0])

			for user in userlist:
				if user not in finl:
					finl.append(user)

		elif option =="host":

			k = open(filename,"r")

			print("List of hosts for: " + filename)

			readlines = k.readlines()
			mylist=[]
			userlist=[]
			finl=[]

			for line in readlines:
				newline = line.split()
				mylist.append(newline)

			for listuser in mylist[0:31]:
				userlist.append(listuser[2])

			for i in userlist:
				if i not in finl:
					finl.append(i)

		print(*finl, sep = "\n")

def userlisting(name, filename, loginuser):
	'''
	This functions takes the input from the list function, divides and takes only the time
	from each row, in the format of Mon:Day:Time:Year, then returns the list of rows.
	'''

	tlist = []
	f = open(filename, "r")
	readlines = f.readlines()
	mylist = []

	for line in readlines:
		new_line = line.split()
		mylist.append(new_line)

	if loginuser == '-u':
		for i in mylist[0:31]:
			if i[0] == name:
				tlist.append(i[3:14])
	elif loginuser == '-r':
		for i in mylist[0:31]:
			if i[2] == name:
				tlist.append(i[3:14])

	return tlist


def daily(listofusers):
	'''
	This function takes the parameter listofusers which is the list from userlist
	It first reads the date, and then deletes the date, puts it into a list, then
	joins the list to form a string. Then, it seperates each row into the login and logout time, converts the time into seconds, 
	then back into a date in the format of Y:M:D
	'''
	datetime= 0
	totaltime = 0
	datelist = []
	daytime = []

	for x in listofusers:
		test = x[1:5]
		del test[2]
		strlist1 = ' '.join(x[0:5])
		strlist2 = ' '.join(x[6:])
		strlist3 = ' '.join(test[0:])

		a = time.mktime(time.strptime(strlist1, "%a %b %d %H:%M:%S %Y"))
		b = time.mktime(time.strptime(strlist2, "%a %b %d %H:%M:%S %Y"))

		timeinsec = time.mktime(time.strptime(strlist3, "%b %d %Y"))
		datetime = time.strftime("%Y %m %d", time.localtime(timeinsec))
		totaltime = totaltime + (b - a)
		reductime = b - a
		datelist.append(datetime)
		daytime.append(int(reductime))
	
	rounduplist = []

	sumlist = []

	for t, y in zip(datelist, daytime):
		
		if t not in rounduplist:
			rounduplist.append(t)
			sumlist.append(y)
		
		
		elif t in rounduplist:
			sumlist[-1] = sumlist[-1] + y

	print("<><><><><><><><><><><><><><>")
	print("Date\t\tUsage in Seconds")

	for j, k in zip(rounduplist, sumlist):
		print(j, "\t", k)
	
	print("Total\t\t", int(totaltime))


def weekly(listofusers):
	'''
	Just like daily function, suited to focus on week of the year instead of y:m:d
	'''

	datetime= 0
	totaltime = 0
	datelist = []
	daytime = []

	for x in listofusers:
		test = x[1:5]

		del test[2]
		strlist1 = ' '.join(x[0:5])
		strlist2 = ' '.join(x[6:])
		strlist3 = ' '.join(test[0:])

		a = time.mktime(time.strptime(strlist1, "%a %b %d %H:%M:%S %Y"))
		b = time.mktime(time.strptime(strlist2, "%a %b %d %H:%M:%S %Y"))

		timeinsec = time.mktime(time.strptime(strlist3, "%b %d %Y"))
		
		weekoftheyear = time.strftime("%Y %W", time.localtime(timeinsec))
		
		datetime = time.strftime("%Y %m %d", time.localtime(timeinsec))
		totaltime = totaltime + (b - a)
		reducetime = b - a
		
		datelist.append(weekoftheyear)
		daytime.append(int(reducetime))

	rounduplist = []
	sumlist = []
	for t, y in zip(datelist, daytime):
		if t not in rounduplist:
			rounduplist.append(t)
			sumlist.append(y)			
		elif t in rounduplist:
			sumlist[-1] = sumlist[-1] + y

	print("<><><><><><><><><><><><><><>")
	print("Date\t\tUsage in Seconds")
	for j, k in zip(rounduplist, sumlist):
		print(j, "\t", k)

	print("Total\t\t", int(totaltime))

def monthly(listofusers):
	'''
	Just like daily, and weekly function, suited to focus on month of the year instead of the day, or week
	'''

	datetime= 0
	totaltime = 0
	datelist = []
	daytime = []

	for x in listofusers:
		test = x[1:5]

		del test[2]
		strlist1 = ' '.join(x[0:5])
		strlist2 = ' '.join(x[6:])
		strlist3 = ' '.join(test[0:])

		a = time.mktime(time.strptime(strlist1, "%a %b %d %H:%M:%S %Y"))
		b = time.mktime(time.strptime(strlist2, "%a %b %d %H:%M:%S %Y"))

		timeinsec = time.mktime(time.strptime(strlist3, "%b %d %Y"))
		
		weekoftheyr = time.strftime("%Y %m", time.localtime(timeinsec))
		
		datetime = time.strftime("%Y %m %d", time.localtime(timeinsec))
		totaltime = totaltime + (b - a)
		reducetime = b - a
		
		datelist.append(weekoftheyr)
		daytime.append(int(reducetime))

	rounduplist = []
	sumlist = []
	for t, y in zip(datelist, daytime):
		if t not in rounduplist:
			rounduplist.append(t)
			sumlist.append(y)			
		elif t in rounduplist:
			sumlist[-1] = sumlist[-1] + y

	print("<><><><><><><><><><><><><><>")
	print("Date\t\tUsage in Seconds")
	for j, k in zip(rounduplist, sumlist):
		print(j, "\t", k)

	print("Total\t\t", int(totaltime))

def verbose():
	'''
	Prints parts of the verbose
	'''
	print("Files to be processed", args.F)
	print("Type of args for files", type(args.F))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Usage Report based on the last command",epilog="Copyright 2019 - Igor Kossinov")
	parser.add_argument("-l", "--list", type=str, choices=['user','host'], help="generate user name or remote host IP from the given files")
	parser.add_argument("-r", "--rhost", help="usage report for the given remote host IP")
	parser.add_argument("-t","--type", type=str, choices=['daily','weekly','monthly'], help="type of report: daily, weekly, and monthly")
	parser.add_argument("-u", "--user", help="usage report for the given user name")
	parser.add_argument("-v","--verbose", action="store_true",help="turn on output verbosity")
	parser.add_argument("F", nargs = "+", help="list of files to be processed")
	args=parser.parse_args()
	select = sys.argv[2]
	filename = args.F[0]
	loginuser = sys.argv[1]
	
	
	if args.list:
		if args.verbose:
			print("Generating list for", select)
			verbose()
			print("processing usage report for the following:")
			print("reading login/logout record files", args.F)
		print("Generating list for", select)
		list(select, filename)
	elif args.rhost:
		timely = sys.argv[4]
		if args.verbose:
			verbose()
			print("usage report for remote host:", select)
			print("usage report for type:", timely)
			print("processing usage report for the following:")
			print("reading login/logout record files", args.F)
		if timely == "daily":
			print("Daily Usage Report for", select)
			daily(userlisting(select, filename, loginuser))
		elif timely == "weekly":
			print("Weekly Usage Report for", select)
			weekly(userlisting(select, filename, loginuser))
		elif timely == "monthly":
			print("Monthly Usage Report for", select)
			monthly(userlisting(select, filename, loginuser))
	elif args.user:
		timely = sys.argv[4]
		if args.verbose:
			verbose()
			print("usage report for user:", select)
			print("usage report for type:", timely)
			print("processing usage report for the following:")
			print("reading login/logout record files", args.F)
		if timely == "daily":
			print("Daily Usage Report for", select)
			daily(userlisting(select, filename, loginuser))
		elif timely == "weekly":
			print("Weekly Usage Report for", select)
			weekly(userlisting(select, filename, loginuser))
		elif timely == "monthly":
			print("Monthly Usage Report for", select)
			monthly(userlisting(select, filename, loginuser))	