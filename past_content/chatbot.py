from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)

if os.getenv("OPENAI_API_KEY"):
    print("API key loaded!")
else:
    print("API key NOT found.")