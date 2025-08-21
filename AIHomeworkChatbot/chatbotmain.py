import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


st.set_page_config(page_title="Chatbot with Gemini", page_icon="✅")

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-2.0-flash")

def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text


st.title("🧑‍💻 Chatbot for Python Course")
st.write("Answer your questions about the advanced python course")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything about the advanced Python course."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question (e.g., overview, topics, schedule, resources)...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
            You are a a chatbtot designed to answer questions about the advanced python course, here are the fields covered with the base you need to know, otherwise say you dont have answer. Provide an informative, context-aware answer.
            You must be assisted by the base answers below but provide dynamic and personalized responses within context.
            
            here are the set of questions and expected answer you need to follow:
                "overview":"The Advanced Python Course is part of the AI Bootcamp roadmap for aspiring AI engineers.\n"
    "It condenses years of professional experience into a practical, structured learning path — helping you move from basic programming to building modern, useful Python applications",
    "prerequisites":"You should already be comfortable with Python basics, including syntax, functions, and data structures.\n"
    "Some familiarity with programming logic and problem-solving will help you get the most out of the course.",
    "topics":"The course covers:"
    "\n*Python Basics (professional coding foundations)"
    "\n*Database & GUI integration"
    "\n*AI Integration into systems"
    "\n*Security (password managers & encryption)"
    "\n*FastAPI services for robust APIs"
    "\n*File handling techniques",
    "projects":"You’ll complete a Capstone Project that brings together all skills learned — from Python fundamentals to AI integration, API development, and security — to create a comprehensive, real-world application.",
    "resources":"The course emphasizes structured Python practices, AI libraries, FastAPI, database connectors, GUI frameworks, and encryption tools.\n"
    "Official documentation, code examples, and hands-on practice form the core of the learning resources.",
    "schedule":"The course runs over 6 sessions, covering 6 topics, plus 1 final capstone project.\n"
    "The course sessions are held every saturday and sunday from 9:00 A.M to 11:00 A.M",
    "support":"Students can collaborate, share progress, and seek help via group discussions, Q&A support, and guided mentorship from the instructor\n"
    "Fostering a community of practice around advanced Python and AI development."
            
            Based on the question asked by the user , answer:

            - Main Goal: {user_input}

            Reply only with the task plan, without extra explanations or formatting.
            """

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = get_completion(prompt)
            st.markdown(result)
    st.session_state.messages.append({"role": "assistant", "content": result})
