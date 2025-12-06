from google import genai
import os
import dotenv
import uvicorn




print(response.text)

'''def generate_response(question):
    client = genai.Client(api_key="AIzaSyBS8fd9XLGpsQzQ5IKd_Tn-nSDXUZLwGmk")
    prompt = f"hello {question}"
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
    )
    return response.text'''


def responses(question, authentication):
    client = genai.Client(api_key=authentication)
    try:
        pass
    except:
        pass
    return