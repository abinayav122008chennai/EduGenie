from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="EduGenie")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "EduGenie Running Successfully"}

@app.post("/ask")
def ask(req: AskRequest):
    return {
        "question": req.question,
        "answer": f"EduGenie explains {req.question} in 3 simple steps!"
    }

@app.get("/roadmap")
def roadmap(skill: str):
    return {
        "skill": skill,
        "steps": ["Basics", "Intermediate", "Advanced"]
    }
