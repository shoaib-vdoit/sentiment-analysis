from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download("punkt_tab")

url = "https://www.cnbc.com/2024/10/23/tokyo-metro-shares-gain-40percent-on-debut-after-japans-largest-ipo-in-six-years-.html"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)

