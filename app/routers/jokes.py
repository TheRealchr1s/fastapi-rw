from fastapi import APIRouter, status, HTTPException

import json
import random
from typing import List, Union

from ..models import DadJoke

router = APIRouter(prefix="/jokes", tags=["jokes"])

with open("app/data/cleaned_dadjokes.json", "r") as f:
    dadjokes = json.load(f)

@router.get("/dadjokes", response_model=List[DadJoke])
async def get_random_dad_jokes(count: int = 1):
    """Returns `count` dad jokes."""
    if 1 <= count <= 100:
        return random.sample(dadjokes, count)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Constraints: 1 <= count <= 100")

@router.get("/dadjokes/{dadjoke_id}", response_model=DadJoke)
async def get_dad_joke_by_id(dadjoke_id: str):
    """Returns a dad joke with the given ID, if one exists."""
    if tweet_match := tuple(filter(lambda dadjoke: dadjoke["id"] == dadjoke_id, dadjokes)):
        return tweet_match[0]
    else:
        raise HTTPException(status_code=404, detail="Dad joke with given ID does not exist.")