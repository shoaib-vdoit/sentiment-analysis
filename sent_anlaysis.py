from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download("punkt_tab")

url = "https://www.cnbc.com/2024/09/28/hezbollah-leader-hassan-nasrallah-killed-in-strike-israeli-army-says.html"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)

