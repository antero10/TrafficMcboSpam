import pandas as pd
import re
from nltk.corpus import stopwords
class Spam:

    def __init__(self):
        self.data_frame = pd.read_csv("tweets.csv", header=0)
    def clean_data(self):

        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.only_text)
        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.to_lower)
        self.data_frame['tweet'] = self.data_frame['tweet'].apply(self.remove_stop_words)
        

    def only_text(self,text):
        return re.sub("[^a-zA-Z]"," ",text)

    def to_lower(self,text):
        return text.lower()


    def remove_stop_words(self,text):
        return [w for w in text.split() if not w in stopwords.words('spanish')]



spam = Spam()
spam.clean_data()
