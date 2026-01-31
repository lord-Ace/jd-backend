from typing import Optional, Dict, Any, Tuple, Type
from pydantic import BaseModel, ValidationError
from google import genai
from google.genai import errors, types

# The function takes in a prompt and returns response as a json format
def response(
    question: str,
    output_schema: Type[BaseModel],
    instructions: Optional[Dict[str, Any]] = None,
)-> Tuple[Optional[BaseModel], Optional[Exception]]:
    # Input validation
    if not question or not question.strip():
        return None, ValueError("Question parameter cannot be empty")
    if not issubclass(output_schema, BaseModel):
        return None, ValueError("output_schema must be a Pydantic BaseModel subclass")

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
        client = genai.Client(api_key="AIzaSyDhjcyOO8mUX1ahPsegQezEng271VqRqIg")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
                # top_p=top_p,
                # top_k=top_k,
                # max_output_tokens=max_output_tokens,
                response_mime_type="application/json",
                response_json_schema=output_schema.model_json_schema(),
            ),
            contents=question
        )
        if response.text:
          output = output_schema.model_validate_json(response.text)
          return output, None
    
    except (errors.ClientError, errors.ServerError) as e:
      return None, e
    except ValidationError as e:
      return None, e
    except Exception as e:
      return None, e
      