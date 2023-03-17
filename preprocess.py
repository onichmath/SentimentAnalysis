from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
#import SpellCheck

class Preproccessor:
    # r'@([A-Za-z0-9_]+)|(\w+\S+\w+)'
    def __init__(self):
        self._regex_tokenizer = RegexpTokenizer(r'\w+')
        self._lemmatizer = WordNetLemmatizer()
        self._reg_whitespace = re.compile(r'\s+')
        self._reg_user_website = re.compile(r'@\S+|http\S+')

    def _rm_whitespace(self,tweet_content:str):
        pass

    def _spell_check(self,tweet_content:str):
        pass

    # TODO: REMOVE @USERS
    def preprocess(self,tweet_content: str):
        tweet_content = tweet_content.lower()
        tweet_content = re.sub(self._reg_user_website,'',tweet_content)
        tokens = self._regex_tokenizer.tokenize(tweet_content)
        lcase_nopunc_tokens = [token.strip() for token in tokens if token not in list(stopwords.words('english'))]
        lemmatized_words = [self._lemmatizer.lemmatize(token) for token in lcase_nopunc_tokens] 
        return lemmatized_words
