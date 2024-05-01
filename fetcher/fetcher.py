import os
from os.path import join
import json
import googleapiclient.discovery
from dotenv import load_dotenv

load_dotenv()
DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

def fetch(videoId,order): #returns list of 100 relevant comments

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        order=order,
        videoId=videoId
    )

    response = request.execute()
    commentList = []
    for item in response['items']:
        commentText = item['snippet']['topLevelComment']['snippet']['textOriginal']
        commentList.append(commentText)
    
    return commentList

def getPopularVideos(): 
    request = youtube.videos().list(
        part="id",
        chart="mostPopular",
        maxResults=10
    )
    response = request.execute()
    trending_videos = []
    for item in response['items']:
        video_id = item['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        trending_videos.append(video_url)

    return trending_videos
    
    


#print(fetch('i1aKpceiIcY'))
#print(getPopularVideos())