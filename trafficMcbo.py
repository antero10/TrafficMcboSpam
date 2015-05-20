import tweepy
import json
from models.tweet import TweetModel
class trafficMcbo:
    """ETL for trafficMcbo Twitter Account"""
    def __init__(self):
        self.consumer_key = 'FOEVRW1yTdOarEftWNt03TMcl'
        self.consumer_secret = 'O0qYWqG5rvfjbG9rZdSH3BspcYL2deSaccnIbMuVbykcQGoKRI'
        self.access_token = '79949444-hN4NSBSmefScvvJTqFggi8MnfAwXlXrCSb8cbKi2t'
        self.access_token_secret = 'dstf86FNm1Lg515gwWRaPG3F3PJ404VhWnCbleFkyi4Nu'
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True)
        self.tweetModel = TweetModel()
        
    def initRecolector(self):
        goal = round(5000/200)
        max_id  = None
        while goal > 0:
            tweets = self.api.user_timeline('trafficMcbo',count=200,max_id = max_id)
            for tweet in tweets:
                self.tweetModel.save(tweet)
            max_id = tweets[-1].id
            goal = goal - 1
            print max_id
        print 'Finish!...'

traffic = trafficMcbo()
traffic.initRecolector()