from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    print("API key loaded!")
else:
    print("API key NOT found.")