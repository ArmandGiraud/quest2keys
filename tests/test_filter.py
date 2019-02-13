"""simple tests for extract_keyword module"""
from ..quest2keys.extract_keywords import SpacyExtractor


SPACY_FILTER_HARD = ["NOUN", "PROPN", "VERB", "X"]
SPACY_FILTER_SOFT = ["NOUN", "PROPN", "VERB", "X", "ADJ", "ADV"]
ss = SpacyExtractor(SPACY_FILTER_SOFT, "fr_core_news_md")
sh = SpacyExtractor(SPACY_FILTER_SOFT, "fr_core_news_md")



def test_soft():
    """test soft filter"""
    test_string = "j'ai eu un accident du travail, je souhaite connaitre mes droits"
    string = ss.filter_sent_spacy(test_string)
    answer = 'eu accident travail souhaite connaitre droits'
    assert string == answer

def test_hard():
    """test hard filters"""
    test_string = "j'ai eu un accident du travail, je souhaite connaitre mes différents droits"
    string = sh.filter_sent_spacy(test_string)
    answer = 'eu accident travail souhaite connaitre droits'
    assert string == answer
