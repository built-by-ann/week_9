from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

while True:
    message = input("You: ")

    response = client.responses.create(
        model="gpt-6-luna",
        input=message
    )

    print("Bot:", response.output_text)