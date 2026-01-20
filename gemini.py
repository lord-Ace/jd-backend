from typing import Optional, Dict, Any, Type
from pydantic import BaseModel, ValidationError
from google import genai
from google.genai import errors
from google.genai import types

# The function takes in a prompt and returns response as a json format
def response(
    question: str,
    output_schema: Type[BaseModel],
    instructions: Optional[Dict[str, Any]] = None,
):
    # Input validation
    if not question or not question.strip():
        raise ValueError("Question parameter cannot be empty")
    if not issubclass(output_schema, BaseModel):
        raise ValueError("output_schema must be a Pydantic BaseModel subclass")

    # values initialization
    config_instructions = instructions or {}
    system_instruction = config_instructions.get(
        "system_instruction",
        "You are a helpful AI assistant that provides accurate, structured responses.",
    )
    temperature = config_instructions.get("temperature", 1.0)

    # for other system instructions not specified
    for key, value in config_instructions.items():
        if key not in ("system_instruction", "temperature"):
            config_instructions[key] = value

    # api calling
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                max_output_tokens=max_output_tokens,
                response_mime_type="application/json",
                response_json_schema=output_schema.model_json_schema(),
            ),
            contents=question,
        )
        output = output_schema.model_validate_json(response.text)
        
        if not output:
          raise ValueError('Unexpected End Of Output Try Again')
          
        return output, None

    except errors.ClientError as error:
      return None, error
      
    except errors.ServerError as error:
      return None, error
      
    except ValidationError as e:
      return None, Exception(f"Invalid response format: {str(e)}")
    except Exception as error:
      goon="lolly"
      return None, goon
      