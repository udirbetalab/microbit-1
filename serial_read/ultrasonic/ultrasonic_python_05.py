import serial
import time
import tweepy
import random

var = 0
count = 0

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()


WORDS2 = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "drum", "silly", "mad", "happy", "sad")
WORDS3 = ("dog", "cat", "cow", "horse", "pig",  "chinchilla", "elephant", "sheep", "snake")
WORDS1 = ("red", "blue", "green", "yellow", "black", "white", "grey", "pink")
HASTAG = ("#animal",
          "#love",
          "#peace",
          "#twitter",
          "#norway",
          "#chillabot",
          "#yolo",
          "#fun",
          "#happy",
          "#raisin",)

VERB = ("swim",
        "ride",
        "walk",
        "fly",
        "drink",
        "watch",
        "run",
        "drive",
        "sleep",
        "bath",
        "burn",
        "eat",
        "love")

NOUN = ("cat",
        "car",
        "dog",
        "horse",
        "pig",
        "apple",
        "banana",
        "rosine",
        "bike",
        "bird",
        "book",
        "frog",
        "cow",
        "elephant",
        "xylophone",
        "drum",
        "heart")

COLOUR = ("red",
          "blue",
          "green",
          "yellow",
          "black",
          "white",
          "grey",
          "pink")

ADJECTIVE = ("angry",
            "clumsy",
            "jealous",
            "lazy",
            "scary",
            "fat",
            "huge",
            "little",
            "skinny",
            "happy",
            "kind",
            "silly",
            "clean",
            "beautiful",
            "elegant",
            "fancy")
          
          

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "your code",
    "consumer_secret"     : "your code",
    "access_token"        : "your code",
    "access_token_secret" : "your code" 
    }  

  api = get_api(cfg)
  status = api.update_status(status=tweet)
  print(tweet)
  time.sleep(600)
       

try:
  while True:
    data = ser.readline().rstrip()  
    data_s = data.split(":")
    x,y = data_s[0], data_s[1]
    y = int(y)
    if 3 <= y <= 25:
      print("Alert! ")
      count = count + 1
      print(count)
#      tweet = random.choice(WORDS1) + " " + random.choice(WORDS2) + " " + random.choice(WORDS3) + " " + random.choice(HASTAG) + " - Random tweet from Aragorn Chinchilla #chinchilla #microbit #python"
      tweet = "I like to " + random.choice(VERB) + " " + random.choice(ADJECTIVE) + " " + random.choice(COLOUR) + " " + random.choice(NOUN) + " " + random.choice(HASTAG) + "  - Random tweet from Aragorn Chinchilla #chinchilla #microbit #python"
      main()

finally:
    ser.close()
  
