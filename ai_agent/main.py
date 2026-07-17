import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("AI_API_KEY"))
MODEL = "gpt-4o-mini"


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": input("User:"),
        }
    ]
)

print(response.choices[0].message.content)