
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.data import Sentence
from flair.nn import Classifier
from . import my_model

model = my_model.init()

tagger = Classifier.load('sentiment')

vaderAnalyzer = SentimentIntensityAnalyzer()

def analyze(commentList, model):
    polarity = list(map(model, commentList))
    return polarity

def vaderModel(comment):
    return vaderAnalyzer.polarity_scores(comment)['compound']

def flairModel(comment):
    sentence = Sentence(comment)
    tagger.predict(sentence)
    return 1 if str(sentence).split(' ')[-2] == "POSITIVE" else -1 

def textBlobModel(comment):
    return TextBlob(comment).sentiment.polarity


def use_custom_model(comment_list):
    return list(model.predict(comment_list))

def do_mafs(polarities):
    negative_thresh = -0.1
    positive_thresh = 0.1
    
    count_p = count_n = count_ne = 0
    
    n = len(polarities)
    
    for polarity in polarities:
        if polarity <= negative_thresh:
            count_n += 1
        elif polarity > negative_thresh and polarity < positive_thresh:
            count_ne += 1
        else:
            count_p += 1
    
    return {'positive': round((count_p/n) * 100,2),'neutral': round((count_ne/n)*100,2), 'negative':round((count_n/100)*n,2)}



# commentList = ['this is great',"i don't like it",'i am sam']
# p = list(model.predict(commentList))
# print(do_mafs(p))






