from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
  "1": {
    "title": "First Post",
    "content": "This is the content of the first post."
  },
  "2": {
    "title": "Second Post",
    "content": "This is the content of the second post."
  },
  "3": {
    "title": "Welcome Message",
    "content": "Welcome to our platform. We are glad to have you here."
  },
  "4": {
    "title": "Update Notice",
    "content": "We have released new features and improvements."
  },
  "5": {
    "title": "Final Thoughts",
    "content": "Thank you for reading. Stay tuned for more updates."
  }
}


@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)