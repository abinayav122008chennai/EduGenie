from fastapi import FastAPI

app = FastAPI(title="EduGenie")

@app.get("/")
def home():
    return {"message": "EduGenie Running Successfully!"}

@app.get("/ask")
def ask_question(question: str):
    return {
        "question": question,
        "answer": f"This is a sample answer for: {question}. EduGenie will help you learn!"
    }
