from pymongo import MongoClient
import json
class TweetModel:
	"""Model for Tweet"""
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client.trafficMcbo
		self.collection = self.db.tweets
		
	def save(self,tweet):
		self.collection.save(tweet._json)
		print 'Saved Success with id : ' + str(tweet.id)