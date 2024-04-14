import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List
import nltk


class CorpusProcessor:
    def __init__(self) -> None:
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    # Preprocessing function
    def preprocess_text(self, text):
        # Tokenize text
        tokens = word_tokenize(text)
        
        # Remove punctuation and lowercase
        tokens = [word.lower() for word in tokens if word.isalnum()]
        
        # Remove stopwords
        tokens = [word for word in tokens if word not in self.stop_words]
        
        # Lemmatization
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        
        return tokens

    def create_single_corpus(self, content:List[str]):
        # Create single corpus
        single_corpus = set()
        for doc in content:
            single_corpus.update(self.preprocess_text(doc))
        return single_corpus


