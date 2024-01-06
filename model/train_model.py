from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
nltk.download('wordnet')

# Loada o X com todas as 2000 reviews, e coloca no Y as categorias target (no sistema de pasta atual, neg e pos). O y é uma array
# numpy com 2000 items que são 0s e 1s porque o load_files add um numero pra cada categoria (nesse caso, neg e pos)
movie_data = load_files('assets/movie-reviews')
X, y = movie_data.data, movie_data.target

# Text preprocessing
documents = []


stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # remove special characters
    document = re.sub(r'\W', ' ', str(X[sen]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # substituting multiple spaces to single spaces
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # converting to lowercase
    document = document.lower()

    # lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)

    documents.append(document)

# Bag of words

vectorizer = CountVectorizer(
    max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()

# TF-IDF
# calculo Term Frequency
# Term Frequency = (Number of occurrences of a word)/(Total words in the document)
# calculo Inverse Document Frequency
# IDF(word) = Log((Total number of documents)/(Number of documents containing the word))
# o valor TF-IDF de um palavra vai ser alto em um documento se a frequencia dela é alta naquele doc especifico mas baixa em todos os documentos.

# converter valores do BoW para TF-IDF

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

# training and testing

# divides data into 20% test set and 80% training set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)


classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)


# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

import joblib

