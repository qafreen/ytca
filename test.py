from fetcher import fetcher
from analyzer import analyzer
 

commentList = fetcher.fetch('YbJOTdZBX1g') #youtube rewind 2018 https://www.youtube.com/watch?v=YbJOTdZBX1g&ab_channel=YouTube
polarities = analyzer.analyze(commentList,analyzer.textBlobModel)

negative_thresh = -0.2
positive_thresh = 0.2

for i,polarity in enumerate(polarities):
    if polarity <= negative_thresh:
        print(i,commentList[i])
        print()

    # elif polarity > negative_thresh and polarity < positive_thresh:
    #     count_ne += 1
    # else:
    #     count_p += 1

print()
print(analyzer.do_mafs(polarities))
print()