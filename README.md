# Quest2keys
**a simple question 2 keywords in french based on pos-tags**

## Install

```pip install .```

Download the spacy model
 ```python -m spacy download fr_core_news_md```

## Usage:
```python
from quest2keys.extract_keywords import SpacyExtractor
SPACY_FILTER_SOFT = ["NOUN","PROPN", "VERB", "X","ADJ", "ADV"]
se = SpacyExtractor(SPACY_FILTER_SOFT, "fr_core_news_md")
se.filter_sent_spacy("Quels sont les moyens d'action du comité d'entreprise?"
>>> moyens action comité entreprise
```