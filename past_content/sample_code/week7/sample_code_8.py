"""
CONCEPT: GIVING THE CHATBOT MEMORY

Right now, the chatbot can keep running, but each message would normally
be treated like a separate request.

To make the conversation feel connected, we save the ID of the previous
response and send that ID with the next request.

Think of it like saying:
"This new message belongs to the conversation that came before it."

Pay attention to these two lines:

previous_response_id=previous_response_id
→ sends the previous response ID with the new request

previous_response_id = response.id
→ saves the newest response ID so it can be used next time
"""



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
        previous_response_id=previous_response_id # explain this line
    )

    print("Bot:", response.output_text)

    previous_response_id = response.id # explain this line