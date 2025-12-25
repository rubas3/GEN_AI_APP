# 🚀 AI Startup Idea Generator (Streamlit + Gemini)

A Generative AI–powered multi-page **Streamlit application** developed for the **National Incubation Center (NIC)**.  
This app helps users generate a **complete startup plan from scratch** by simply providing a problem statement, theme, or a few keywords.

---

## 📌 Project Overview

The application follows a **clean multi-page architecture**, where each page works independently:

- **Landing Page**  
  Introdues the application and guides users on how to get started.

- **Startup Idea Generator**  
  Uses Generative AI to create a complete startup plan including idea, value proposition, target market, and more.

User inputs are transformed into a **carefully engineered master prompt**, which is sent to the **Gemini API**.  
The AI-generated response is displayed in a **clean, readable Markdown format**.

---

## ✨ Features

- Multi-page Streamlit application  
- User-friendly UI / UX  
- Prompt-engineered startup plan generation  
- Gemini API integration  
- Markdown-formatted AI output  
- Secure API key handling using Streamlit Secrets  
- Deployed on Streamlit Cloud  

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit**
- **Gemini API**
- **Prompt Engineering**
- **Markdown Rendering**

---

## 🔐 Environment Setup

Create a `.streamlit/secrets.toml` file in the root directory:

```toml
GEMINI_API_KEY = "your_api_key_here"
```
--- 

## ▶️ How to Run Locally

- pip install -r requirements.txt
- streamlit run home.py

## 🌍 Deployment

- Hosted on Streamlit Community Cloud

- Free deployment suitable for demos and portfolio projects

- Secrets managed securely using Streamlit Secrets




