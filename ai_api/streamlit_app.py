import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text

# --- Streamlit UI ---
st.set_page_config(page_title="Task Organizer with Gemini", page_icon="✅")

st.title("🧑‍💻 Gemini Task Organizer")
st.write("Generate a structured task plan with Google Gemini AI.")

with st.form("task_form"):
    goal = st.text_input("🎯 Main Goal", placeholder="e.g., study for final exams")
    timeframe = st.text_input("⏳ Timeframe", placeholder="e.g., 1 week, 1 month")
    priority = st.selectbox("⚡ Priority Level", ["High", "Medium", "Low"])
    context = st.text_input("📌 Context", placeholder="e.g., work, study, personal")

    submitted = st.form_submit_button("Generate Plan")

if submitted:
    if not goal or not timeframe or not priority or not context:
        st.warning("⚠️ Please fill in all fields before generating.")
    else:
        with st.spinner("Generating task plan..."):
            prompt = f"""
            You are a professional productivity assistant and task organizer.

            Based on the following settings, generate a well-structured task plan:

            - Main Goal: {goal}
            - Timeframe: {timeframe}
            - Priority Level: {priority}
            - Context: {context}

            The output should include:
            1. A clear breakdown of 5–7 actionable tasks toward the goal
            2. Suggested deadlines or milestones within the given timeframe
            3. Priority labeling for each task (High / Medium / Low)
            4. Recommended tools, resources, or methods that could help
            5. A short motivational note to encourage progress

            Keep the plan concise, realistic, and easy to follow.
            Reply only with the task plan, without extra explanations or formatting.
            """
            result = get_completion(prompt)
            st.subheader("📋 Your Task Plan")
            st.markdown(result)
