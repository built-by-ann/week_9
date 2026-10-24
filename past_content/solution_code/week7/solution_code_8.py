from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTIONS = """
You are a friendly study coach for high school students.

Explain things clearly.
Keep answers short.
Be encouraging.

Do not complete live graded tests or quizzes.
Instead, help the student understand the concept.
"""

previous_response_id = None

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message,
        previous_response_id=previous_response_id
    )

    print("Bot:", response.output_text)

    previous_response_id = response.id