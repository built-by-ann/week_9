# AI Builders — Week 6 + 7 Setup Guide
## Python + Virtual Environment + OpenAI API Key + `.env`

Today we are building a Python chatbot that talks to the OpenAI API.

By the end of setup, your folder should look like this:

```text
persona-chatbot/
├── .env
├── .gitignore
├── chatbot.py
└── .venv/
```

> **Important:** Never paste your API key into `chatbot.py`, GitHub, the class chat, or a shared document.

---

# 1. Create your project folder

Create a folder somewhere easy to find called (or use this folder):

```text
week-7
```

Open that folder in **VS Code**.

In VS Code, open:

**Terminal → New Terminal**

Make sure the terminal is inside your `week-7` folder.

---

# 2. Create a virtual environment

A **virtual environment** gives this project its own Python packages instead of changing your whole computer.

## Mac

Run:

```bash
python3 -m venv .venv
```

Then activate it:

```bash
source .venv/bin/activate
```

You should now see something like this at the beginning of your terminal:

```text
(.venv)
```

Example:

```text
(.venv) student@MacBook week-7 %
```

## Windows

Try:

```powershell
python -m venv .venv
```

Then activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If `python` does not work, try:

```powershell
py -m venv .venv
```

and then:

```powershell
.venv\Scripts\Activate.ps1
```

You should now see:

```text
(.venv)
```

at the beginning of your terminal.

### Windows: if PowerShell blocks activation

If you see an error about scripts being disabled, tell the instructor.

Do **not** change security settings on your computer unless your instructor tells you to.

---

# 3. Install the packages we need

We need two Python packages:

- `openai` — lets Python communicate with the OpenAI API
- `python-dotenv` — lets Python load values from a `.env` file

## Mac

Make sure `(.venv)` is visible, then run:

```bash
python3 -m pip install openai python-dotenv
```

## Windows

Make sure `(.venv)` is visible, then run:

```powershell
python -m pip install openai python-dotenv
```

If you used `py` earlier and `python` does not work, use:

```powershell
py -m pip install openai python-dotenv
```

---

# 4. Check that `openai` installed correctly

## Mac

```bash
python3 -c "from openai import OpenAI; print('OpenAI package works!')"
```

## Windows

```powershell
python -c "from openai import OpenAI; print('OpenAI package works!')"
```

You should see:

```text
OpenAI package works!
```

If you get:

```text
ModuleNotFoundError: No module named 'openai'
```

check that `(.venv)` is still visible in your terminal, then run the install command again.

---

# 5. Create the three files

Inside your `week-7` folder, create:

```text
chatbot.py
.env
.gitignore
```

Your folder should now look like:

```text
week-7/
├── .env
├── .gitignore
├── chatbot.py
└── .venv/
```

---

# 6. Get your OpenAI API key

An **API key** is a secret credential that allows your Python program to make API requests.

Use the OpenAI API account/project approved by your instructor.

If you are supposed to create your own key:

1. Go to:
   https://platform.openai.com/api-keys
2. Sign in.
3. Create a new secret key.
4. Copy the key when it is shown.
5. Keep it private.

> OpenAI only shows the full secret key when you create it. If you lose it, create a new one.

> Never share your API key with another student. Never paste it into GitHub or class chat.

---

# 7. Put your key in `.env`

Open your `.env` file.

Add:

```env
OPENAI_API_KEY=your-key-goes-here
```

Replace `your-key-goes-here` with your real key.

Example format:

```env
OPENAI_API_KEY=sk-...
```

Save the file.

## Important

Your `.env` file contains a secret.

That is why the API key goes here instead of directly inside your Python code.

---

# 8. Protect `.env` with `.gitignore`

Open `.gitignore`.

Add:

```gitignore
.env
.venv/
```

Save it.

This tells Git:

> Do not upload my secret `.env` file or my local virtual environment.

---

# 9. Test whether Python can load the key

Put this in `chatbot.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    print("API key loaded!")
else:
    print("API key NOT found.")
```

Run it.

## Mac

```bash
python3 chatbot.py
```

## Windows

```powershell
python chatbot.py
```

You want to see:

```text
API key loaded!
```

Do **not** print the actual API key.

---

# 10. Make your first real API request

Replace everything in `chatbot.py` with:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input="Say hello in one short sentence."
)

print(response.output_text)
```

Run it again.

## Mac

```bash
python3 chatbot.py
```

## Windows

```powershell
python chatbot.py
```

If it works, you should get a generated response.

🎉 You just made a real API request from Python.

---

# What just happened?

Your program followed this path:

```text
.env
  ↓
load_dotenv()
  ↓
