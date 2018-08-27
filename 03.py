import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
symbol = ["'", '"', ':', ';', '.', ',', '-', '!', '?', "'s"]

document = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
list_of_words = nltk.FreqDist(w.lower() for w in document if w.lower() not in stop_words + symbol)


words = wordpunct_tokenize(document) not in stop_words

# for doc in documents:
#     list_of_words = [i.lower() for i in wordpunct_tokenize(doc) if i.lower() not in stop_words]


print(list_of_words)

