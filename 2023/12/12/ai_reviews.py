from textblob import TextBlob

wiki = TextBlob("yay")
print(wiki.tags)
print(wiki.noun_phrases)
print(wiki.sentiment)
print(wiki.sentiment.polarity)

words = zen.words

for word in len(words):
    print(word.sentiment)