from flask import Flask
from flask import request


from quest2keys.extract_keywords import SpacyExtractor
# load model
print("loading model...")
SPACY_FILTER_HARD = ["NOUN","PROPN", "VERB", "X"]
SPACY_FILTER_SOFT = ["NOUN","PROPN", "VERB", "X","ADJ", "ADV"]
se = SpacyExtractor(SPACY_FILTER_SOFT, "fr_core_news_md")

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello there !'

@app.route('/api/words', methods=['GET', 'POST'])
def words():
    if request.method == 'POST':
        responses = {}
        keys = se.filter_sent_spacy(request.form["data"])
        responses["keywords"] = keys
        return  responses

if __name__ == "__main__":
    app.run(debug=True)
