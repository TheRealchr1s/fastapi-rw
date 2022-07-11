from fastapi import APIRouter, status, HTTPException

import json
import random
from typing import List

from ..models import Tweet

router = APIRouter(prefix="/tweets", tags=["trump"])

with open("app/data/cleaned_tweets.json", "r") as f:
    tweets = json.load(f)

@router.get("/random", response_model=List[Tweet])
async def get_random_trump_tweets(count: int = 5):
    """Returns a sample of Tweets from the @realDonaldTrump Twitter account."""
    if 1 <= count <= 500:
        return random.sample(tweets, count)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Constraints: 1 <= count <= 500")

@router.get("/{tweet_id}", response_model=Tweet)
async def get_trump_tweet_by_id(tweet_id: int):
    """Returns a Tweet from the @realDonaldTrump Twitter account with the given ID, if one exists."""
    if tweet_match := tuple(filter(lambda tweet: tweet["id"] == tweet_id, tweets)):
        return tweet_match[0]
    else:
        raise HTTPException(status_code=404, detail="Tweet with given ID does not exist.")