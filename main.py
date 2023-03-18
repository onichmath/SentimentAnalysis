"""
1. Prompt user for hashtag to scrape
With options for amount of data to scrape

2. Scrape data from twitter and store it into ?? file

3. Sentiment analysis on data

4. Display results, options for what to display"""
from web_scraper import WebScraper
from data_process import DataProcess

def main():
   web_scraper = WebScraper()
   #print(web_scraper.tweet_storage)
   polarity = DataProcess().get_polarity(web_scraper.tweet_storage)
   print(polarity)

if __name__ == "__main__":
        main()
