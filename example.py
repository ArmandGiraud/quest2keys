from quest2keys.extract_keywords import SpacyExtractor

SPACY_FILTER_SOFT = ["NOUN","PROPN", "VERB", "X","ADJ", "ADV"]

se = SpacyExtractor(SPACY_FILTER_SOFT, "fr_core_news_md")
res = se.filter_sent_spacy("Quels sont les moyens d'action du comité d'entreprise?")
assert res == "moyens action comité entreprise", "build failed..."