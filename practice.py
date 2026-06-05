from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return{"message": "hello thank you for today"}