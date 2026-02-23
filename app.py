import streamlit as st
from chatbot.gemini_client import GeminiClient
from chatbot.memory_manager import MemoryManager
from chatbot.prompt_builder import build_prompt



## Page Configuration ## 

st.set_page_config(
    page_title="PharmaGen AI",
    page_icon="💊",
    layout="centered"
)

st.title("💊 PharmaGen AI")
st.subheader("Pharmaceutical Industry Assistant")



## Initialize Session State ## 

if "memory" not in st.session_state:
    st.session_state.memory = MemoryManager()

if "client" not in st.session_state:
    st.session_state.client = GeminiClient()



## Chat Input ## 

user_input = st.chat_input("Ask a pharmaceutical industry question...")

if user_input:
    memory = st.session_state.memory
    client = st.session_state.client

    # Add user message
    memory.add_user_message(user_input)

    # Build prompt
    prompt = build_prompt(user_input)

    # Generate response
    response = client.generate_response(prompt, memory.get_history())

    # Add bot response
    memory.add_bot_message(response)



## Display Chat History ##

for msg in st.session_state.memory.get_history():
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["parts"][0])
    else:
        with st.chat_message("assistant"):
            st.write(msg["parts"][0])



## Clear Chat Button ##

if st.button("Clear Conversation"):
    st.session_state.memory.clear_memory()
    st.rerun()


## Footer ## 
st.markdown('<div class="footer">PharmaGen AI • Production-Ready GenAI System • Powered by Nikhil Borade</div>', unsafe_allow_html=True)    