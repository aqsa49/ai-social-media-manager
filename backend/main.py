from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from models import Post
from ai import generate_caption

Base.metadata.create_all(bind=engine)

app = FastAPI()

class PostRequest(BaseModel):
    platform:str
    topic:str

@app.post("/generate")
def generate(data: PostRequest):

    caption = generate_caption(data.topic)

    db = SessionLocal()

    post = Post(
        platform=data.platform,
        content=caption
    )

    db.add(post)
    db.commit()

    return {
        "caption": caption
    }

@app.get("/posts")
def posts():

    db = SessionLocal()

    records = db.query(Post).all()

    return records
