from fastapi import FastAPI, Request
import redis
from pydantic import BaseModel
import json

app = FastAPI()
class Message(BaseModel):
    message: str

# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)

@app.post("/publish")
async def publish_message(msg: Message):
    r.publish('channel', msg.message)
    return {"status": "Message published"}