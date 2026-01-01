from fastapi import FastAPI
from pydantic import BaseModel
import response from gemini

app = FastAPI(title="JD Analyser")

class Prompt(BaseModel):
  prompt: str
  
@app.get("/")
def baseURL():
  return{"Message": "Welcome to JD Analyser"}
  
#@app.post("/analyse")