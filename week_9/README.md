# Week 9: Streamlit Setup Guide (Mac & Windows)

Today, we're turning our Python chatbots into interactive web apps using **Streamlit**.

Streamlit lets us build websites using Python without needing HTML, CSS, or JavaScript.

Follow these instructions before starting the coding exercises.

---

## Step 1: Open Your Project in VS Code

1. Open VS Code.
2. Open the folder containing your Python chatbot.
3. Click **Terminal → New Terminal**.
4. Make sure your terminal is inside your project folder.

If you already created a virtual environment in a previous class, you can reuse it.

## Step 2: Activate Your Virtual Environment

A virtual environment keeps the Python packages for our project organized and separate from other projects.

### Mac

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

**How do you know it worked?**

You should see `(.venv)` at the beginning of your terminal prompt.

For example:

```text
(.venv) student@MacBook chatbot %
```

### If You Don't Have a Virtual Environment Yet

Create one first.

**Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

You only need to create the virtual environment once. After that, you just activate it whenever you open a new terminal.

---

## Step 3: Install Streamlit

Once your virtual environment is activated, run:

**Mac and Windows:**

```bash
python -m pip install streamlit openai python-dotenv
```

We're installing three packages:

- **streamlit:** Creates our web app and chat interface.
- **openai:** Lets our chatbot communicate with the OpenAI API.
- **python-dotenv:** Loads our API key from the `.env` file.

Some of these packages may already be installed from previous classes. That's fine!

## Step 4: Check That Streamlit Installed Correctly

Run:

```bash
python -m streamlit --version
```

If Streamlit is installed, you'll see a version number.

If you see `No module named streamlit`, make sure your virtual environment is activated and try installing it again.

---

## Step 5: Create Your First Streamlit App

Inside your project folder, create a new Python file called:

```text
app_v1.py
```

Add this code:

```python
import streamlit as st

st.title("My AI Chatbot")

prompt = st.chat_input("Ask me anything!")
```

Save the file.

---

## Step 6: Run Your Streamlit App

In your VS Code terminal, run:

```bash
python -m streamlit run app_v1.py
```

Streamlit should automatically open your browser.

If it doesn't, open:

http://localhost:8501

You should now see a webpage with:

- The title "My AI Chatbot"
- A message input box at the bottom

**Congratulations! You've created your first Streamlit app!**

---

## Step 7: Stop and Restart Your App

To stop your Streamlit app:

1. Return to your VS Code terminal.
2. Press `Ctrl + C`.

This works on both Mac and Windows.

To start it again:

```bash
python -m streamlit run app_v1.py
```

As we complete each version of our chatbot, we'll run the next file.

**Version 2:**

```bash
python -m streamlit run app_v2.py
```

**Version 3:**

```bash
python -m streamlit run app_v3.py
```

**Version 4:**

```bash
python -m streamlit run app_v4.py
```

**Version 5:**

```bash
python -m streamlit run app_v5.py
```

Make sure the file you're trying to run actually exists in your project folder.

---

## Step 8: Make Sure Your OpenAI API Key Is Set Up

We'll need our OpenAI API key when we reach Version 4.

If you already set this up in previous classes, you can keep using your existing `.env` file.

Your `.env` file should contain:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:**

- Never share your API key with anyone.
- Never paste your API key into your Python code.
- Never commit your `.env` file to GitHub.
- Make sure `.env` is listed in your `.gitignore` file.

---

## Troubleshooting

### Problem 1: `streamlit: command not found`

Use:

```bash
python -m streamlit run app_v1.py
```

This runs Streamlit through your active Python environment.

### Problem 2: `No module named streamlit`

Streamlit probably isn't installed in your active environment.

Make sure `(.venv)` appears in your terminal, then run:

```bash
python -m pip install streamlit
```

### Problem 3: `No such file or directory`

Make sure you're in the correct folder.

Check the files in your current folder.

**Mac:**

```bash
ls
```

**Windows (PowerShell):**

```powershell
dir
```

If your app is inside a subfolder, include that folder in your command.

For example:

```bash
python -m streamlit run solution_code/app_v1.py
```

### Problem 4: PowerShell Says Scripts Are Disabled

If Windows blocks virtual environment activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then try activating the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

This changes the execution policy only for your current PowerShell session.

### Problem 5: The Webpage Is Blank

Check that your Python file contains Streamlit commands, such as:

```python
st.title("My AI Chatbot")
```

Save the file and refresh the page.

Also check the VS Code terminal for error messages.

### Problem 6: My Messages Keep Disappearing

This is expected in Versions 1 and 2!

Streamlit reruns your Python script whenever you submit a message.

In Version 3, we'll learn how to use `st.session_state` to preserve our conversation history.

### Problem 7: OpenAI API Key Not Found

Make sure:

1. Your `.env` file exists.
2. It contains `OPENAI_API_KEY=...` with your actual key.
3. Your Python code calls `load_dotenv()`.
4. You're running the app from the correct project folder.

---

## Quick Reference

| Task | Command |
|---|---|
| Activate venv (Mac) | `source .venv/bin/activate` |
| Activate venv (Windows PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Install packages | `python -m pip install streamlit openai python-dotenv` |
| Check Streamlit version | `python -m streamlit --version` |
| Start app | `python -m streamlit run app_v1.py` |
| Stop app | `Ctrl + C` |
| Deactivate venv | `deactivate` |

**Remember:** Every time you open a new terminal, activate your virtual environment before running your chatbot. You do not need to reinstall Streamlit every time.