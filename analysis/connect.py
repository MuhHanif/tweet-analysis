import tweepy
from textblob import TextBlob as blob
import csv
#import pandas as pd
#import numpy as np
#import re
#import matplotlib.pyplot as plt

#read the key from my csv files
csvDir = input("enter csv dir: ")
#hardcode key for debug only
csvDir = "/home/gray/git-repo/twitter-key/key.tweet"

with open(csvDir, mode ='r')as file:
  # reading the CSV file
  tokenList = list(csv.reader(file))

### this is code snippet directly from tweepy docs ###
auth = tweepy.OAuthHandler(tokenList[0][1], tokenList[1][1])
auth.set_access_token(tokenList[2][1], tokenList[3][1])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



#something to be added hehe
