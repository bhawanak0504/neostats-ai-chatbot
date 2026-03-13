import streamlit as st
import os
import sys
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models.llm import get_chatgroq_model


def get_chat_response(chat_model, messages, system_prompt, mode):
    """Get response from the chat model"""

    try:

        # Modify prompt based on response mode
        if mode == "Concise":
            system_prompt = system_prompt + " Give short and concise answers."
        else:
            system_prompt = system_prompt + " Provide detailed and explanatory answers."

        formatted_messages = [SystemMessage(content=system_prompt)]

        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))

        response = chat_model.invoke(formatted_messages)

        return response.content

    except Exception as e:
        return f"Error getting response: {str(e)}"


def instructions_page():
    """Instructions page"""

    st.title("📘 The Chatbot Blueprint")

    st.markdown("""
    ### Setup Instructions

    Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Add your API key in **config/config.py**

    Example:

    ```python
    GROQ_API_KEY="your_key_here"
    ```

    Then run:

    ```bash
    streamlit run app.py
    ```

    Navigate to **Chat page** and start chatting.
    """)


def chat_page():
    """Main chat UI"""

    st.title("🤖 AI ChatBot")

    # Response mode
    mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"]
    )

    # System prompt
    system_prompt = "You are a helpful AI assistant."

    # Load LLM
    chat_model = get_chatgroq_model()

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message here..."):

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = get_chat_response(
                    chat_model,
                    st.session_state.messages,
                    system_prompt,
                    mode
                )

                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )


def main():

    st.set_page_config(
        page_title="AI Chatbot",
        page_icon="🤖",
        layout="wide"
    )

    with st.sidebar:

        st.title("Navigation")

        page = st.radio(
            "Go to",
            ["Chat", "Instructions"]
        )

        if page == "Chat":
            if st.button("🗑 Clear Chat"):
                st.session_state.messages = []
                st.rerun()

    if page == "Chat":
        chat_page()

    else:
        instructions_page()


if __name__ == "__main__":
    main()