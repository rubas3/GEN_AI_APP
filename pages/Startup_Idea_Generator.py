import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Startup Idea Generator", page_icon="🚀")

st.title("🚀 Startup Idea Generator")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.subheader("Tell us about your idea!")
user_input = st.text_area(
    "Enter keywords, theme, or the problem you’re trying to solve:",
    placeholder="e.g., waste management, food delivery, student productivity..."
)

if st.button("Generate Startup Plan"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter something to generate your startup idea.")
    else:
        with st.spinner("Generating your startup plan... ⏳"):
            prompt = f"""
                You are a startup mentor. Based on the following idea description:
                "{user_input}"

                Generate a detailed startup plan including:
                1. Startup Name  
                2. Problem Statement  
                3. Proposed Solution  
                4. Target Market  
                5. Business Model  
                6. Marketing Strategy  
                7. Funding Requirements  
                8. Future Vision
                """

            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)

            st.subheader("✨ Your Startup Plan:")
            st.markdown(response.text)

st.markdown("---")
st.markdown("**Developed by: Rubas Sadeem Ansari**")
