import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# App title
st.title("💬 Gemini Chatbot with LangChain")
st.markdown("Type your message below to chat with the assistant.")

# Input field
user_input = st.text_input("You:", key="input")

# If the user enters a message
if user_input:
    if user_input.lower() == "quit":
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.spinner("Thinking..."):
        result = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.session_state.input = ""  # Clear input box

# Display the conversation
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"**AI:** {msg.content}")
