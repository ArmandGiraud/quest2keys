#!/usr/bin/env python

"""Code takes a question string as input,
output a string list of keywords.
"""

__author__ = "Armand Giraud"
__license__ = "Apache"
__version__ = "1.0.1"
__maintainer__ = "Armand Giraud"
__email__ = "armand.giraud.ag@gmail.com"
__status__ = "Dev"

## using spacy as a dependency: requires spacy 2.0 and fr_core_news_sm model

import spacy
import re

#https://spacy.io/api/annotation

SPACY_FILTER_HARD = ["NOUN", "PROPN", "VERB", "X"]
SPACY_FILTER_SOFT = ["NOUN", "PROPN", "VERB", "X", "ADJ", "ADV"]

REGEX_ARTICLE = re.compile(u"(?:R|L|D)\d{1,4}(?:-\d{1,2})?(?:-\d{1,2})?") 
# see https://regex101.com/r/ewzrsG/1

def has_article(string):
    if re.search(REGEX_ARTICLE, string):
        return True
    else:
        return False


class SpacyExtractor():
    """class for extracting keywords using spacy"""

    def __init__(self, filt, model_name):
        self.filt = filt
        self.model_name = model_name

        self.load_model()


    def load_model(self):
        """utility to load spacy trained model"""
        try:
            self.loader = spacy.load(self.model_name, disable  = ['parser', 'ner'])
        except FileNotFoundError as e:
            print("Model {} not found\nplease try $python -m spacy download {}"\
                .format(self.model_name, self.model_name))
            print(e)

    def filter_sent_spacy(self, sent):
        """filter input string based on tags in filters"""
        assert type(sent) == str, "sent input should be string"
        
        if has_article(sent):
            return sent
        
        doc = self.loader(sent)
        return " ".join([tok.text for tok in doc if tok.pos_ in self.filt]).strip()

def main():
    "pass"
    pass

if __name__ == '__main__':
    main()
