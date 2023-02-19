# %%
# Import Modules
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pickle
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import style

# List declarative elements
parser = 'html.parser'
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Aquire Data
article_page = requests.get('https://web.archive.org/web/20210327165005/https://hackaday.com/2021/03/22/how-laser-headlights-work/')
article_html = article_page.text

with open('laser_headlights.pkl', 'wb') as f:
    pickle.dump(article_page.text, f)

with open('laser_headlights.pkl', 'rb') as f:
    article_html = pickle.load(f)

soup = BeautifulSoup(article_html, parser)

article_element = soup.find('article')
article_text = article_element.get_text()
doc = nlp(article_text.lower())

# %%
# Import data
sentences = list(doc.sents)

# Find Tokens
def trim_extra(token):
    return not (token.is_space or token.is_punct or token.is_stop)

interesting_token = [token for token in doc if trim_extra(token)]
token_freq = Counter(interesting_token)
interesting_lemmas = [token.lemma_.lower() for token in doc if trim_extra(token)]
lemma_freq = Counter(interesting_lemmas)

# Pick most common
top_tok = set()
for tok, freq in token_freq.most_common(5):
    top_tok.add(tok)

top_lem = set()
for lem, freq in lemma_freq.most_common(5):
    top_lem.add(lem)

# Seperate paragraph into lines
for sentence in sentences:
    count = 0
    for token in sentence:
        if token.lemma_.lower() in interesting_lemmas:
            count += 1
    sent_str = str(sentence).replace('\n','').replace('  ',' ')
    #print(count,':', sent_str)

sentence = sentences[6]
print(sentence)

def score_sentence_by_token(sentence, interesting_tokens):
    # Word Count
    count = 0
    for token in sentence:
        if not (token.is_space or token.is_punct):
            count += 1
    
    # Word occurrence count
    # occurrence = 0
    occurrence =  len([i for i in interesting_tokens if i in sentence ])
    
    # Calculation
    result = occurrence / count
    return result, count, occurrence

def score_sentence_by_lemma(sentence, interesting_lemmas):
    # Word Count
    count = 0
    for token in sentence:
        if not (token.is_space or token.is_punct):
            count += 1
    
    # Word occurrence count
    lemcount = 0
    for token in sentence:
        if token.lemma_.lower() in top_lem:
            lemcount += 1
    
    # Calculation
    result = lemcount / count
    return result, count, lemcount

result_token = score_sentence_by_token(sentence, interesting_token)
result_lemma = score_sentence_by_lemma(sentence, interesting_lemmas)

score_token = result_token[0]
score_lemma = result_lemma[0]

# print(sentence)
print(f'\nSentences By Tokens: \nOccurrence of tokens in sentence: {result_token[2]} \nWord count of sentence: {result_token[1]} \nDivided Results: {round(result_token[0], 4)}')
print(f'\nSentences By Lemmas: \nOccurrence of lemmas in sentence: {result_lemma[2]} \nWord count of sentence: {result_lemma[1]} \nDivided Results: {round(result_lemma[0], 4)}')

# %%



