from TwitterAPI import TwitterAPI


#TRACK_TERM = ' @potus'
#TRACK_TERM2 = '@potus'
sok1 = '#romforlek'
sok2 = ''
antallTweet = 1

from auth_romforlek import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)



api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret)

#r = api.request('statuses/filter', {'track': TRACK_TERM})

#for item in r:
#    print(item['text'] if 'text' in item else item)

for item in api.request('search/tweets', {'q': sok1 + ' ' + sok2, 'count': antallTweet}):
#            print(item['text'] if 'text' in item else item)
            print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')
            print " "
            tweet = item['text'].encode('utf-8')
            print tweet.split()

            if '#servo90' in tweet.split():
                print 'servo90'
            elif '#servo180' in tweet.split():
                print 'servo180'
#           elif 
#            if tweet.find('sded'):
#                print 'Servo to 013 degree'
#            elif tweet.find('def'):
#                print 'Servo to 90 degree'
#            elif tweet.find('#servo180'):
#                print 'Servo to 180 degree'
            
