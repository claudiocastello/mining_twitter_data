import tweepy, tt_auth
from tweepy import OAuthHandler
 
consumer_key = tt_auth.c_key
consumer_secret = tt_auth.c_secret
access_token = tt_auth.a_token
access_secret = tt_auth.a_secret


# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 
# api = tweepy.API(auth)