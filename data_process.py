from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from web_scraper import WebScraper
# TODO: pandas instead of dict would make it easier to label with sentiment
# TODO: quit initing classes
class DataProcess:
    def __init__(self):
        self.sent_analyzer = SentimentIntensityAnalyzer()
        self.polarity_df = self._create_polarity_df_from_dict(WebScraper().tweet_storage)

    # Converted to df as pandas has easy plotting methods
    def _create_polarity_df_from_dict(self,tweet_dict):
        sentiment_dict = {k:[date_tweet[0], date_tweet[1], self.sent_analyzer.polarity_scores(date_tweet[1])]
                             for k,date_tweet in tweet_dict.items()}
        polarity_df = pd.DataFrame.from_dict(sentiment_dict, orient='index',columns=['Date','Tweet','Sentiment'])
        polarity_df['Date'] = pd.to_datetime(polarity_df['Date'])
        polarity_df['Date'] = polarity_df['Date'].dt.tz_localize(None)
        return polarity_df

