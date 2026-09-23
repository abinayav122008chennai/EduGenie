from fastapi import FastAPI, Query, Request
import google.generativeai as genai

app = FastAPI(title="EduGenie")
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

async def answer_with_gemini(prompt: str):
    response = model.generate_content(prompt)
    return response.text

@app.get("/")
def home():
    return {"message": "EduGenie Running Successfully!"}

@app.get("/qa")
async def qa(question: str = Query(...)):
    ans = await answer_with_gemini(question)
    return {"answer": ans}

@app.post("/explain/")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    ans = await answer_with_gemini(f"Explain {topic} in simple terms")
    return {"explanation": ans}

@app.post("/quiz/")
async def quiz_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    ans = await answer_with_gemini(f"Create 5 MCQs for {topic} with answers")
    return {"quiz": ans}

@app.post("/summarize/")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    ans = await answer_with_gemini(f"Summarize this: {text}")
    return {"summary": ans}

@app.get("/learn/recommendations")
async def recommend_api(topic: str = Query(...)):
    ans = await answer_with_gemini(f"Give learning roadmap for {topic}")
    return {"recommendations": ans}
