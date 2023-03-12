# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
i = 0
# TODO: numpy list
search_phrase = input("Phrase to search: ")
tweet_generator = sn.TwitterSearchScraper(search_phrase).get_items()
for i,v in enumerate(tweet_generator):
    if (v.lang == 'en'):
        print(v.renderedContent)
        i += 1
    if (i > 9):
        break
