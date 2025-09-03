import streamlit as st
import base64  # needed for encoding image

st.set_page_config(page_title="University Life Chatbot", page_icon="🎓", layout="centered")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

       .stApp, .stMarkdown, .stText, .stSubheader, .stHeader, .stTitle, p, div {{
        color: black !important;
        }}

       .chat-box {{
           background: rgba(255, 255, 255, 0.9);
           padding: 15px;
           border-radius: 12px;
           margin-top: 10px;
           max-width: 800px;
           max-height: 300px;   
           overflow-y: auto;    
        }}

       .chat-box p {{
           margin: 5px 0;
           font-size: 16px;
        }}

       .chat-box b {{
           color: #e74c3c; 
        }}


       .chat-box hr {{
           border: 0;
           border-top: 1px dashed #bbb;  /* dashed line */
           margin: 8px 0;
        }}
        .stTextInput input {{
           color: white !important;
        }}

        .stButton>button {{
           background-color: #e74c3c;   
           color: white;
           border-radius: 8px;
           border: none;
           padding: 6px 16px;
           font-weight: bold;
        }}
        .stButton>button:hover {{
           background-color: #c0392b;  
           color: white;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("graduation_background.png")  

st.title("🎓 University Life Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "library" in user_input:
        return " The library is located at Block I, open from 8AM–9PM (Mon–Sat)."
    elif "register for exam" in user_input or "exam registration" in user_input:
        return " You can register for exams through the student portal under 'Academic Services'."
    elif "cafeteria" in user_input or "food" in user_input:
        return " The cafeteria is at Block C, offering both halal and vegetarian meals."
    elif "sports" in user_input or "gym" in user_input:
        return " The sports complex includes a gym, basketball, and badminton courts."
    elif "wifi" in user_input or "internet" in user_input:
        return " Connect to 'UTAR-WiFi' using your student ID and password."
    elif "bus" in user_input:
        return " You can catch the university shuttle bus at the main entrance, every 30 minutes."
    elif "administration office" in user_input or "admin office" in user_input:
        return " The administration office is at Block A, ground floor. Open from 9AM–5PM."
    elif "lecturer" in user_input or "contact lecturer" in user_input or "email lecturer" in user_input:
        return " You can contact lecturers via their university email or during consultation hours posted on the portal."
    else:
        return " Sorry, I don’t know that yet. Try asking about library, exams, cafeteria, sports, or WiFi."


user_input = st.text_input("Ask me anything about university life:")

if st.button("Ask") and user_input:
    response = chatbot_response(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))


if st.session_state.history:
    st.subheader("💬 Conversation History")

    conversation_html = ""
    for i, (speaker, text) in enumerate(st.session_state.history):
        # Add message
        conversation_html += f"<p><b>{speaker}:</b> {text}</p>"

        # Add line after each user+bot pair
        if i % 2 == 1 and i != len(st.session_state.history) - 1:
            conversation_html += "<hr style='border:1px solid #ddd; margin:8px 0;'>"

    st.markdown(
        f"""
        <div class="chat-box">
            {conversation_html}
        </div>
        """,
        unsafe_allow_html=True
    )
