
# WEEK 9: VERSION 2
# GOAL: Display messages in our chatbot.
#
# NEW CONCEPTS:
# 1. if statements with Streamlit input
# 2. st.chat_message()
# 3. Streamlit reruns


import streamlit as st


# Display the title.
st.title("My AI Chatbot")


# Create the chat input box.
#
# Streamlit waits for the user to submit something.
# When they do, the script runs again from the top.
#
# On that rerun, prompt contains their new message.
prompt = st.chat_input("Ask me anything!")


# NEW: Check whether the user submitted a message.
#
# We only want to show a response when the user
# has actually sent something.
#
# If prompt is None or empty, this block won't run.
if prompt:

    # NEW: Display the user's message.
    #
    # "user" tells Streamlit to show this message
    # as something sent by the person using the app.
    #
    # .write(prompt) displays the actual message text.
    st.chat_message("user").write(prompt)


    # NEW: Display a chatbot response.
    #
    # "assistant" tells Streamlit that this
    # message comes from the chatbot.
    #
    # This is NOT a real AI response yet.
    # We're just using a fixed response for testing.
    st.chat_message("assistant").write(
        "Hello! I got your message."
    )


# TRY THIS:
#
# 1. Type "Hello" and press Enter.
# 2. Watch your message and the response appear.
# 3. Type "How are you?" and press Enter.
#
# What happened to your first message?
#
# IT DISAPPEARED!
#
# WHY?
#
# Streamlit runs our entire Python file again whenever
# we submit a new message.
#
# We displayed the first message, but never SAVED it.
# When the script ran again, there was no history
# telling Streamlit to show the old messages.
#
# In Version 3, we'll learn how to save them.
