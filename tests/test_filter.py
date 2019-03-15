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

def test_regex():
    string = "Section 1 : Missions Articles L7234-1 à D7234-2 R234-34-9 de la des comment quand"
    out_string = ss.filter_sent_spacy(string)
    assert out_string == string



if __name__ == "__main__":
    test_regex()
    test_hard()
    test_soft()

