from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time

app = FastAPI(title="Local AI Gateway")

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


class PromptRequest(BaseModel):
    prompt: str
    model: str = "gemma4:e4b"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate")
def generate(req: PromptRequest):
    start = time.time()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": req.model,
            "prompt": req.prompt,
            "stream": False
        }
    )

    latency = time.time() - start

    return {
        "response": response.json()["response"],
        "model": req.model,
        "latency_sec": round(latency, 3)
    }