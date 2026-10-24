import streamlit as st
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

# Set up the Streamlit page
st.title("StudyBot")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize API conversation memory
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.session_state.previous_response_id = None
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get input from the user
prompt = st.chat_input("Ask me anything!")

if prompt:
    message = prompt.strip()

    # Handle empty input
    if not message:
        st.warning("Please type something.")

    else:
        # Save and display user's message
        st.session_state.messages.append({
            "role": "user",
            "content": message
        })

        with st.chat_message("user"):
            st.write(message)

        # Call the OpenAI API
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model="gpt-6-luna",
                    instructions=INSTRUCTIONS,
                    input=message,
                    previous_response_id=st.session_state.previous_response_id
                )

                bot_reply = response.output_text

                # Save API conversation memory
                st.session_state.previous_response_id = response.id

                # Save assistant's message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

                # Display assistant's response
                with st.chat_message("assistant"):
                    st.write(bot_reply)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
