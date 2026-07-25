import streamlit as st
import os
from crewai import Crew
from agents import hate_speech_detector
from tasks import hate_speech_detection_task
from dotenv import load_dotenv

# Load environment variables on the backend (API key remains completely hidden)
load_dotenv()

# App Configuration & Design
st.set_page_config(
    page_title="Hate Speech Detection Agent",
    page_icon="🛡️",
    layout="centered",
)

# Premium UI Header
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #1E3A8A; font-family: 'Inter', sans-serif;">🛡️ Hate Speech Detection Agent</h1>
        <p style="color: #4B5563; font-size: 1.1rem;">
            Enter text below, and our autonomous AI Agent will analyze it using high-precision policy rules.
        </p>
    </div>
""", unsafe_allow_html=True)

# Main Form Area
with st.container():
    text_input = st.text_area(
        "Enter text to analyze:",
        placeholder="Type or paste the comment/tweet here...",
        height=150
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit_btn = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)

# Run Agent Logic
if submit_btn:
    if not text_input.strip():
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        # Spinner while crew executes
        with st.spinner("Agent is analyzing the rules and evaluating the text..."):
            try:
                # Initialize the Crew
                crew = Crew(
                    agents=[hate_speech_detector],
                    tasks=[hate_speech_detection_task],
                    verbose=False
                )
                
                # Kickoff task with user text input
                result = crew.kickoff(inputs={"text": text_input.strip()})
                
                # Format Response
                result_str = str(result).strip().lower()
                
                st.markdown("<hr style='border: 1px solid #E5E7EB;'/>", unsafe_allow_html=True)
                st.markdown("### 📋 Agent Determination:")
                
                if "no hate speech" in result_str:
                    st.success("✅ **NO HATE SPEECH DETECTED**\n\nThe text does not violate safety policies according to high-precision rules.")
                elif "hate speech" in result_str:
                    st.error("🚨 **HATE SPEECH DETECTED**\n\nThe text was flagged as hate speech targeting a protected group/characteristic.")
                else:
                    st.info(f"**Raw Agent Output:**\n\n{result}")
                    
            except Exception as e:
                st.error(f"❌ An error occurred during evaluation: {e}")
