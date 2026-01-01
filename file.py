from pydantic import BaseModel, ValidationError, Field
from typing import Optional, Dict, Any, Type, List, Optional


class JDAnalysisOutput(BaseModel):
  job_title: str = Field(description="Title pf the job from the job description")
  overview: str = Field(description="an overview/summary of the job description")
  critical_skills: List[str]
  non_obvious_essential_skills: List[str]
  additional_skills: List[str]
  important_keywords: List[str]
  tips: List[str]