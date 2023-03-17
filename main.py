"""
1. Prompt user for hashtag to scrape
With options for amount of data to scrape

2. Scrape data from twitter and store it into ?? file

3. Sentiment analysis on data

4. Display results, options for what to display"""
from web_scraper import WebScraper
import data_process as dp

def main():
   tweet_storage = WebScraper()
   print(tweet_storage)

if __name__ == "__main__":
        main()
