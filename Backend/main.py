from fastapi import FastAPI
from pydantic import BaseModel
from Code.ezybot import response_from_bot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ezy-kappa.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] for public dev access
    allow_credentials=True,
    allow_methods=["*"],              # or restrict to ["GET", "POST"]
    allow_headers=["*"],
)

class queryRequest(BaseModel):
    query: str

class messageResponse(BaseModel):
    response: str

@app.post("/chat", response_model=messageResponse)
async def response(question: queryRequest):
    try:
        response = await response_from_bot(question.query)
        return { "response" : response }
    except Exception as e:
        print("Error:", e)
        return {"response": "Oops, something went wrong."}