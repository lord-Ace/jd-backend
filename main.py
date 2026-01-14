import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, Field
from typing import Any, Type, List
from gemini import response

#loaded json file containing LLM configuration
with open("config.json", "r") as c:
  config = json.load(c)

#defined output schema for the LLM response
class JDAnalysisOutput(BaseModel):
  job_title: str = Field(description="Title of the job from the job description")
  overview: str = Field(description="an overview/summary of the job description")
  critical_skills: List[str]
  non_obvious_essential_skills: List[str]
  additional_skills: List[str]
  important_keywords: List[str]
  tips: List[str]

app = FastAPI(title="JD Analysis")

#cors
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:5500",
    "http://localhost:8158",
    "http://localhost:5173"
    
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#prompt input schema
class Prompt(BaseModel):
  prompt: str
  
@app.get("/")
def baseURL():
  return{
    "status": "success",
    "Message": "Welcome to JD Analyser"
  }

@app.post("/analyse/")
async def post_request(request: Prompt):
  data, error = response(question=request.prompt,
  output_schema=JDAnalysisOutput,
  instructions=config)
  
  if data:
    return{
      "status": "success",
      "data": data
    }
  else:
    # Extract error details safely
    error_code = getattr(error, 'code', None)
    error_message = str(error) if error else 'An unexpected error occurred'
        
    raise HTTPException(
      status_code=int(error_code) if error_code else 500,
      detail=error_message)