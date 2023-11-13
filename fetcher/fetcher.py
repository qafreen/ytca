import os
from os.path import join
import json
import googleapiclient.discovery
from dotenv import load_dotenv

load_dotenv()
DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

print(DEVELOPER_KEY)
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

def fetch(videoId): #returns list of 100 relevant comments

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        order="relevance",
        videoId=videoId
    )

    response = request.execute()
    
    commentList = []
    for item in response['items']:
        commentText = item['snippet']['topLevelComment']['snippet']['textOriginal']
        commentList.append(commentText)
    
    return commentList


#print(fetch('i1aKpceiIcY'))