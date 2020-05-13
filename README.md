# py4tfidf

Term Frequency–Inverse Document Frequency (TF-IDF) Python Library

## Getting Started

This project is simply implementation of TF-IDF algorithm in python programming language.

### Prerequisites

Numpy


### Installing

The easiest way to install py4tfidf is using pip

```
pip install py4tfidf
```

### Usage
There is 2 public method of tfidf class. It is vectorize_train and vectorize_test. vectorize_train used to build the corpus, calculate idf based on training text, and transform it into usable vector by multiplying it's tf and it's idf, while vectorize_test is just simply transforming the test text into usable vector by multiplying it's tf with previously obtained idf. vectorize_train and vectorize_test takes 1 argument namely x_train and x_text respectively. Because tokenizing is usually done in text preprocessing phase, we assume you tokenize your text by your own, so the argument for vectorize_train and vectorize_test should be list of tokenized text.
```
from py4tfidf.vectorizer import tfidf
vec = tfidf()
x_train = [['i','love', 'python'],['natrual','language','processing','is','fun'],['python','is','fun']]
x_test = [['python','language','is','fun'],['im','learning','natrual','language','processing']]
x_train = vec.vectorize_train(x_train)
x_test = vec.vectorize_test(x_test)
```