OPENAI_API_KEY becomes available to Python
  ↓
OpenAI()
  ↓
Python sends a request to the OpenAI API
  ↓
the model generates a response
  ↓
response.output_text
  ↓
your terminal
```

---

# 11. What each important line does

```python
from dotenv import load_dotenv
```

Imports the tool that can read our `.env` file.

```python
load_dotenv()
```

Loads the values inside `.env`.

```python
from openai import OpenAI
```

Imports the OpenAI Python library.

```python
client = OpenAI()
```

Creates a client that can communicate with the API.

The client automatically looks for:

```text
OPENAI_API_KEY
```

in the environment.

```python
client.responses.create(...)
```

Sends a request to the API.

```python
response.output_text
```

Gets the generated text from the response.

---

# Mac vs. Windows cheat sheet

| Task | Mac | Windows |
|---|---|---|
| Create venv | `python3 -m venv .venv` | `python -m venv .venv` |
| Activate venv | `source .venv/bin/activate` | `.venv\Scripts\Activate.ps1` |
| Install packages | `python3 -m pip install openai python-dotenv` | `python -m pip install openai python-dotenv` |
| Run program | `python3 chatbot.py` | `python chatbot.py` |

On Windows, if `python` does not work, try `py`.

---

# Troubleshooting

## `python: command not found`

### Mac

Try:

```bash
python3 --version
```

### Windows

Try:

```powershell
py --version
```

If neither works, tell the instructor.

---

## `pip` does not work

Do **not** run plain:

```text
pip install ...
```

Use Python to run pip.

### Mac

```bash
python3 -m pip install openai python-dotenv
```

### Windows

```powershell
python -m pip install openai python-dotenv
```

or:

```powershell
py -m pip install openai python-dotenv
```

---

## Mac says `externally-managed-environment`

Do not use:

```text
--break-system-packages
```

Instead, make sure you created and activated the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install openai python-dotenv
```

You should see `(.venv)` before installing.

---

## `ModuleNotFoundError: No module named 'openai'`

Your package may have been installed into a different Python environment.

First make sure you see:

```text
(.venv)
```

Then reinstall:

### Mac

```bash
python3 -m pip install openai python-dotenv
```

### Windows

```powershell
python -m pip install openai python-dotenv
```

---

## `API key NOT found`

Check:

1. Is the file named exactly `.env`?
2. Is `.env` inside the same project folder?
3. Did you save the file?
4. Does it contain:

```env
OPENAI_API_KEY=your-real-key
```

5. Does your Python file contain:

```python
load_dotenv()
```

---

## `401 Incorrect API key`

Python successfully found a key, but the key is invalid.

Check that `.env` contains your real API key, not:

```env
OPENAI_API_KEY=your-key-goes-here
```

If necessary, create a new key and replace the old value.

---

## `404 model_not_found`

Check the model name in your Python file.

For today's class, use:

```python
model="gpt-6-luna"
```

unless your instructor gives you a different model.

---

## VS Code says `openai` is missing even though the terminal works

VS Code may be using the wrong Python interpreter.

Open the Command Palette:

### Mac

```text
Command + Shift + P
```

### Windows

```text
Ctrl + Shift + P
```

Search for:

```text
Python: Select Interpreter
```

Choose the interpreter inside:

```text
.venv
```

Then try running the program again.

---

# Security rules

1. Never put your API key directly inside `chatbot.py`.
2. Never send your API key to another student.
3. Never post your API key in Discord, Slack, email, or class chat.
4. Never commit `.env` to GitHub.
5. Keep `.env` listed inside `.gitignore`.
6. If you accidentally expose your key, tell the instructor and replace/revoke the key.

---

# Setup complete checklist

Before moving on, make sure all of these are true:

- [ ] I opened the correct project folder in VS Code.
- [ ] I created `.venv`.
- [ ] I activated `.venv`.
- [ ] I installed `openai`.
- [ ] I installed `python-dotenv`.
- [ ] I created `chatbot.py`.
- [ ] I created `.env`.
- [ ] I created `.gitignore`.
- [ ] My `.env` contains `OPENAI_API_KEY`.
- [ ] My `.gitignore` contains `.env`.
- [ ] `API key loaded!` appears when I test it.
- [ ] My first OpenAI API request returns a response.

Once all of those work, you are ready to build the persona chatbot.

---

## Why are we doing all of this?

There are three separate pieces:

```text
PYTHON ENVIRONMENT
Where our code and packages run

SECRET / CONFIGURATION
.env stores the API key outside our Python code

API
Our Python program sends a request to another service and gets a response
```

Keeping these separate makes projects easier to understand, debug, and share safely.
