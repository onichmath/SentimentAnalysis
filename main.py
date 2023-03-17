"""
1. Prompt user for hashtag to scrape
With options for amount of data to scrape

2. Scrape data from twitter and store it into ?? file

3. Sentiment analysis on data

4. Display results, options for what to display"""
import web_scraper as ws
import data_process as dp

def main():
    search_phrase = ws._search_string()
    tweet_generator = ws._create_generator(search_phrase)
    tweet_dataframe = ws._create_tweet_dataframe(tweet_generator,int(input("Tweets to store: ")))
    print(tweet_dataframe.to_string())

if __name__ == "__main__":
        main()
