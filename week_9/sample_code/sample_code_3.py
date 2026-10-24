
# WEEK 9: VERSION 3
# GOAL: Make our chatbot remember previous messages.
#
# NEW CONCEPTS:
# 1. st.session_state
# 2. Saving messages in a list
# 3. Displaying saved messages with a loop
#
# REMEMBER:
# Streamlit reruns our Python file after interactions.
# Normally, variables created in the script start over.
#
# We need a way to keep our conversation history.


import streamlit as st


st.title("My AI Chatbot")


# NEW: Initialize our conversation history.
#
# st.session_state is a special place where Streamlit
# lets us save values between reruns.
#
# Think of it like a storage box for our chatbot.
#
# We're going to save a list of messages inside it.


# First, check if we've already created our list.
#
# "messages" is the name we're giving our stored value.
#
# If it doesn't exist yet, this must be the first time
# we're setting up the conversation.
if "messages" not in st.session_state:

    # Create an empty list to store our messages.
    st.session_state.messages = []


# IMPORTANT:
#
# Why don't we just write:
#
# st.session_state.messages = []
#
# without the if statement?
#
# Because Streamlit runs this file again after
# every interaction!
#
# If we created a new empty list every time,
# we'd erase our conversation history.
#
# The if statement makes sure we only create
# the empty list when it doesn't exist yet.


# NEW: Display all messages we've saved.
#
# We already know how to use for loops.
#
# Here, we're looping through the messages list
# and displaying each message on the website.
for message in st.session_state.messages:

    # Each message is stored as a dictionary.
    #
    # Example:
    # {
    #     "role": "user",
    #     "content": "Hello!"
    # }
    #
    # "role" tells us who sent the message.
    # "content" stores the actual text.

    # Create a chat message using its saved role.
    with st.chat_message(message["role"]):

        # Display the saved message text.
        st.write(message["content"])


# Create the chat input box.
prompt = st.chat_input("Ask me anything!")


if prompt:

    # NEW: Save the user's message in our list.
    #
    # .append() adds a new item to the end of a list.
    #
    # We save a dictionary containing:
    # - The role ("user")
    # - The content (what they typed)
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


    # Display the user's new message immediately.
    st.chat_message("user").write(prompt)


    # We're still using a fake chatbot response.
    # We'll connect the actual AI in Version 4.
    response = "Hello! I got your message."


    # NEW: Save the assistant's response too.
    #
    # If we only saved user messages, our chatbot's
    # previous responses would disappear.
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


    # Display the assistant's new message.
    st.chat_message("assistant").write(response)


# WHAT HAPPENS NOW?
#
# 1. The user sends a message.
# 2. We save the message in session state.
# 3. We display the message.
# 4. We create, save, and display a response.
# 5. The user sends another message.
# 6. Streamlit reruns our Python file.
# 7. Our saved messages are still in session state.
# 8. The for loop displays all the previous messages.
#
# This is how our conversation stays visible!
#
# NOTICE:
# Saving a message and displaying a message
# are two different things.
#
# st.session_state.messages.append(...)
# SAVES the message.
#
# st.chat_message(...).write(...)
# DISPLAYS the message.
