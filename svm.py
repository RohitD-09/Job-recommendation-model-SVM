# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m5S-ULxxX1j24hKtjEzMBCvNnKIL8Y0G
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

data = pd.read_csv('naukri.csv')

data = data.dropna()

data.reset_index(drop=True)

data['Job Title'] = data['Job Title'].fillna('')

data['Job Experience Required'] = data['Job Experience Required'].fillna('')

data['Key Skills'] = data['Key Skills'].fillna('')

data['Location'] = data['Location'].fillna('')

data['Industry'] = data['Industry'].fillna('')

data['Role'] = data['Role'].fillna('')

import re
data['Key Skills'] = data['Key Skills'].apply(lambda x: re.sub('[^a-zA-Z0-9\s]', '', x)) # remove special characters
data['Location'] = data['Location'].apply(lambda x: re.sub('[^a-zA-Z0-9\s]', '', x)) # remove special characters
data['Industry'] = data['Industry'].apply(lambda x: re.sub('[^a-zA-Z0-9\s]', '', x))
data['Role'] = data['Role'].apply(lambda x: re.sub('[^a-zA-Z0-9\s]', '', x))

data['Key Skills'] = data['Key Skills'].apply(lambda x: x.lower()) # convert to lowercase
data['Location'] = data['Location'].apply(lambda x: x.lower())
data['Industry'] = data['Industry'].apply(lambda x: x.lower())
data['Role'] = data['Role'].apply(lambda x: x.lower())

X = data[['Key Skills','Location', 'Industry', 'Role']]
y = data['Job Title']

vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
X_tfidf = vectorizer.fit_transform(X.apply(lambda x: ' '.join(x), axis=1))

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

svm = LinearSVC(random_state=42)

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

accuracy = svm.score(X_test, y_test)
print('Accuracy:', accuracy)

from sklearn.metrics import f1_score
f1score = f1_score(y_test, y_pred, average='weighted')
print(f'F1-score: {f1score}')

new_soundbite = pd.DataFrame({'Key Skills': ['media planning'],
                              'Location': ['mumbai'],
                              'Industry': ['advertising'],
                              'Role': ['manager']})
new_soundbite_tfidf = vectorizer.transform(new_soundbite.apply(lambda x: ' '.join(x), axis=1))
predictions = svm.decision_function(new_soundbite_tfidf)[0]
top_5_careers = predictions.argsort()[::-1][:5]
print('Top 5 careers:', [svm.classes_[i] for i in top_5_careers])

