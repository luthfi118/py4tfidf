# py4tfidf

Term Frequency – Inverse Document Frequency (TF-IDF) Python Library

## Getting Started

This project is simply an implementation of TF-IDF algorithm in python programming language.

### Prerequisites

Numpy


### Installing

The easiest way to install py4tfidf is by using pip

```
pip install py4tfidf
```

### Usage
There are 2 public methods of ```Tfidf``` class. It is ```vectorize_train``` and ```vectorize_test```. ```vectorize_train``` used to build the corpus, calculate idf based on training text, and transform it into a usable vector by multiplying its tf and its idf, while ```vectorize_test``` is just simply transforming the test text into a usable vector by multiplying its tf with previously obtained if. Both ```vectorize_train``` and ```vectorize_test``` take 1 argument namely x_train and x_text respectively. Because tokenizing is usually done in the text preprocessing phase, we assume you tokenize your text on your own, so the argument for ```vectorize_train``` and ```vectorize_test``` should be a list of tokenized text.
```
from py4tfidf.vectorizer import Tfidf
vec = Tfidf()
x_train = [['i','love', 'python'],['natrual','language','processing','is','fun'],['python','is','fun']]
x_test = [['python','language','is','fun'],['im','learning','natrual','language','processing']]
x_train = vec.vectorize_train(x_train)
x_test = vec.vectorize_test(x_test)
```
