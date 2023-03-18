from nltk.sentiment.vader import SentimentIntensityAnalyzer
# TODO: pandas instead of dict would make it easier to label with sentiment
# TODO: quit initing classes
class DataProcess:
    def __init__(self):
        self.sent_analyzer = SentimentIntensityAnalyzer()

    def get_polarity_df(self,tweets_storage):
        tweets_sentiment = {k:[tweet,self.sent_analyzer.polarity_scores(tweet)]
                             for k,tweet in tweets_storage.items()}
        return tweets_sentiment

