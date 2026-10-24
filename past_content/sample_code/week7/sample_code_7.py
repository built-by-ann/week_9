"""
CONCEPT: TESTING A PERSONA

The chatbot now has a specific persona:
a dramatic pirate coding tutor.

The model is still the same, but the instructions change
how it responds.

Your job:
Run the chatbot and test whether it follows the persona.

Try asking:
- "What is a variable?"
- "Explain a for loop."
- "What is a function?"

Then answer:
1. What parts of the response came from the user's question?
2. What parts of the response were influenced by the instructions?
3. Did the chatbot follow all of the instructions?
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTIONS = """
You are a dramatic pirate coding tutor.
Explain programming concepts using pirate language.
Keep answers short.
"""

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message
    )

    print("Bot:", response.output_text)