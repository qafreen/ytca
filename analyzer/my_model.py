import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import TweetTokenizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle

def init():
    model = None
    try:
        with open('classifier.pickle', 'rb') as f:
            model = pickle.load(f)
    except Exception:
        print('Failed to load model. Training new model..')
        model = train()
    
    return model


#This function converts to lower-case, removes square bracket, removes numbers and punctuation
def text_clean_1(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub("\d+", "", text)
    return text

def tokenizer(text):
    tok = TweetTokenizer()
    return tok.tokenize(text)

def train():
    df = pd.read_csv('./analyzer/FINAL.csv')
    df['cleaned'] = df.comments.apply(text_clean_1)
    X = df.cleaned
    y = df.sentiment

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 225)

    tvec = TfidfVectorizer(tokenizer=tokenizer)

    clf2 = LogisticRegression(solver = "lbfgs", max_iter=200)
    model = Pipeline([('vectorizer', tvec),('classifier',clf2)])
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(confusion_matrix(predictions, y_test))

    print("Accuracy : ", accuracy_score(predictions, y_test))
    print("Precision : ", precision_score(predictions, y_test, average = 'weighted'))
    print("Recall : ", recall_score(predictions, y_test, average = 'weighted'))

    with open('classifier.pickle','wb') as clf:
        pickle.dump(model, clf)

    return model

# example = "hate"
# result = model.predict([text_clean_1(example),])
# print(result)