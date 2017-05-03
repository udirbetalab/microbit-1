# -*- coding: utf-8 -*-

import time
from time import sleep
from TwitterAPI import TwitterAPI
import struct
import os
from serial import Serial
import httplib
from httplib import IncompleteRead

availableMicrobit = True
testSerial = False
microbitPort = '/dev/tty.usbmodem40132'
microbitBaud = '115200'
microbitWaitTime = 1
stringToTrack = '#testing1234'

from auth_romforlek import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


os.system('cls' if os.name == 'nt' else 'clear')

print "Initialising Twitter Stream Application"

print "Initialisation OK!"

print 'Initialising micro:bit Board through Serial'


if availableMicrobit:
	ser = Serial(microbitPort, microbitBaud, timeout=3)


sleep(microbitWaitTime)


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

		api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

		print "Initialisation OK!"
		print 'Twitter Stream Request running'
		print '---'


		r = api.request('statuses/filter', {'track':stringToTrack})


		for item in r.get_iterator():
			if 'text' in item:
				print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')


				tweet = item['text'].encode('utf-8')
				tweet2 = tweet.split(stringToTrack)
				tweetUten = tweet2[0]
				if availableMicrobit:

					ser.write(tweetUten + '\r\n')

					print "micro:bit turning on and show: " + tweetUten

					print '---'
					sleep(microbitWaitTime)

	except IncompleteRead:

		print "IncompleteRead occurred"
	except KeyboardInterrupt:

		api.disconnect()
		exit()
