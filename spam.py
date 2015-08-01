import pandas as pd
import re
from nltk.corpus import stopwords
class Spam:

    def __init__(self):
        self.data_frame = pd.read_csv("tweets.csv", header=0)
        self.stops = set(stopwords.words("spanish"))
    def clean_data(self):

        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.only_text)
        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.to_lower)
        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.remove_stop_words)
        return self.data_frame

    def only_text(self,text):
        return re.sub("[^a-zA-Z]|via|(http:\/\/\w+.+?\w+\/?\w+?)"," ",text)

    def to_lower(self,text):
        return text.lower()

    def remove_stop_words(self,text):
        return [w for w in text.split() if not w in self.stops]



spam = Spam()
spam.clean_data()
