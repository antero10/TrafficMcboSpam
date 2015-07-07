import pandas as pd
import re
from models.tweet import TweetModel
from sklearn.feature_extraction.text import CountVectorizer

class Spam:

    def __init__(self):
        self.regex = re.compile(ur'via\s+@[a-z]+:\s+')
        self.tweet = TweetModel()
        self.data = self.tweet.get()
        pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier



    def cleanData(self):
        data_frame = pd.DataFrame()
        data_frame['text'] = map(lambda text: text[1].lower().decode('utf-8'),self.data)
        data_frame['text'] = data_frame['text'].str.replace("\\",'')
        data_frame['text'] = data_frame['text'].str.replace(r"^(\s+)?via\s+@\w+:",'')
        data_frame['text'] = data_frame['text'].str.replace(r"@\w+",'')
        data_frame['text'] = data_frame['text'].str.strip()
        data_frame['text'] = data_frame['text'].str.replace(r"(\*|\)|\(|\[|\])",'')
        data_frame['spam'] = map(lambda spam: spam[2] == 1,self.data)
        self.logisticRegression(data_frame[:50])

    def logisticRegression(self,data_frame):
        import statsmodels.api as sm
        train_cols = data_frame.columns[1:]
        logit = sm.Logit(data_frame['spam'],data_frame[train_cols])
        result = logit.fit()
        print result.summary()
        print result.conf_int()

spam = Spam()
spam.cleanData()
