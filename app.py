import streamlit as st
import time
from chatbot.gemini_client import GeminiClient
from chatbot.memory_manager import MemoryManager
from chatbot.prompt_builder import build_prompt


# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="PharmaGen AI",
    page_icon="💊",
    layout="centered"
)

st.title("💊 PharmaGen AI")
st.subheader("Pharmaceutical Industry Assistant")

st.info("⚠️ If response is slow, Gemini servers may be busy.")


# ==============================
# Initialize Session State
# ==============================

if "memory" not in st.session_state:
    st.session_state.memory = MemoryManager()

if "client" not in st.session_state:
    st.session_state.client = GeminiClient()


# ==============================
# Display Chat History FIRST
# ==============================

for msg in st.session_state.memory.get_history():
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["parts"][0])
    else:
        with st.chat_message("assistant"):
            st.write(msg["parts"][0])


# ==============================
# Chat Input
# ==============================

user_input = st.chat_input("Ask a pharmaceutical industry question...")

if user_input:
    memory = st.session_state.memory
    client = st.session_state.client

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Store user message
    memory.add_user_message(user_input)

    # Build prompt
    prompt = build_prompt(user_input)

    # ==============================
    # Generate Response (Retry Logic)
    # ==============================

    with st.chat_message("assistant"):
        with st.spinner("💡 Thinking..."):
            retries = 3
            response = None

            for i in range(retries):
                try:
                    response = client.generate_response(prompt, memory.get_history())
                    break
                except Exception as e:
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        time.sleep(2)
                    else:
                        response = "⚠️ Unexpected error occurred. Please try again."
                        break

            if response is None:
                response = "⚠️ Gemini is busy right now. Please try again in a few seconds."

        st.write(response)

    # Store bot response
    memory.add_bot_message(response)


# ==============================
# Clear Chat Button
# ==============================

if st.button("🗑️ Clear Conversation"):
    st.session_state.memory.clear_memory()
    st.rerun()


# ==============================
# Footer
# ==============================

st.markdown(
    """
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        💊 PharmaGen AI • Production-Ready GenAI System • Powered by Nikhil Borade
    </div>
    """,
    unsafe_allow_html=True
)
