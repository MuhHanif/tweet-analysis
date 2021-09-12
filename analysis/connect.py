import tweepy as tp
from textblob import TextBlob as blob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


### this is code snippet directly from tweepy docs ###
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



#something to be added hehe
