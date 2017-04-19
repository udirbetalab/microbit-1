# -*- coding: utf-8 -*-
# Author: Nicholas Bester (Arduino)
# reAuthor to micro:bit: Lars Gisme
# Title: Twitter Stream connection with micro:bit
# Description: Tracks a string using the Twitter API and sends a Serial command to an micro:bit once a Tweet matching the tracked string is found


# imports
import time
from time import sleep
from TwitterAPI import TwitterAPI
import struct
import os
from serial import Serial
import httplib
from httplib import IncompleteRead

# Pretty console colours
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Variables
availableMicrobit = True # Debugging without an micro:bit
testSerial = False # Debugging without Twitter connection
microbitPort = '/dev/tty.usbmodem40132' # USB port address for the micro:bit /dev/tty.usbmodem1412
microbitBaud = '115200' # Baud for serial communication
microbitWaitTime = 1 # The length of time Python wait before attemping to issue commands to the micro:bit
stringToTrack = "#romforlek" # Change this to the search term you wish to track from Twitter

# Access requirements for Twitter API connection
access_token = '822342768500637696-6LMVbXAqaNhgGjVs5xswIs8ehNAKma1'
access_token_secret = '315m85HOWxX85FCLXUFVYKCHH2iSp7o57L6Y8fhGgJhmn'
consumer_key = 'KF0sDbUfANTAMoQS3iikioPJk'
consumer_secret = 'T8ca055KeHaU0BrHQjKt4k56jSzRNqPMnNAokres6IhVTlheCG'

# Clearing the screen for aesthetic display of console statements
os.system('cls' if os.name == 'nt' else 'clear')

print "Initialising Twitter Stream Application"

print "Initialisation OK!"

print 'Initialising micro:bit Board through Serial'

# micro:bit serial communication
if availableMicrobit:
	ser = Serial(microbitPort, microbitBaud, timeout=3)

# Gives the micro:bit board time to initialise
sleep(microbitWaitTime)

# Testing serial send to micro:bit (ensure available micro:bit is True)
if testSerial:
	print "Send to micro:bit"
	ser.write('Hello' + '\r\n')
	sleep(microbitWaitTime)
	sleep(10)
	ser.write('World' + '\r\n')
	sleep(microbitWaitTime)

else:
	print "Initialisation OK!"
	print 'Initialising Twitter Stream API Authorisation'
	try:
		# Setting up a connection to Twitter using the Twitter API
		api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

		print "Initialisation OK!"
		print 'Twitter Stream Request running'

		# A request object which opens a stream to Twitter tracking the hashtag in question
		r = api.request('statuses/filter', {'track':stringToTrack})

		# Checks if text within the stream item is populated and issues a command to the micro:bit
		for item in r.get_iterator():
			if 'text' in item:
				print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')# Print screen name and the tweet text

				# It is possible to check the tweets for further commands using regular expressions to send multiple commands to the micro:bit
				
				if availableMicrobit:
					print "micro:bit turning on and show tweet with " + stringToTrack
					#ser.write(bytes(1)) # The command is a simple byte intepretation of the integer 1
					ser.write(item['text'].encode('utf-8'))
					sleep(microbitWaitTime) # Wait before sending next command
					#ser.write(bytes(0))
					#sleep(microbitWaitTime) # Wait before sending next command
	except IncompleteRead:
		# Oh well, reconnect and keep trucking
		print "IncompleteRead occurred"
	except KeyboardInterrupt:
		# Or however you want to exit this loop
		api.disconnect()
		exit()
