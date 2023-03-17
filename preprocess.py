from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from spellchecker import SpellChecker

# TODO: Chunking
class Preproccessor:
    # r'@([A-Za-z0-9_]+)|(\w+\S+\w+)'
    # Spellchecker is default distance 2, may lag on longer words
    # Initialize with distance of 1 if it slows down
    def __init__(self):
        self._regex_tokenizer = RegexpTokenizer(r'\w+')
        self._lemmatizer = WordNetLemmatizer()
        self._reg_whitespace = re.compile(r'\s+')
        self._reg_user_website = re.compile(r'@\S+|http\S+')
        self._spell_checker = SpellChecker()

    def _rm_whitespace(self,tweet_content:str):
        pass

    def _spell_check(self,tweet_content):
        for word in tweet_content:
            self._spell_checker.correction(word)
        return tweet_content
    
    # Specific preprocessing for Vader model, as vader does not require tokenizing/lcasing/etc
    def vader_preprocess(self,tweet_content:str):
        tweet_content = re.sub(self._reg_user_website,'',tweet_content)
        tweet_content = self._spell_check(tweet_content)
        return tweet_content

        # TODO: REMOVE @USERS
    def tokenize_preprocess(self,tweet_content: str):
        tweet_content = tweet_content.lower()
        tweet_content = re.sub(self._reg_user_website,'',tweet_content)
        tokens = self._regex_tokenizer.tokenize(tweet_content)
        lcase_nopunc_tokens = [token.strip() for token in tokens if token not in list(stopwords.words('english'))]
        spellchecked_tokens = self._spell_check(lcase_nopunc_tokens)
        lemmatized_words = [self._lemmatizer.lemmatize(token) for token in spellchecked_tokens] 
        return lemmatized_words
