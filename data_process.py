from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from web_scraper import WebScraper
# TODO: pandas instead of dict would make it easier to label with sentiment
# TODO: quit initing classes
class DataProcess:
    def __init__(self):
        self.sent_analyzer = SentimentIntensityAnalyzer()
        self.tweets_polarity_df = self._create_tweet_polarity_df_from_dict(WebScraper().tweet_storage)

    # Converted to df as pandas has easy plotting methods
    def _create_tweet_polarity_df_from_dict(self,tweet_dict):
        #sentiment_dict = {k:[date_tweet[0], date_tweet[1], self.sent_analyzer.polarity_scores(date_tweet[1])]
        #                     for k,date_tweet in tweet_dict.items()}
        tweet_df = pd.DataFrame.from_dict(tweet_dict, orient='index',columns=['Date','Tweet'])
        tweet_df['Date'] = pd.to_datetime(tweet_df['Date'])
        tweet_df['Date'] = tweet_df['Date'].dt.tz_localize(None)
        sentiment_df = self._create_sentiment_df(tweet_dict)
        polarity_df = pd.concat([tweet_df,sentiment_df], axis=1) 
        return polarity_df
    
    def _create_sentiment_df(self,tweet_dict):
        sentiments = []
        for date_tweet in tweet_dict.values():
            sentiments.append(self.sent_analyzer.polarity_scores(date_tweet[1]))
        return pd.DataFrame(sentiments)
        #return pd.DataFrame.from_dict(self.tweets_polarity_df['Sentiment'], orient='column')
        #for key,value in self.tweets_polarity_df['Sentiment'].items():
         #   if key
