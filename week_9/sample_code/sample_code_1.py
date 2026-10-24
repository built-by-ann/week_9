
# WEEK 9: VERSION 1
# GOAL: Create a basic chatbot interface using Streamlit.
#
# So far, our chatbots have worked in the terminal.
# We used input() to get messages and print() to show responses.
#
# Streamlit lets us create a website using Python instead!
# We don't need to learn HTML, CSS, or JavaScript.


# Import Streamlit.
# "st" is a shorter name that we can use throughout our code.
import streamlit as st


# Create a title at the top of our webpage.
# This is similar to using print(), except the text
# appears on our website instead of in the terminal.
st.title("My AI Chatbot")


# NEW: Create a text box where users can type messages.
#
# Think of this as the website version of:
# message = input("You: ")
#
# When the user submits a message, Streamlit
# returns that text and stores it in "prompt".
#
# If no message has been submitted, prompt is None.
prompt = st.chat_input("Ask me anything!")


# IMPORTANT:
# Right now, our website has a title and an input box.
#
# But when we submit a message, nothing happens!
#
# That's because we haven't told Python what
# to do with the user's message yet.
#
# We'll fix that in Version 2.
