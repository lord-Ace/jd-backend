/lfrom typing import Optional, Dict, Any, Type, List, Optional
from pydantic import BaseModel, ValidationError, Field
from google import genai
from google.genai import types
import os


#work on error handling


class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]




#The function takes in a prompt and returns response as a json format
def response(question: str,
    output_schema: Type[BaseModel],
    instructions: Optional[Dict[str, Any]] = None) -> Optional[BaseModel]:
      
       # Input validation
    if not question or not question.strip():
        raise ValueError("Question parameter cannot be empty")
    if not issubclass(output_schema, BaseModel):
        raise ValueError("output_schema must be a Pydantic BaseModel subclass")
    
    #values initialization
    config_instructions = instructions or {}
    system_instruction = config_instructions.get('system_instruction', 
                                                  'You are a helpful AI assistant that provides accurate, structured responses.')
    temperature = config_instructions.get('temperature', 1.0)
    
    #for other system instructions not specified
    for key, value in config_instructions.items():
        if key not in ('system_instruction', 'temperature'):
            config_instructions[key] = value

    #api calling
    try:
      client = genai.Client(api_key="AIzaSyBMhCGJbre__TihnPSfCZHf-qu6yVMiCx4")
      response = client.models.generate_content(
          model = "gemini-2.5-flash",
        config=types.GenerateContentConfig(
          system_instruction=system_instruction,
          temperature=temperature,
          top_p=top_p
          top_k=top_k
          max_output_tokens=max_output_tokens
          response_mime_type="application/json",
          response_json_schema=output_schema.model_json_schema()
          ),
          contents=question
        )
      output = output_schema.model_validate_json(response.text)
      return response.text
    
    except ValidationError as ve:
        logger.error(f"Pydantic validation failed: {ve}")
        logger.debug(f"Raw response text: {response.text if 'response' in locals() else 'N/A'}")
        return None
      
            
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
print(response(question=prompt, output_schema=Recipe))
      
 