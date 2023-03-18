from nltk.sentiment.vader import SentimentIntensityAnalyzer
# TODO: pandas instead of dict would make it easier to label with sentiment
# TODO: quit initing classes
class DataProcess:
    def __init__(self):
        self.sent_analyzer = SentimentIntensityAnalyzer()

    def get_polarity(self,tweets_storage):
        tweets_sentiment = {k:[date_tweet[0], date_tweet[1], self.sent_analyzer.polarity_scores(date_tweet[1])]
                             for k,date_tweet in tweets_storage.items()}
        return tweets_sentiment

