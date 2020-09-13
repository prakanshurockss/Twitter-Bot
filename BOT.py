# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.


import tweepy
from time import sleep

CONSUMER_KEY = 'i73CZaLFIv2iuzUSWwAZ4n3qj'
CONSUMER_SECRET = 'Za4BuBZEL8sGPwKq2kDZsS5vieG8qvH0bdgBWM2OdbjOi5Root'
ACCESS_KEY = '1261021151754682375-WFJgum4dUxrErkxUzLabrGitnYQPgj'
ACCESS_SECRET = 'sBiyzO60LzMwDC7X6x2XaJBRcoPOzxT7JDypbcptHD1Ob'

# change your Twitter application keys, tokens, and secrets


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'
i=0
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

    #q – the search query string
    #item(5) - how many of tweets you want to retweet
    #If you want to search multiple terms then separate it with OR keyword.
    #for single tearm search use q='example'

for tweet in tweepy.Cursor(api.search, q='#akgec OR #AKGEC').items(999):
       
    try:
        print('\nbot by @prakanshu'+ ' ' + tweet.user.screen_name + '.' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')

        sleep(5)
        #sleep(5) - tweet interval (In Second)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
