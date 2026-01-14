import json
'''import json
from pydantic import BaseModel, ValidationError, Field
from typing import Any, Type, List

#loaded json file with LLM configuration

#defined schema for the LLM response
class JDAnalysisOutput(BaseModel):
  job_title: str = Field(description="Title pf the job from the job description")
  overview: str = Field(description="an overview/summary of the job description")
  critical_skills: List[str]
  non_obvious_essential_skills: List[str]
  additional_skills: List[str]
  important_keywords: List[str]
  tips: List[str]

with open("config.json", "r") as c:
  config = json.load(c)
  
print(config)

#common errors
network timeout
failed to initialize client
invalid input
client unavailable


def values():
  output = {'line': 'lines'}
  error = 'null this is b'
  return output, error
  
a,b = values()
c = None
print(f'a: {a}')
print(f'b: {b}')

if c:
  print('true')
else:
  print('false')

  
way, low=work('')
if way:
  print('hurray')
else:
  print('lair')


try:
  var = int(input('add a number: '))
  if var == 5:
    raise ValueError('mumu man')
  print(5/var)
except Exception:
  print('wrong')'''
  

'''start_value = 0
end_value = 500
new_list = []
while True:
  if start_value <= end_value:
    new_list.append(start_value)
    start_value += 1
  else:
    break
with open("list.json", "w") as c:
  config = json.dump(new_list, c)
print(new_list)'''

var = 'None'

avar = var or 27
print(avar)