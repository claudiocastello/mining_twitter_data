import tweepy, config
from tweepy import OAuthHandler
 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

status = tweepy.Cursor(api.home_timeline).items(10)