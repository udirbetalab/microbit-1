import serial
import tweepy
import random


PORT = "/dev/tty.usbmodem1422"
count = 0
WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
WORDS2 = ("dog", "cat", "cow", "horse", "pig",  "chinchilla")

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "xx",
    "consumer_secret"     : "xx",
    "access_token"        : "xx",
    "access_token_secret" : "xx" 
    }

  api = get_api(cfg)
#  tweet = random.choice('abcdefghij')
#  tweet = random.sample(["dog", "cat", "pig", "cow", "horse", "giraff", "elephant", "sheep", "bird"], 4)
#    tweet = random.randint(1000, 10000)
  status = api.update_status(status=tweet)
#tweet = word
  print(tweet)
#  print(word)
  

try:
    while True:
        #read a line from the microbit, decode it and
        # strip the whitespace at the end
        data = s.readline().rstrip()

        #split the accelerometer data into x, y, z
        data_s = data.split(" ")
        a, b, p = data_s[0], data_s[1], data_s[2]
        x, y, z = data_s[3], data_s[4], data_s[5]
#        twitter = data_s[0]
#        print(a,b,p,x,y,z)
#        print(data_s[0])
        if (data_s[0] == "True" ):
            print("You push A button")
            count = count + 1
            print(count)
            tweet = "Twitter from micro:bit: " + random.choice(WORDS) + " " + random.choice(WORDS2)
            main()
            
        elif (data_s[1] == "True" ):
            count = 0
            print("You push B button")
            print("Count to zero")
#            print(tweet)
#        elif (data_s[0] == "False" ): print("Nooo!")
finally:
    s.close()
