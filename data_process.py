from nltk.sentiment.vader import SentimentIntensityAnalyzer

# TODO: pandas instead of dict would make it easier to label with sentiment
class DataProcess:
    def __init__(self):
        self.sent_analyzer = SentimentIntensityAnalyzer()

    def get_polarity(self,tweets_storage):
        sentiment = {(i,self.sent_analyzer.polarity_scores(tweet)) for i,tweet in tweets_storage}
        return sentiment

