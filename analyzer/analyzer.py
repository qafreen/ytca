
from textblob import TextBlob

def analyze(commentList, model):
    polarity = list(map(model, commentList))
    return polarity


def textBlobModel(comment):
    return TextBlob(comment).sentiment.polarity

def do_mafs(polarities):
    negative_thresh = -0.2
    positive_thresh = 0.2
    
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
# p = analyze(commentList,model)
#print(do_mafs(p))






