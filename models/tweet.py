import MySQLdb
import re as re
import sys
class TweetModel:
	"""Model for Tweet"""
	def __init__(self):
		try:
			self.connection = MySQLdb.connect('127.0.0.1','gustavo','gusdata','trafficMcbo')
			self.cursor = self.connection.cursor()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0],e.args[1])

	def save(self,status):
		if not self.exist(status):
			sql = "INSERT INTO tweets SET tweet = \'%s\'" % (re.escape(status.text.encode('utf-8')))
			try:
				self.cursor.execute(sql)
				self.connection.commit()
				print 'Tweet saved with text: '+status.text
			except:
				self.connection.rollback()
	def exist(self,status):
		sql = "SELECT COUNT(*) from tweets WHERE tweet = \'%s\' " % (re.escape(status.text.encode('utf-8')))
		self.cursor.execute(sql)
		value = self.cursor.fetchone()[0]
		if value == 0 :
			print 'Tweet: '+status.text+ 'No exist'
			return False
		else :
			print 'Value alredy exist'
			return True

	def get(self):
		sql = "SELECT * FROM tweets"
		self.cursor.execute(sql)
		return self.cursor.fetchall()
