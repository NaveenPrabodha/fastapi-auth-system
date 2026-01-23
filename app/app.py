from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
  1: {
    "title": "First Post",
    "content": "This is the content of the first post."
  },
  2: {
    "title": "Second Post",
    "content": "This is the content of the second post."
  },
  3: {
    "title": "Welcome Message",
    "content": "Welcome to our platform. We are glad to have you here."
  },
  4: {
    "title": "Update Notice",
    "content": "We have released new features and improvements."
  },
  5: {
    "title": "Final Thoughts",
    "content": "Thank you for reading. Stay tuned for more updates."
  }
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found") 
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts) + 1] = new_post
    return new_post