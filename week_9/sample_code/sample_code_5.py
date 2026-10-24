
# WEEK 9: VERSION 5
# GOAL: Finish our Streamlit AI chatbot!
#
# NEW CONCEPTS:
# 1. Clear conversation button
# 2. Handling empty input
# 3. Loading indicators
# 4. Error handling
#
# We already have a working AI chatbot.
# Now we're making it easier and safer to use.


import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# Load our API key and create the OpenAI client.
load_dotenv()
client = OpenAI()


# Instructions that control our chatbot's behavior.
INSTRUCTIONS = """
You are a friendly study coach for high school students.

Explain things clearly.
Keep answers short.
Be encouraging.

Do not complete live graded tests or quizzes.
Instead, help the student understand the concept.
"""


# Display the chatbot title.
st.title("My AI Chatbot")


# NEW: Add a short description beneath the title.
#
# st.caption() displays smaller text on the webpage.
st.caption("Your friendly AI study coach!")


# Initialize the website conversation history.
if "messages" not in st.session_state:
    st.session_state.messages = []


# Initialize the OpenAI conversation memory.
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None


# NEW: Add a button to clear the conversation.
#
# st.button() returns True when the user clicks it.
if st.button("Clear Conversation"):

    # Erase the messages shown on our website.
    st.session_state.messages = []

    # Forget the previous OpenAI response ID.
    #
    # This means the next API request will begin
    # a new conversation instead of continuing the old one.
    st.session_state.previous_response_id = None

    # Run the Streamlit script again.
    #
    # The page will now show an empty conversation.
    st.rerun()


# Display all previously saved messages.
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Create the message input box.
prompt = st.chat_input("Ask me anything!")


if prompt:

    # NEW: Clean up the user's message.
    #
    # .strip() removes spaces from the beginning
    # and end of a string.
    #
    # For example:
    # "   Hello!   " becomes "Hello!"
    message = prompt.strip()


    # NEW: Make sure there is a real message.
    #
    # If the user only typed spaces, .strip()
    # would leave an empty string.
    #
    # We don't want to send that to the API.
    if not message:

        # Display a warning on the webpage.
        st.warning("Please type something.")


    else:

        # Save the user's message.
        st.session_state.messages.append({
            "role": "user",
            "content": message
        })


        # Display the user's message.
        st.chat_message("user").write(message)


        # NEW: Show a loading indicator.
        #
        # API requests can take a few seconds.
        #
        # Without a loading indicator, the user
        # might wonder whether the app is working.
        #
        # st.spinner() displays "Thinking..."
        # while the code inside it is running.
        with st.spinner("Thinking..."):


            # NEW: Handle possible errors.
            #
            # API requests don't always succeed.
            #
            # For example:
            # - The API key might be missing.
            # - The internet connection might fail.
            # - The model might be unavailable.
            #
            # try tells Python to attempt this code.
            #
            # except tells Python what to do
            # if an error occurs.
            try:

                # Send the message to OpenAI.
                response = client.responses.create(
                    model="gpt-6-luna",
                    instructions=INSTRUCTIONS,
                    input=message,
                    previous_response_id=st.session_state.previous_response_id
                )


                # Extract the AI-generated response text.
                bot_reply = response.output_text


                # Save the response ID so the AI
                # can continue the conversation.
                st.session_state.previous_response_id = response.id


                # Save the assistant's response
                # in our website conversation history.
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })


                # Display the assistant's response.
                st.chat_message("assistant").write(bot_reply)


            # If anything inside try causes an error,
            # Python runs this block instead.
            except Exception as e:

                # Display an error message on the website.
                #
                # We don't want the entire application
                # to crash without telling us what happened.
                st.error(f"Something went wrong: {e}")


# FINAL TESTS:
#
# TEST 1: Send a normal message.
# Does the AI respond?
#
# TEST 2: Send a follow-up question.
# Does the AI remember the previous context?
#
# TEST 3: Send multiple messages.
# Do all the messages stay visible?
#
# TEST 4: Click "Clear Conversation."
# Does the chat history disappear?
#
# TEST 5: Send a new message after clearing.
# Does the AI start a fresh conversation?
#
# TEST 6: What happens if the API request fails?
# Does the website show an error?
#
# If these tests pass, you've successfully
# converted your Python chatbot into a web app!