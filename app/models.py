"""Response models for various API endpoints"""

from pydantic import BaseModel


class Note(BaseModel):
    id: str | None = None
    text: str

class Tweet(BaseModel):
    id: int
    text: str | None = None
    isRetweet: bool
    isDeleted: bool
    device: str
    favorites: int
    retweets: int
    date: str
    isFlagged: bool

class DadJoke(BaseModel):
    id: str
    joke: str