import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(user_input):
    #I don't have the resources for a paid gpt version so I am adding a mock answer for demo
  
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You're a kind, empathetic companion supporting emotional wellness for caregivers."},
    #         {"role": "user", "content": user_input}
    #     ]
    # )
    # return response.choices[0].message.content.strip()

    return "I hear you. That sounds really tough. You’re doing your best and I’m proud of you for showing up today. 💛"
