import serial
import time
import tweepy
import random
import safygiphy
import giphypop
import warnings
from giphypop import translate

warnings.filterwarnings("ignore")

var = 0
count = 0

ser = serial.Serial('/dev/tty.usbmodem1422', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False) # raPI /dev/ttyACM0
ser.flushInput()
ser.flushOutput()

WORDS1 = ("red", "blue", "green", "yellow", "black", "white", "grey", "pink")
WORDS2 = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "drum", "silly", "mad", "happy", "sad")
WORDS3 = ("dog", "cat", "cow", "horse", "pig",  "chinchilla", "elephant", "sheep", "snake")
HASTAG = ("#plantbot","#microbit","#python","#hourofcode"," ", " ", " ", " ", " ")
VERB = ("swim","ride","walk","fly","drink","watch","run","drive","sleep","bath","burn","eat","love")
NOUN = ("cat","car","dog","horse","pig","apple","banana","rosine","bike","bird","book","frog","cow","elephant","xylophone","drum","heart","house",
        "tent","bus","airplaine","snake","mountain","city","river","flower")

COLOUR = ("red","blue","green","yellow","black","white","grey","pink","purple","rainbow")

ADJECTIVE = ("dry","dead","sad","unhappy","badday")          

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = { 
    "consumer_key"        : "code",
    "consumer_secret"     : "code",
    "access_token"        : "code",
    "access_token_secret" : "code" 
    }  

  api = get_api(cfg)
  status = api.update_status(status=tweet)
  print(tweet)
#  time.sleep(10)
  print("Ready for new Tweet!")
  print(" ")
       

try:
  while True:
    data = ser.readline().rstrip()  
    data_s = data.split(":")
    x,y = data_s[0], data_s[1]
    y = int(y)
    if 10 <= y <= 399:
      print("Alert! ")
      count = count + 1
      print(count)
      adj = random.choice(ADJECTIVE)
      img = translate(adj, api_key='dc6zaTOxFJmzC')
      print(img.url)
      print(img.bitly)
      print(adj)
      print(x)
      print(y)
#      tweet = "HELP! @robotgimse " + " I like to " + random.choice(VERB) + " " + adj + " " + random.choice(COLOUR) + " " + random.choice(NOUN) + " " + random.choice(HASTAG) + "  - #chinchilla #giphy"+" ("+adj+")" + " " + img.bitly
      tweet = "HELP! @larsgimse " + " Your E-plant need water! " + random.choice(HASTAG) + +" " + "#giphy ("+adj+")" + " " + img.bitly 
      main()
    elif y > 400:
        print(x)
        print(y)

finally:
    ser.close()
  
