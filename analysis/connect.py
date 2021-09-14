from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import csv
import sys

### key file detection ###
try:
    csvDir = sys.argv[1]
    pass
except:
    print("please enter the key file as an argument")
    print("python3 connect.py <key file>")
    sys.exit("terminated no key detected")

#hardcode key for debug only
csvDir = "/home/gray/git-repo/twitter-key/key.tweet"

#read csv key file
with open(csvDir, mode ='r')as file:
  # reading the CSV file
  tokenList = list(csv.reader(file))

""""Authenticator class"""
class twitterAuth():
    """authenticate to twitter API"""
    def authenticate(self):
        auth = OAuthHandler(tokenList[0][1], tokenList[1][1])
        auth.set_access_token(tokenList[2][1], tokenList[3][1])
        api = API(auth,wait_on_rate_limit=True)
        return(api)

api = twitterAuth().authenticate()

tweets = Cursor(api.search, q=sys.argv[2], lang='id', tweet_mode="extended").items(20)

data = [result.full_text for result in tweets]

[print(x) for x in data]

#something to be added hehe
