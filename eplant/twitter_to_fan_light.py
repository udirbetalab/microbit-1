#code to comminucate with Arduino with fan, relay and lots of stuff

import tweepy
from tweepy import OAuthHandler
import serial
import time
#import scrollphat


ckey = 'code'
csecret = 'code'
atoken = 'code'
asecret = 'code'

auth = OAuthHandler(ckey, csecret) 
auth.set_access_token(atoken, asecret)
auth.secure = True
api = tweepy.API(auth)
time_sleep = 60

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
#    scrollphat.scroll()
    status = []
    x = 0
    status = api.user_timeline('plantofinternet')
    checkIt = [s.text for s in status]
    drip = checkIt[0].split()
    if drip[0] == '#allon':
        ser.write('1') #49
        print 'All ON'
        time.sleep(time_sleep)
#        scrollphat.write_string("ALL ON ")
    elif drip[0] == '#alloff':
        ser.write('2') #50
        print 'All OFF'
        time.sleep(time_sleep)
    elif drip[0] == '#fanon':
        ser.write('3') #51
        print 'FAN ON'
        time.sleep(time_sleep)
    elif drip[0] == '#fanoff':
        ser.write('4') #52
        print 'FAN OFF'
        time.sleep(time_sleep)
    elif drip[0] == '#ledon':
        ser.write('5') #53
        print 'Led ON'
        time.sleep(time_sleep)
    elif drip[0] == '#ledoff':
        ser.write('6') #54
        print 'Led OFF'
        time.sleep(time_sleep)
    elif drip[0] == '#lighton':
        ser.write('7') #55
        print 'Light ON'
        time.sleep(time_sleep)
    elif drip[0] == '#lightoff':
        ser.write('8') #56
        print 'Light OFF'
        time.sleep(time_sleep)
    elif drip[0] == '#stop':
        ser.write('0')
        print 'STOP and awaiting Tweet instruction'
        time.sleep(time_sleep)
    else:
        ser.write('0')
        print 'Awaiting Tweet instruction'
        time.sleep(time_sleep)
