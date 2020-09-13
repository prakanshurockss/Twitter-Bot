# Twitter-Bot
twitter bot can be use to search a particular hastage and repost it automatically
#tweet bot using python and tweepy.
#python and tweepy required.
import tweepy
from time import sleep
import random

#Setup your twitter dev account on https://developer.twitter.com/
#to know more read this blog https://docs.inboundnow.com/guide/create-twitter-application/

CONSUMER_KEY = 'Paste your keys'
CONSUMER_SECRET = 'yyyyyy'
ACCESS_KEY = 'zzzzz'
ACCESS_SECRET = 'zzz'

print('Script started',)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#twitter compares the tweets. multiple tweet can not have same value, so we are going to generate random value an add that to our every tweet.
#generating random number(int).
randomlist = random.sample(range(0, 99), 99)
int = random.choice(randomlist)
print(int)
#intiger value can not be tweeted so
#converting intiger to string.
string = f'{int}'
print('Attempting to Comment.', flush=True)
for status in api.user_timeline():
    #Edit text you want to tweeted.
    #Don't exceed the charector limit (280).
    #items(no.) no. of time you want to tweet
    api.update_status('YOUR TEXT TO BE TWEETED @User_name #Hashtags ' + ' ' + string).items(100)
    print('Comment successful')
    #Read the twitter automaation guidlines, don't get blocked.
    #sleep(60) In second
    sleep(60)
