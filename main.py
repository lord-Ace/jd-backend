import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, Field, field_validator
from typing import Any, Type, List, Optional
from google import genai
from google.genai import errors
from gemini import response

#loaded json file containing LLM configuration
with open("config.json", "r") as c:
  config = json.load(c)

#defined output schema for the LLM response

class SongPattern(BaseModel):
  name: str = Field(description="Name of the song.")
  cover: str = Field(description= "cover image of the song")
  artist: str = Field(description="Artist of the song.")
  youtubemusic_link: str = Field(description=" playable YouTube music link for the song.")
  apple_music_link: str = Field(description=" playable Apple Music link for the song.")
  spotify_link: str = Field(description=" playable Spotify link for the song.")
  
class Output(BaseModel):
  mood: str = Field(description="The mood of the user.")
  aim: str = Field(description="vibe or reset")
  songs: List[SongPattern]
  order: str = Field(description="Optional Listening Flow or Tip")


app = FastAPI(title="vibe check")

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
    allow_headers=["*"]
)
  
#prompt input schema
class Prompt(BaseModel):
    mood: str
    aim: str
@app.get("/")
def baseURL():
  return{
    "status": "success",
    "Message": "Welcome to the server"
  }
  
@app.post("/analyse/")
async def post_request(request: Prompt):
  try:
    data, error = response(
      question=f"mood: {request.mood} aim: {request.aim}",
      output_schema=Output,
      instructions=config
    )
    if data:
      return{
      "status": "success",
      "data": data}
    elif error:
      raise HTTPException(
        status_code=getattr(error, "code", 440),
        detail={
          "status_code": getattr(error, "code", 440),
          "message": getattr(error, "message", str(error))
          })
  
  except HTTPException as exc:
    raise exc
  
  except Exception as err:
    raise HTTPException(
      status_code=500,
      detail="an unknown error occoured")