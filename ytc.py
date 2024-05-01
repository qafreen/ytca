from fastapi import FastAPI, Form, Query
from typing import Annotated
from urllib.parse import urlparse, parse_qs
from fastapi.middleware.cors import CORSMiddleware
import fetcher
import analyzer

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sentiment")
async def sentiment(URL: str = Query(...,title="User Input",description="Input String")):
    parse_result = urlparse(URL)
    final = parse_qs(parse_result.query)
    vid = final['v'][0]
    comment = fetcher.fetch(vid,"time")# relevance or time
    polarities = analyzer.analyze(comment, analyzer.vaderModel)
    result = analyzer.do_mafs(polarities)
    return{
        "Video Id": vid,
        "Result": result
    }

@app.get("/PopularVideos")
async def popularVideos():
    u=fetcher.getPopularVideos()
    print("Hello")
    return {
        "url":u
    }