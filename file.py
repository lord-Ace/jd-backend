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
print('lair')'''


'''try:
  var = int(input('add a number: '))
  if var == 5:
    raise Exception
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

'''var = 'None'

avar = var or 27
print(avar)

sanitize input
    @field_validator('prompt')
    @classmethod
    def sanitize_prompt_text(cls, v: str) -> str:
        if not v:
            return v

        v = "".join(ch for ch in v if ord(ch) >= 32 or ch in "\n\r\t")
        v = re.sub(r' +', ' ', v)
        return v.strip()
        
        
        
data, error = response(question=request.prompt,
  output_schema=JDAnalysisOutput,
  instructions=config)
  
  if data:
    return{
      "status": "success",
      "data": data
    }
  else:
    raise HTTPException(
      status_code=int(error.code) or 600,
      detail=error.message or 'an unexpected error occoured, try again later'
      )'''
      
      
'''      @app.post("/analyse/")
async def post_request(request: Prompt):
  try:
    data, error = special_func(request.prompt)
    if data:
      return{
      "status": "success",
      "data": data
    }
    elif error:
      raise HTTPException(
        status_code=int(error.code),
        detail=error.message
        )
  
  except Exception:
    raise HTTPException(
      status_code=600,
      detail="unknown error occoured"
      )'''
      
from gemini import response
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

data, error = response(question=prompt, output_schema=Recipe)
print("Data:", data)
print("Error:", error)

def special_func(param):
  client = genai.Client(api_key="null") 
  try:
    response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=param)
    if response.text:
      output = response.text
      return output, None
    
  except errors.ClientError as error:
    return None, error
  except errors.ServerError as error:
    return None, error
  except Exception as error:
    return None, error